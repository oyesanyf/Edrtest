#!/usr/bin/env python3
"""
MITRE ATT&CK STIX Integration Module
Integrates mitreattack-python for threat actor emulation, CTI lookups, and detection mapping.
"""

import os
import sys
from typing import Optional

try:
    from mitreattack.stix20 import MitreAttackData
    from mitreattack.download_stix import download_domains
    MITREATTRACK_AVAILABLE = True
except ImportError:
    MITREATTRACK_AVAILABLE = False


REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_STIX_DIR = os.path.join(REPO_ROOT, "stix")
_ATTACK_DATA_INSTANCE: Optional["MitreAttackData"] = None


def get_stix_file_path(stix_dir: str = DEFAULT_STIX_DIR) -> Optional[str]:
    """Finds or downloads the Enterprise ATT&CK STIX 2.0 bundle."""
    if not MITREATTRACK_AVAILABLE:
        return None

    # Search for an existing enterprise-attack.json in stix_dir
    if os.path.isdir(stix_dir):
        for root, _, files in os.walk(stix_dir):
            for file in files:
                if file.lower() == "enterprise-attack.json":
                    return os.path.join(root, file)

    # If not found, download latest enterprise bundle
    print(f"[*] Downloading latest MITRE Enterprise ATT&CK STIX dataset to {stix_dir}...")
    try:
        os.makedirs(stix_dir, exist_ok=True)
        download_domains(
            domains=["enterprise"],
            download_dir=stix_dir,
            all_versions=False,
            stix_version="2.0",
        )
        for root, _, files in os.walk(stix_dir):
            for file in files:
                if file.lower() == "enterprise-attack.json":
                    return os.path.join(root, file)
    except Exception as e:
        print(f"[-] Failed to download STIX data: {e}", file=sys.stderr)
        return None


def get_attack_data(stix_dir: str = DEFAULT_STIX_DIR) -> Optional["MitreAttackData"]:
    """Returns a cached MitreAttackData instance."""
    global _ATTACK_DATA_INSTANCE
    if _ATTACK_DATA_INSTANCE is not None:
        return _ATTACK_DATA_INSTANCE

    if not MITREATTRACK_AVAILABLE:
        print("[-] 'mitreattack-python' is not installed. Run: pip install mitreattack-python", file=sys.stderr)
        return None

    stix_file = get_stix_file_path(stix_dir)
    if not stix_file or not os.path.isfile(stix_file):
        print("[-] STIX data file not found.", file=sys.stderr)
        return None

    try:
        _ATTACK_DATA_INSTANCE = MitreAttackData(stix_file)
        return _ATTACK_DATA_INSTANCE
    except Exception as e:
        print(f"[-] Error loading MitreAttackData: {e}", file=sys.stderr)
        return None


def get_techniques_for_group(group_query: str, stix_dir: str = DEFAULT_STIX_DIR) -> list[str]:
    """Resolves techniques used by a threat group name, alias, or ID (e.g. APT29, G0016, Lazarus Group)."""
    attack_data = get_attack_data(stix_dir)
    if not attack_data:
        return []

    # Try lookup by attack ID (e.g. G0082)
    group_obj = None
    if group_query.upper().startswith("G") and group_query[1:].isdigit():
        group_obj = attack_data.get_object_by_attack_id(group_query.upper(), "intrusion-set")

    # If not found by ID, search by alias
    if not group_obj:
        matched_groups = attack_data.get_groups_by_alias(group_query)
        if matched_groups:
            group_obj = matched_groups[0]
        else:
            # Case-insensitive scan across all groups
            all_groups = attack_data.get_groups()
            for g in all_groups:
                aliases = [a.lower() for a in getattr(g, "aliases", [])]
                if group_query.lower() == g.name.lower() or group_query.lower() in aliases:
                    group_obj = g
                    break

    if not group_obj:
        print(f"[-] Threat group '{group_query}' not found in MITRE ATT&CK CTI.", file=sys.stderr)
        return []

    ext_id = "N/A"
    for ref in getattr(group_obj, "external_references", []):
        if ref.source_name == "mitre-attack" and hasattr(ref, "external_id"):
            ext_id = ref.external_id
            break

    print(f"\n[*] Found Threat Group: {group_obj.name} (ID: {ext_id})")
    aliases = getattr(group_obj, "aliases", [])
    if aliases:
        print(f"[*] Known Aliases: {', '.join(aliases[:6])}")

    techniques_used = attack_data.get_techniques_used_by_group(group_obj.id)
    tech_ids = set()
    for rel in techniques_used:
        target = rel.get("object")
        if target:
            for ref in getattr(target, "external_references", []):
                if ref.source_name == "mitre-attack" and hasattr(ref, "external_id"):
                    tech_ids.add(ref.external_id)

    sorted_techs = sorted(tech_ids)
    print(f"[*] Attributed Techniques: {len(sorted_techs)}\n")
    return sorted_techs


def show_technique_info(technique_id: str, stix_dir: str = DEFAULT_STIX_DIR) -> None:
    """Displays comprehensive MITRE ATT&CK CTI, detection telemetry components, and threat actor associations."""
    attack_data = get_attack_data(stix_dir)
    if not attack_data:
        return

    tech_obj = attack_data.get_object_by_attack_id(technique_id.upper(), "attack-pattern")
    if not tech_obj:
        print(f"[-] Technique '{technique_id}' not found in MITRE ATT&CK.", file=sys.stderr)
        return

    print("\n" + "=" * 70)
    print(f" MITRE ATT&CK(R) CTI Intel: {tech_obj.name} [{technique_id.upper()}]")
    print("=" * 70)

    # Tactics
    tactics = [
        phase.phase_name.replace("-", " ").title()
        for phase in getattr(tech_obj, "kill_chain_phases", [])
        if phase.kill_chain_name == "mitre-attack"
    ]
    if tactics:
        print(f"\n[+] Tactics: {', '.join(tactics)}")

    # Description (formatted excerpt)
    desc = getattr(tech_obj, "description", "").strip()
    if desc:
        clean_desc = desc.split("\n")[0]
        # Remove markdown citation markers
        import re
        clean_desc = re.sub(r"\(Citation:.*?\)", "", clean_desc).strip()
        print(f"\n[+] Overview:\n    {clean_desc}")

    # Detection data components (critical for EDR validation!)
    data_components = attack_data.get_datacomponents_detecting_technique(tech_obj.id)
    if data_components:
        dc_names = [dc["object"].name for dc in data_components]
        print(f"\n[+] EDR Telemetry & Data Sources Needed for Detection:")
        for name in sorted(set(dc_names)):
            print(f"    - {name}")

    # Associated threat groups
    groups = attack_data.get_groups_using_technique(tech_obj.id)
    if groups:
        group_list = []
        for g in groups:
            obj = g["object"]
            gid = "N/A"
            for ref in getattr(obj, "external_references", []):
                if ref.source_name == "mitre-attack" and hasattr(ref, "external_id"):
                    gid = ref.external_id
                    break
            group_list.append(f"{obj.name} [{gid}]")
        print(f"\n[+] Known Threat Actors Utilizing This Technique ({len(group_list)}):")
        # Print first 10
        for item in group_list[:10]:
            print(f"    * {item}")
        if len(group_list) > 10:
            print(f"    * ... and {len(group_list) - 10} more.")

    print("\n" + "=" * 70 + "\n")
