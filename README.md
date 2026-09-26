# Edrtest

A Python-native automation harness and resilience port for [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam) and [mitreattack-python](https://github.com/mitre-attack/mitreattack-python). Designed for security operations (SecOps), detection engineers, and purple teams to validate Endpoint Detection and Response (EDR) sensors, behavioral telemetry, and SIEM alerting pipelines against the **MITRE ATT&CK® Enterprise Matrix**.

---

> [!CAUTION]
> **LEGAL & OPERATIONAL WARNING / DISCLAIMER**
> 
> - **Defensive Testing Only:** This tool generates real adversarial activity patterns (such as credential dumping commands, service installation, process injection simulations, and registry modifications) designed to test endpoint security software.
> - **Authorization Required:** Only execute this software against systems and networks that you own or have explicit, formal, written permission to test. Unauthorized execution may violate federal, state, and international cybercrime legislation (e.g., Computer Fraud and Abuse Act - 18 U.S.C. § 1030).
> - **Production Safety:** Do not execute batch testing (`--all` or broad tactics) in production environments without appropriate change-control and SOC notification. Although disruptive actions like system reboots (`T1529`) are bypassed by default, tests can generate heavy security event volume or trigger host isolation.

---

## Port Attribution & Architecture

This repository is an automation and orchestration **port** built on top of:
- **[Atomic Red Team™](https://github.com/redcanaryco/atomic-red-team)** by Red Canary — library of simple, open-source tests mapped to the MITRE ATT&CK® framework.
- **[Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)** by Red Canary — PowerShell execution framework for Atomic tests.
- **[mitreattack-python](https://github.com/mitre-attack/mitreattack-python)** by MITRE — official Python library for navigating and querying ATT&CK STIX 2.0 CTI datasets.

### Enhancements Provided by this Port:
1. **EDR Intervention Resilience (`check_edr_block`):**
   - Automatically monitors standard output, standard error, and exit codes for security controls (`Access is denied`, virus signature detections, AppLocker/WDAC blocks, AV process termination).
   - When an EDR blocks an action, the harness records the defense success and **continues execution without halting or freezing**.
2. **Automatic Post-Test Artifact Cleanup (Default):**
   - Wraps every test in a PowerShell `try ... finally` block that runs `Invoke-AtomicTest -Cleanup -Force` immediately after execution to wipe dropped files, temporary registry entries, and scheduled tasks.
   - An emergency timeout cleanup is triggered if a process hangs and gets terminated.
   - Opt-out available via `--no-cleanup`.
3. **Dual Execution Engine (Local & Remote WinRM):**
   - Seamlessly targets either the local host via PowerShell or remote endpoints across the network via WinRM (`pywinrm`) with NTLM authentication.
4. **Threat Actor Emulation (`--group`):**
   - Integrates live MITRE Enterprise STIX 2.0 CTI to query techniques used by specific threat actors (e.g., `APT29`, `FIN7`, `Lazarus Group`, `G0082`) and execute tests matching their known profile.
5. **Safety Guards:**
   - Excludes reboot techniques (`T1529`) by default in batch runs.
   - Enforces configurable subprocess timeouts (`--timeout`, default 25s) to prevent headless GUI popups (e.g., `mstsc.exe`, `wmic`) from stalling test runs.

---

## Prerequisites

1. **Python 3.10+** (Python 3.14+ supported).
2. **Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Installs `pywinrm` and `mitreattack-python`)*
3. **PowerShell Execution Policy:**
   Ensure PowerShell allows script execution:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
4. **Invoke-AtomicRedTeam & Atomics Directory:**
   By default, the script looks for:
   - Module: `D:\tools\redteam\invoke-atomicredteam\Invoke-AtomicRedTeam.psd1`
   - Atomics folder: `D:\tools\redteam\atomics`
   *(Override via `--module-path` and `--atomics-path` if installed elsewhere).*
5. **Remote Host Requirements (for WinRM testing):**
   - Enable WinRM on target endpoint: `Enable-PSRemoting -Force`
   - Default port: `5985` (HTTP) or `5986` (HTTPS).

---

## Usage

```text
usage: edr_tester.py [-h] [-t TECHNIQUE [TECHNIQUE ...]] [--matrix]
                     [--tactic TACTIC] [--group GROUP] [--info INFO]
                     [--all] [--list-techniques] [-n TEST_NUMBER]
                     [-a {show,check,get_prereqs,execute,cleanup}]
                     [--atomics-path ATOMICS_PATH] [--module-path MODULE_PATH]
                     [--local] [--remote] [--host HOST] [--user USER]
                     [--password PASSWORD] [--port PORT] [--force]
                     [--report REPORT] [--timeout TIMEOUT] [--include-reboot]
                     [--no-cleanup]
```

### CLI Arguments

| Flag | Description |
| :--- | :--- |
| `--all` | **Master Run.** Executes every test across all 340+ techniques in sequence with isolated timeouts and progress tracking. |
| `--no-cleanup` | Disable automatic post-test artifact cleanup (**cleanup is enabled by default** after each test). |
| `--timeout <sec>` | Maximum timeout in seconds per test before terminating it (default: `25s`). |
| `--include-reboot` | Include `T1529` (System Shutdown/Reboot) during batch runs (excluded by default for safety). |
| `--group <name>` | Emulate a threat actor by name, alias, or ID (e.g. `APT29`, `APT38`, `G0082`). Automatically pulls their techniques via MITRE CTI. |
| `--info <T_ID>` | Query official MITRE ATT&CK CTI intel, description, detection components, and threat actors for a technique. |
| `--matrix`, `--tactics` | Displays the full MITRE ATT&CK Enterprise Matrix breakdown and test counts. |
| `--tactic <name>` | Filters and runs all techniques belonging to a specific tactic (e.g. `credential-access`, `discovery`, `execution`). |
| `-t`, `--technique` | One or more ATT&CK Technique IDs (comma-separated `T1082,T1033` or space-separated `T1082 T1033`). |
| `--list-techniques` | Fast enumeration of all available technique IDs in the atomics directory. |
| `-n`, `--test-number` | Atomic test index (1-based integer, optional). Ignored when `--all` is used. |
| `-a`, `--action` | Action to perform: `show`, `check`, `get_prereqs`, `execute`, `cleanup` (default: `execute`). |
| `--local` | Target local machine via PowerShell (default if `--remote` is omitted). |
| `--remote` | Target remote endpoint via WinRM. |
| `--host` | Remote hostname or IP address (required with `--remote`). |
| `--user` | Remote administrator username (`DOMAIN\User` or `User`, required with `--remote`). |
| `--password` | Remote password (required with `--remote`). |
| `--port` | WinRM port (default: `5985`). |
| `--force` | Force execution without confirmation prompts (automatically set with `--all`). |
| `--report` | Path to save CSV execution report via `Default-ExecutionLogger`. |

---

## Examples

### 1. Run Everything with Auto-Cleanup and EDR Resilience
```bash
python edr_tester.py --all
```

### 2. Emulate a Specific Threat Actor (e.g., APT29)
Pulls all 119 techniques attributed to APT29, checks which are available locally, and tests them with automatic cleanup and block continuation:
```bash
python edr_tester.py --group "APT29" --local -a execute --timeout 20
```

### 3. Test a Single Technique with Specific Test Number
```bash
python edr_tester.py -t T1003.002 -n 1 --local -a execute
```

### 4. Target a Remote Windows Host via WinRM
```bash
python edr_tester.py -t T1082 --remote \
  --host 10.0.0.165 \
  --user "Administrator" \
  --password "TargetPassword"
```

### 5. Inspect Official MITRE Threat Intel for a Technique
```bash
python edr_tester.py --info T1059.001
```

### 6. Display the Installed MITRE ATT&CK Matrix Coverage
```bash
python edr_tester.py --matrix
```

---

## Validation Summary Output

At the end of every run (or if paused with `Ctrl+C`), a summary report is rendered:

```text
==============================================================
                 EDR VALIDATION SUMMARY
==============================================================
  Total Techniques Processed  : 79 / 79
  Executed Cleanly (Unblocked): 58
  Blocked / Denied by EDR     : 18
  Timed Out (Safety killed)   : 3
==============================================================
```

---

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
Atomic Red Team is a registered trademark of Red Canary. MITRE ATT&CK is a registered trademark of The MITRE Corporation.
