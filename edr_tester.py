#!/usr/bin/env python3
"""
EDR Telemetry & Atomic Testing Harness
Executes Atomic Red Team tests locally or remotely to validate EDR alerts.
Maps to MITRE ATT&CK Tactics, Techniques, Enterprise Matrices, and CTI via mitreattack-python.
"""

import argparse
import csv
import os
import re
import subprocess
import sys
import winrm


# Project root directory (atomics and engine default to root folder)
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ATOMICS_PATH = os.path.join(REPO_ROOT, "atomics")
DEFAULT_INVOKE_PATH = os.path.join(REPO_ROOT, "invoke-atomicredteam", "Invoke-AtomicRedTeam.psd1")


def get_atomics_path(override_path: str | None = None) -> str:
    """Returns the atomics folder path, prioritizing the root folder of the code."""
    if override_path and os.path.isdir(override_path):
        return override_path

    root_path = os.path.join(REPO_ROOT, "atomics")
    if os.path.isdir(root_path):
        return root_path

    # Fallback paths
    fallbacks = [
        r"D:\tools\redteam\atomics",
        os.path.expandvars(r"%HOMEDRIVE%\AtomicRedTeam\atomics"),
        r"C:\AtomicRedTeam\atomics",
    ]
    for p in fallbacks:
        if os.path.isdir(p):
            return p
    return root_path


def get_module_path(override_path: str | None = None) -> str:
    """Returns the Invoke-AtomicRedTeam.psd1 path, prioritizing the root folder of the code."""
    if override_path and os.path.isfile(override_path):
        return override_path

    root_module = os.path.join(REPO_ROOT, "invoke-atomicredteam", "Invoke-AtomicRedTeam.psd1")
    if os.path.isfile(root_module):
        return root_module

    # Fallback paths
    fallbacks = [
        r"D:\tools\redteam\invoke-atomicredteam\Invoke-AtomicRedTeam.psd1",
        os.path.expandvars(r"%HOMEDRIVE%\AtomicRedTeam\invoke-atomicredteam\Invoke-AtomicRedTeam.psd1"),
        r"C:\AtomicRedTeam\invoke-atomicredteam\Invoke-AtomicRedTeam.psd1",
    ]
    for p in fallbacks:
        if os.path.isfile(p):
            return p
    return root_module


def install_atomic_red_team(install_dir: str | None = None) -> bool:
    """Downloads and installs Invoke-AtomicRedTeam and atomics directly into the root folder of the code."""
    dest = install_dir or REPO_ROOT
    print(f"\n{'=' * 68}")
    print("      ATOMIC RED TEAM INSTALLER (Root Directory Deployment)")
    print(f"{'=' * 68}")
    print(f"[*] Target Destination: {dest}")
    print("[*] Running official Red Canary installer via PowerShell...\n")

    ps_script = f"""
    $ProgressPreference = 'SilentlyContinue'
    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
    try {{
        IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1' -UseBasicParsing)
        Install-AtomicRedTeam -InstallPath '{dest}' -getAtomics -Force
        exit 0
    }} catch {{
        Write-Error $_
        exit 1
    }}
    """
    try:
        proc = subprocess.run(
            ["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
            capture_output=True,
            text=True,
            check=False,
            timeout=600,
        )
        if proc.stdout:
            print(proc.stdout)
        if proc.stderr:
            print("[!] STDERR:", file=sys.stderr)
            print(proc.stderr, file=sys.stderr)

        expected_atomics = os.path.join(dest, "atomics")
        expected_module = os.path.join(dest, "invoke-atomicredteam", "Invoke-AtomicRedTeam.psd1")
        if os.path.isdir(expected_atomics) and os.path.isfile(expected_module):
            print(f"[+] SUCCESS: Atomic Red Team deployed to root folder:\n    {dest}\n")
            return True
        else:
            print(f"[-] Components missing after install in {dest}", file=sys.stderr)
            return False
    except subprocess.TimeoutExpired:
        print("\n[-] Installation timed out after 10 minutes.", file=sys.stderr)
        return False
    except Exception as e:
        print(f"\n[-] Installation error: {e}", file=sys.stderr)
        return False


def ensure_atomic_red_team(atomics_path: str, module_path: str) -> tuple[str, str]:
    """Ensures Atomic Red Team is present. If missing, automatically downloads it to the repository root."""
    if os.path.isdir(atomics_path) and os.path.isfile(module_path):
        return atomics_path, module_path

    print("\n" + "=" * 68)
    print("      ATOMIC RED TEAM NOT FOUND IN ROOT DIRECTORY")
    print("=" * 68)
    print("[*] First-time run detected: Atomic Red Team test library and engine")
    print(f"    are not yet installed in the project root:\n    {REPO_ROOT}")
    print("[*] Automatically initiating zero-config setup to fetch components...")
    print("=" * 68 + "\n")

    success = install_atomic_red_team(REPO_ROOT)
    if not success:
        print("[-] Automatic installation failed. Please check your internet connection or run:", file=sys.stderr)
        print("    powershell -ExecutionPolicy Bypass -Command \"IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1' -UseBasicParsing); Install-AtomicRedTeam -InstallPath . -getAtomics -Force\"\n", file=sys.stderr)
        sys.exit(1)

    new_atomics = os.path.join(REPO_ROOT, "atomics")
    new_module = os.path.join(REPO_ROOT, "invoke-atomicredteam", "Invoke-AtomicRedTeam.psd1")
    return new_atomics, new_module


def list_techniques(atomics_path: str) -> None:
    """Discovers and displays all available ATT&CK technique IDs in the atomics folder."""
    if not os.path.isdir(atomics_path):
        print(f"[-] Atomics path not found: {atomics_path}", file=sys.stderr)
        return
    pattern = re.compile(r"^T\d{4}(?:\.\d{3})?$")
    techniques = sorted(
        [
            d
            for d in os.listdir(atomics_path)
            if os.path.isdir(os.path.join(atomics_path, d)) and pattern.match(d)
        ]
    )
    print(f"\n[*] Discovered {len(techniques)} ATT&CK Techniques in {atomics_path}:\n")
    col_width = 16
    cols = 4
    for i in range(0, len(techniques), cols):
        row = techniques[i : i + cols]
        print("  " + "".join(f"{t:<{col_width}}" for t in row))
    print()


def show_matrix(atomics_path: str) -> None:
    """Displays the MITRE ATT&CK Enterprise Matrix breakdown for the installed atomics."""
    csv_path = os.path.join(atomics_path, "Indexes", "Indexes-CSV", "windows-index.csv")
    if not os.path.isfile(csv_path):
        csv_path = os.path.join(atomics_path, "Indexes", "Indexes-CSV", "index.csv")
    if not os.path.isfile(csv_path):
        print(f"[-] Matrix index file not found in {atomics_path}", file=sys.stderr)
        return

    tactics = {}
    with open(csv_path, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tac = row.get("Tactic", "").strip().lower()
            tech = row.get("Technique #", "").strip()
            if not tac:
                continue
            if tac not in tactics:
                tactics[tac] = {"techniques": set(), "tests": 0}
            tactics[tac]["techniques"].add(tech)
            tactics[tac]["tests"] += 1

    total_techniques = len(set.union(*[d["techniques"] for d in tactics.values()]))
    total_tests = sum(d["tests"] for d in tactics.values())

    print("\n" + "=" * 68)
    print("  MITRE ATT&CK (R) Enterprise Matrix Coverage (Atomic Red Team)")
    print("=" * 68)
    print(f"  {'TACTIC':<24} | {'TECHNIQUES':<12} | {'TESTS':<10}")
    print("  " + "-" * 64)

    tactic_display_order = [
        "initial-access",
        "execution",
        "persistence",
        "privilege-escalation",
        "stealth",
        "defense-impairment",
        "credential-access",
        "discovery",
        "lateral-movement",
        "collection",
        "command-and-control",
        "exfiltration",
        "impact",
    ]
    seen = set()
    for tac in tactic_display_order:
        if tac in tactics:
            seen.add(tac)
            data = tactics[tac]
            display_name = tac.replace("-", " ").title()
            print(f"  {display_name:<24} | {len(data['techniques']):>7d}      | {data['tests']:>6d}")

    for tac, data in tactics.items():
        if tac not in seen:
            display_name = tac.replace("-", " ").title()
            print(f"  {display_name:<24} | {len(data['techniques']):>7d}      | {data['tests']:>6d}")

    print("  " + "-" * 64)
    print(f"  {'TOTAL':<24} | {total_techniques:>7d}      | {total_tests:>6d}")
    print("=" * 68)

    nav_layer = os.path.join(
        atomics_path, "Indexes", "Attack-Navigator-Layers", "art-navigator-layer-windows.json"
    )
    if os.path.isfile(nav_layer):
        print(f"\n[+] Visual ATT&CK Navigator Layer available at:\n    {nav_layer}\n")


def get_techniques_by_tactic(atomics_path: str, tactic_name: str) -> list[str]:
    """Retrieves all technique IDs belonging to a specific MITRE ATT&CK tactic."""
    csv_path = os.path.join(atomics_path, "Indexes", "Indexes-CSV", "windows-index.csv")
    if not os.path.isfile(csv_path):
        csv_path = os.path.join(atomics_path, "Indexes", "Indexes-CSV", "index.csv")
    if not os.path.isfile(csv_path):
        return []

    normalized = tactic_name.strip().lower().replace(" ", "-")
    techniques = set()
    with open(csv_path, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tac = row.get("Tactic", "").strip().lower()
            if normalized in tac:
                techniques.add(row.get("Technique #", "").strip())
    return sorted(techniques)


def build_ps_command(
    technique_id: str,
    test_number: int | None,
    action: str,
    atomics_path: str,
    module_path: str,
    force: bool = False,
    report_path: str | None = None,
    timeout_seconds: int = 25,
    auto_cleanup: bool = True,
) -> str:
    """Constructs the PowerShell command to load the harness and trigger the test."""
    flag_map = {
        "check": "-CheckPrereqs",
        "get_prereqs": "-GetPrereqs",
        "execute": "",
        "cleanup": "-Cleanup",
        "show": "-ShowDetailsBrief",
    }
    action_flag = flag_map.get(action, "")
    test_num_flag = f"-TestNumbers {test_number}" if test_number else ""
    force_flag = "-Force" if force else ""
    report_flag = (
        f"-LoggingModule Default-ExecutionLogger -ExecutionLogPath '{report_path}'"
        if report_path
        else ""
    )

    should_auto_clean = auto_cleanup and (action == "execute")

    if should_auto_clean:
        ps_script = f"""
        $ProgressPreference = 'SilentlyContinue'
        Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
        Import-Module '{module_path}' -Force
        $PSDefaultParameterValues['Invoke-AtomicTest:PathToAtomicsFolder'] = '{atomics_path}'
        try {{
            Invoke-AtomicTest {technique_id} -PathToAtomicsFolder '{atomics_path}' {test_num_flag} {action_flag} {force_flag} {report_flag} -TimeoutSeconds {timeout_seconds}
        }} finally {{
            Write-Host "`n[*] Auto-cleaning up test artifacts for {technique_id}..."
            Invoke-AtomicTest {technique_id} -PathToAtomicsFolder '{atomics_path}' {test_num_flag} -Cleanup -Force -TimeoutSeconds {timeout_seconds} -ErrorAction SilentlyContinue
            Write-Host "[+] Cleanup completed for {technique_id}`n"
        }}
        """
    else:
        ps_script = f"""
        $ProgressPreference = 'SilentlyContinue'
        Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
        Import-Module '{module_path}' -Force
        $PSDefaultParameterValues['Invoke-AtomicTest:PathToAtomicsFolder'] = '{atomics_path}'
        Invoke-AtomicTest {technique_id} -PathToAtomicsFolder '{atomics_path}' {test_num_flag} {action_flag} {force_flag} {report_flag} -TimeoutSeconds {timeout_seconds}
        """
    return ps_script.strip()


def check_edr_block(output: str, error: str, exit_code: int) -> bool:
    """Detects whether command output or exit code indicates an EDR, AV, or OS security policy block."""
    combined = (output + " " + error).lower()
    block_signatures = [
        "access is denied",
        "file contains a virus",
        "potentially unwanted software",
        "blocked by group policy",
        "blocked by your administrator",
        "blocked by app control",
        "prevented by app control",
        "windows defender has blocked",
        "operation was blocked",
        "a required privilege is not held",
        "unauthorizedaccess",
    ]
    if any(sig in combined for sig in block_signatures):
        return True
    # Standard Windows error codes for security/AV termination
    if exit_code in [225, 5, 1260, -1073741819, 3221225477]:
        return True
    return False


def run_local(
    command: str,
    timeout: int | None = None,
    technique_id: str | None = None,
    test_number: int | None = None,
    atomics_path: str = DEFAULT_ATOMICS_PATH,
    module_path: str = DEFAULT_INVOKE_PATH,
    auto_cleanup: bool = True,
) -> int:
    """Executes the test harness on the local machine via PowerShell with EDR resilience."""
    print("[*] Target: Local execution via PowerShell...\n")
    try:
        proc = subprocess.run(
            ["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", command],
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout,
        )
        stdout_text = proc.stdout or ""
        stderr_text = proc.stderr or ""

        if stdout_text:
            print(stdout_text)
        if stderr_text:
            print("[!] STDERR:", file=sys.stderr)
            print(stderr_text, file=sys.stderr)

        if check_edr_block(stdout_text, stderr_text, proc.returncode):
            print("\n[*** EDR / DEFENDER INTERVENTION DETECTED ***]")
            print("[+] Action was BLOCKED or DENIED by security controls.")
            print("[+] Result: DEFENSE SUCCESS (Continuing automatically to next test...)\n")
            return 5 if proc.returncode == 0 else proc.returncode
        else:
            print(f"\n[+] Local execution completed (Exit Code: {proc.returncode})")
        return proc.returncode
    except subprocess.TimeoutExpired:
        print(f"\n[-] Subprocess safety timeout expired ({timeout}s). Test process terminated.", file=sys.stderr)
        if auto_cleanup and technique_id:
            print(f"[*] Running emergency post-timeout cleanup for {technique_id}...")
            test_num_flag = f"-TestNumbers {test_number}" if test_number else ""
            clean_cmd = (
                f"$ProgressPreference = 'SilentlyContinue'; "
                f"Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; "
                f"Import-Module '{module_path}' -Force; "
                f"Invoke-AtomicTest {technique_id} -PathToAtomicsFolder '{atomics_path}' {test_num_flag} -Cleanup -Force -TimeoutSeconds 15 -ErrorAction SilentlyContinue"
            )
            try:
                subprocess.run(
                    ["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", clean_cmd],
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=20,
                )
                print(f"[+] Emergency cleanup finished for {technique_id}.")
            except Exception:
                pass
        print("[+] Moving to next test...", file=sys.stderr)
        return 124
    except Exception as e:
        print(f"[-] Execution error: {e}", file=sys.stderr)
        return 1


def run_remote(
    command: str, host: str, user: str, password: str, port: int = 5985
) -> int:
    """Executes the test harness on a remote Windows host via WinRM with EDR resilience."""
    print(f"[*] Target: Remote host {host}:{port} via WinRM...\n")
    try:
        session = winrm.Session(
            f"http://{host}:{port}/wsman",
            auth=(user, password),
            transport="ntlm",
            server_cert_validation="ignore",
        )
        response = session.run_ps(command)
        stdout_text = response.std_out.decode("utf-8", errors="replace") if response.std_out else ""
        stderr_text = response.std_err.decode("utf-8", errors="replace") if response.std_err else ""

        if stdout_text:
            print(stdout_text)
        if stderr_text:
            print("[!] REMOTE STDERR:", file=sys.stderr)
            print(stderr_text, file=sys.stderr)

        if check_edr_block(stdout_text, stderr_text, response.status_code):
            print("\n[*** REMOTE EDR / DEFENDER INTERVENTION DETECTED ***]")
            print("[+] Remote action was BLOCKED or DENIED by security controls.")
            print("[+] Result: DEFENSE SUCCESS (Continuing automatically to next test...)\n")
            return 5 if response.status_code == 0 else response.status_code
        else:
            print(f"\n[+] Remote execution completed (Exit Code: {response.status_code})")
        return response.status_code
    except Exception as e:
        print(f"[-] WinRM execution error: {e}", file=sys.stderr)
        print("[+] Moving to next test...", file=sys.stderr)
        return 1


def main():
    parser = argparse.ArgumentParser(
        description="EDR Telemetry & Atomic Testing Runner (MITRE ATT&CK Matrix Harness)"
    )

    # MITRE ATT&CK Matrix & Technique selection
    parser.add_argument(
        "-t",
        "--technique",
        nargs="+",
        default=None,
        help="One or more ATT&CK Technique IDs (e.g. -t T1082 T1033, or -t T1082,T1033)",
    )
    parser.add_argument(
        "--matrix",
        "--tactics",
        action="store_true",
        help="Display the full MITRE ATT&CK Enterprise Matrix breakdown and test counts",
    )
    parser.add_argument(
        "--tactic",
        help="Filter and target all techniques within a specific tactic (e.g. discovery, execution, persistence, credential-access)",
    )
    parser.add_argument(
        "--group",
        help="Target all techniques used by a specific threat group via MITRE CTI (e.g. APT29, Lazarus Group, FIN7, G0082)",
    )
    parser.add_argument(
        "--info",
        help="Query official MITRE ATT&CK CTI intel, description, detection components, and threat actors for a technique",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run every test across all techniques (or all tests for specified techniques if -t is provided)",
    )
    parser.add_argument(
        "--list-techniques",
        "--list-t",
        action="store_true",
        help="Enumerate and list all available technique IDs (-t) in the atomics directory",
    )
    parser.add_argument(
        "-n",
        "--test-number",
        type=int,
        default=None,
        help="Atomic test index (optional)",
    )
    parser.add_argument(
        "-a",
        "--action",
        choices=["show", "check", "get_prereqs", "execute", "cleanup"],
        default="execute",
        help="Action to perform (default: execute)",
    )

    # Path overrides
    parser.add_argument(
        "--atomics-path",
        default=DEFAULT_ATOMICS_PATH,
        help="Path to atomics folder",
    )
    parser.add_argument(
        "--module-path",
        default=DEFAULT_INVOKE_PATH,
        help="Path to Invoke-AtomicRedTeam.psd1",
    )

    # Target selection
    parser.add_argument(
        "--local",
        action="store_true",
        help="Run against the local machine (default if --remote is not specified)",
    )
    parser.add_argument(
        "--remote",
        action="store_true",
        help="Run against a remote endpoint via WinRM",
    )
    parser.add_argument("--host", help="Remote hostname or IP address")
    parser.add_argument(
        "--user", help="Remote administrator username (DOMAIN\\User or User)"
    )
    parser.add_argument("--password", help="Remote password")
    parser.add_argument(
        "--port", type=int, default=5985, help="WinRM port (default: 5985)"
    )

    # Execution controls & reporting
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force execution without confirmation prompts (always enabled when --all is used)",
    )
    parser.add_argument(
        "--report",
        help="Path to output execution CSV report (uses Default-ExecutionLogger)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=25,
        help="Maximum timeout in seconds for any single atomic test before terminating it (default: 25s)",
    )
    parser.add_argument(
        "--include-reboot",
        action="store_true",
        help="Include T1529 (System Shutdown/Reboot) during batch runs (excluded by default for safety)",
    )
    parser.add_argument(
        "--no-cleanup",
        action="store_true",
        help="Disable automatic post-test artifact cleanup (cleanup runs automatically by default)",
    )
    parser.add_argument(
        "--get-atomics",
        "--install-atomics",
        action="store_true",
        help="Download and install Atomic Red Team and Invoke-AtomicRedTeam directly into the project root folder",
    )

    args = parser.parse_args()

    # Manual or explicit installer trigger
    if getattr(args, "get_atomics", False):
        install_dir = args.atomics_path if args.atomics_path != DEFAULT_ATOMICS_PATH else REPO_ROOT
        success = install_atomic_red_team(install_dir)
        sys.exit(0 if success else 1)

    # Query technique CTI info via mitreattack-python (only requires STIX data)
    if args.info:
        try:
            import mitre_helper
            mitre_helper.show_technique_info(args.info)
        except Exception as e:
            print(f"[-] CTI Lookup Error: {e}", file=sys.stderr)
        return

    # Resolve paths (prioritizing root folder) and automatically download into root if missing
    atomics_path = get_atomics_path(args.atomics_path)
    module_path = get_module_path(args.module_path)
    atomics_path, module_path = ensure_atomic_red_team(atomics_path, module_path)

    # Display MITRE ATT&CK matrix if requested
    if args.matrix:
        show_matrix(atomics_path)
        return

    # Handle fast technique enumeration
    if args.list_techniques:
        list_techniques(atomics_path)
        return

    # Parse techniques from -t
    techniques = []
    if args.technique:
        for item in args.technique:
            for tech in item.split(","):
                tech = tech.strip()
                if tech and tech not in techniques:
                    techniques.append(tech)

    # If --tactic is specified, retrieve techniques for that tactic
    if args.tactic:
        tactic_techs = get_techniques_by_tactic(atomics_path, args.tactic)
        if not tactic_techs:
            print(f"[-] No techniques found for tactic '{args.tactic}'", file=sys.stderr)
            sys.exit(1)
        print(f"[*] Tactic '{args.tactic}' resolved to {len(tactic_techs)} techniques.")
        for tech in tactic_techs:
            if tech not in techniques:
                techniques.append(tech)

    # If --group is specified, resolve threat actor techniques via mitreattack-python
    if args.group:
        try:
            import mitre_helper
            group_techs = mitre_helper.get_techniques_for_group(args.group)
            if not group_techs:
                sys.exit(1)

            # Cross-reference with available techniques in local atomics directory
            pattern = re.compile(r"^T\d{4}(?:\.\d{3})?$")
            local_techs = set(
                d for d in os.listdir(atomics_path)
                if os.path.isdir(os.path.join(atomics_path, d)) and pattern.match(d)
            ) if os.path.isdir(atomics_path) else set()

            matched_techs = [t for t in group_techs if t in local_techs]
            print(f"[*] {len(matched_techs)} of {len(group_techs)} {args.group} techniques exist in your local Atomic library.")
            for tech in matched_techs:
                if tech not in techniques:
                    techniques.append(tech)
        except Exception as e:
            print(f"[-] Threat Group Resolution Error: {e}", file=sys.stderr)
            sys.exit(1)

    # Validate technique vs all
    if not techniques and not args.all:
        parser.error(
            "Specify either -t/--technique, --tactic, --group, --info, --all, --matrix, or --list-techniques."
        )

    if args.all:
        if args.test_number is not None:
            print(
                "[!] Notice: --test-number is ignored when --all is specified.",
                file=sys.stderr,
            )
        test_number = None
        force = True
        if not techniques:
            # Enumerate all available techniques individually so each gets isolated progress & timeouts
            pattern = re.compile(r"^T\d{4}(?:\.\d{3})?$")
            if os.path.isdir(atomics_path):
                discovered = [
                    d
                    for d in os.listdir(atomics_path)
                    if os.path.isdir(os.path.join(atomics_path, d))
                    and pattern.match(d)
                ]
                techniques = sorted(discovered)
            else:
                techniques = ["All"]

    else:
        test_number = args.test_number
        force = args.force

    # Safety protection: Exclude T1529 (System Shutdown/Reboot) during batch runs unless explicitly requested
    if len(techniques) > 1 and "T1529" in techniques and not args.include_reboot:
        techniques.remove("T1529")
        print(
            "[*] Safety Guard: Excluded T1529 (System Shutdown/Reboot) to prevent machine restart. (Use --include-reboot to override)\n"
        )

    # Target determination:
    # If remote credentials are provided and neither --local nor --remote was explicitly set, run on both!
    if args.host and args.user and args.password and not args.local and not args.remote:
        run_on_local = True
        run_on_remote = True
    else:
        run_on_local = args.local or (not args.remote)
        run_on_remote = args.remote

    if run_on_remote:
        if not all([args.host, args.user, args.password]):
            parser.error(
                "--host, --user, and --password are required when using --remote"
            )

    auto_cleanup = not args.no_cleanup
    if auto_cleanup and args.action == "execute":
        print("[*] Test Lifecycle: Automatic post-test artifact cleanup is ENABLED (default).")

    total_techs = len(techniques)
    overall_exit_codes = []
    passed_count = 0
    blocked_count = 0
    timeout_count = 0

    try:
        for index, tech_id in enumerate(techniques, 1):
            if total_techs > 1:
                print(f"\n{'=' * 60}")
                print(f"[*] Processing Technique ({index}/{total_techs}): {tech_id}")
                print(f"{'=' * 60}\n")

            try:
                cmd = build_ps_command(
                    technique_id=tech_id,
                    test_number=test_number,
                    action=args.action,
                    atomics_path=atomics_path,
                    module_path=module_path,
                    force=force,
                    report_path=args.report,
                    timeout_seconds=args.timeout,
                    auto_cleanup=auto_cleanup,
                )

                tech_exit_code = 0
                if run_on_local:
                    code = run_local(
                        cmd,
                        timeout=(args.timeout * 2) + 15,
                        technique_id=tech_id,
                        test_number=test_number,
                        atomics_path=atomics_path,
                        module_path=module_path,
                        auto_cleanup=auto_cleanup,
                    )
                    tech_exit_code = code
                    overall_exit_codes.append(code)

                if run_on_remote:
                    code = run_remote(cmd, args.host, args.user, args.password, args.port)
                    tech_exit_code = code
                    overall_exit_codes.append(code)

                if tech_exit_code == 0:
                    passed_count += 1
                elif tech_exit_code == 124 or tech_exit_code == -1:
                    timeout_count += 1
                else:
                    blocked_count += 1

            except Exception as tech_err:
                print(f"[-] Technique {tech_id} error: {tech_err}", file=sys.stderr)
                print("[*] EDR Resilience: Continuing to next test item...\n", file=sys.stderr)
                blocked_count += 1
                continue

    except KeyboardInterrupt:
        print("\n\n[!] Test run paused by user (Ctrl+C). Generating summary of completed tests...")

    # Final Execution & Detection Summary
    total_processed = passed_count + blocked_count + timeout_count
    if total_processed > 0:
        print("\n" + "=" * 62)
        print("                 EDR VALIDATION SUMMARY")
        print("=" * 62)
        print(f"  Total Techniques Processed  : {total_processed} / {total_techs}")
        print(f"  Executed Cleanly (Unblocked): {passed_count}")
        print(f"  Blocked / Denied by EDR     : {blocked_count}")
        print(f"  Timed Out (Safety killed)   : {timeout_count}")
        print("=" * 62 + "\n")


if __name__ == "__main__":
    main()
