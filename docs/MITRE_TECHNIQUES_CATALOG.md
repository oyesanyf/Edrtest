# Complete MITRE ATT&CK® Techniques & Tests Catalog

This document lists all **266 MITRE ATT&CK Techniques** and **1,587 Atomic Tests** executable via edr_tester.py.

## Tactic Summary

| Tactic | Techniques | Tests |
| :--- | :--- | :--- |
| **Collection** | 16 | 33 |
| **Command And Control** | 14 | 68 |
| **Credential Access** | 33 | 136 |
| **Defense Impairment** | 19 | 201 |
| **Discovery** | 34 | 227 |
| **Execution** | 25 | 127 |
| **Exfiltration** | 9 | 16 |
| **Impact** | 8 | 37 |
| **Initial Access** | 8 | 13 |
| **Lateral Movement** | 10 | 25 |
| **Persistence** | 50 | 254 |
| **Privilege Escalation** | 46 | 193 |
| **Stealth** | 70 | 257 |
| **Total Coverage** | **266** | **1587** |

---

## Collection

### T1005: Data from Local System (1 Tests)
- **Test 1** [powershell]: Search files of interest and save them to a single zip file (Windows)

### T1025: Data from Removable Media (1 Tests)
- **Test 1** [command_prompt]: Identify Documents on USB and Removable Media via PowerShell

### T1039: Data from Network Shared Drive (2 Tests)
- **Test 1** [command_prompt]: Copy a sensitive File over Administrative share with copy
- **Test 2** [powershell]: Copy a sensitive File over Administrative share with Powershell

### T1056.001: Input Capture: Keylogging (1 Tests)
- **Test 1** [powershell]: Input Capture

### T1056.002: Input Capture: GUI Input Capture (1 Tests)
- **Test 2** [powershell]: PowerShell - Prompt User for Password

### T1056.004: Input Capture: Credential API Hooking (1 Tests)
- **Test 1** [powershell]: Hook PowerShell TLS Encrypt/Decrypt Messages

### T1074.001: Data Staged: Local Data Staging (2 Tests)
- **Test 1** [powershell]: Stage data from Discovery.bat
- **Test 3** [powershell]: Zip a Folder with PowerShell for Staging in Temp

### T1113: Screen Capture (4 Tests)
- **Test 7** [powershell]: Windows Screencapture
- **Test 8** [powershell]: Windows Screen Capture (CopyFromScreen)
- **Test 9** [powershell]: Windows Recall Feature Enabled - DisableAIDataAnalysis Value Deleted
- **Test 10** [powershell]: RDP Bitmap Cache Extraction via bmc-tools

### T1114.001: Email Collection: Local Email Collection (1 Tests)
- **Test 1** [powershell]: Email Collection with PowerShell Get-Inbox

### T1115: Clipboard Data (3 Tests)
- **Test 1** [command_prompt]: Utilize Clipboard to store or execute commands from
- **Test 2** [powershell]: Execute Commands from Clipboard using PowerShell
- **Test 4** [powershell]: Collect Clipboard Data via VBA

### T1119: Automated Collection (4 Tests)
- **Test 1** [command_prompt]: Automated Collection Command Prompt
- **Test 2** [powershell]: Automated Collection PowerShell
- **Test 3** [powershell]: Recon information for export with PowerShell
- **Test 4** [command_prompt]: Recon information for export with Command Prompt

### T1123: Audio Capture (2 Tests)
- **Test 1** [powershell]: using device audio capture commandlet
- **Test 2** [command_prompt]: Registry artefact when application use microphone

### T1125: Video Capture (1 Tests)
- **Test 1** [command_prompt]: Registry artefact when application use webcam

### T1557.001: Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay (1 Tests)
- **Test 1** [powershell]: LLMNR Poisoning with Inveigh (PowerShell)

### T1560: Archive Collected Data (1 Tests)
- **Test 1** [powershell]: Compress Data for Exfiltration With PowerShell

### T1560.001: Archive Collected Data: Archive via Utility (7 Tests)
- **Test 1** [command_prompt]: Compress Data for Exfiltration With Rar
- **Test 2** [command_prompt]: Compress Data and lock with password for Exfiltration with winrar
- **Test 3** [command_prompt]: Compress Data and lock with password for Exfiltration with winzip
- **Test 4** [command_prompt]: Compress Data and lock with password for Exfiltration with 7zip
- **Test 10** [powershell]: ESXi - Remove Syslog remote IP
- **Test 11** [command_prompt]: Compress a File for Exfiltration using Makecab
- **Test 12** [powershell]: Copy and Compress AppData Folder

## Command And Control

### T1001.002: Data Obfuscation via Steganography (2 Tests)
- **Test 1** [powershell]: Steganographic Tarball Embedding
- **Test 2** [powershell]: Embedded Script in Image Execution via Extract-Invoke-PSImage

### T1071: Application Layer Protocol (1 Tests)
- **Test 1** [powershell]: Telnet C2

### T1071.001: Application Layer Protocol: Web Protocols (2 Tests)
- **Test 1** [powershell]: Malicious User Agents - Powershell
- **Test 2** [command_prompt]: Malicious User Agents - CMD

### T1071.004: Application Layer Protocol: DNS (4 Tests)
- **Test 1** [powershell]: DNS Large Query Volume
- **Test 2** [powershell]: DNS Regular Beaconing
- **Test 3** [powershell]: DNS Long Domain Query
- **Test 4** [powershell]: DNS C2

### T1090.001: Proxy: Internal Proxy (1 Tests)
- **Test 3** [powershell]: portproxy reg key

### T1090.003: Proxy: Multi-hop Proxy (2 Tests)
- **Test 1** [powershell]: Psiphon
- **Test 2** [powershell]: Tor Proxy Usage - Windows

### T1095: Non-Application Layer Protocol (4 Tests)
- **Test 1** [powershell]: ICMP C2
- **Test 2** [powershell]: Netcat C2
- **Test 3** [powershell]: Powercat C2
- **Test 5** [powershell]: Turla Topinambour TCP Callback via Inline .NET

### T1105: Ingress Tool Transfer (29 Tests)
- **Test 7** [command_prompt]: certutil download (urlcache)
- **Test 8** [powershell]: certutil download (verifyctl)
- **Test 9** [command_prompt]: Windows - BITSAdmin BITS Download
- **Test 10** [powershell]: Windows - PowerShell Download
- **Test 11** [command_prompt]: OSTAP Worming Activity
- **Test 12** [command_prompt]: svchost writing a file to a UNC path
- **Test 13** [command_prompt]: Download a File with Windows Defender MpCmdRun.exe
- **Test 15** [powershell]: File Download via PowerShell
- **Test 16** [command_prompt]: File download with finger.exe on Windows
- **Test 17** [powershell]: Download a file with IMEWDBLD.exe
- **Test 18** [command_prompt]: Curl Download File
- **Test 19** [command_prompt]: Curl Upload File
- **Test 20** [command_prompt]: Download a file with Microsoft Connection Manager Auto-Download
- **Test 21** [powershell]: MAZE Propagation Script
- **Test 22** [command_prompt]: Printer Migration Command-Line Tool UNC share folder into a zip file
- **Test 23** [command_prompt]: Lolbas replace.exe use to copy file
- **Test 24** [command_prompt]: Lolbas replace.exe use to copy UNC file
- **Test 25** [command_prompt]: certreq download
- **Test 26** [command_prompt]: Download a file using wscript
- **Test 28** [command_prompt]: Nimgrab - Transfer Files
- **Test 29** [command_prompt]: iwr or Invoke Web-Request download
- **Test 30** [command_prompt]: Arbitrary file download using the Notepad++ GUP.exe binary
- **Test 32** [powershell]: File Download with Sqlcmd.exe
- **Test 33** [command_prompt]: Remote File Copy using PSCP
- **Test 34** [powershell]: Windows push file using scp.exe
- **Test 35** [powershell]: Windows pull file using scp.exe
- **Test 36** [powershell]: Windows push file using sftp.exe
- **Test 37** [powershell]: Windows pull file using sftp.exe
- **Test 38** [powershell]: Download a file with OneDrive Standalone Updater

### T1132.001: Data Encoding: Standard Encoding (1 Tests)
- **Test 3** [powershell]: XOR Encoded data.

### T1219: Remote Access Software (15 Tests)
- **Test 1** [powershell]: TeamViewer Files Detected Test on Windows
- **Test 2** [powershell]: AnyDesk Files Detected Test on Windows
- **Test 3** [powershell]: LogMeIn Files Detected Test on Windows
- **Test 4** [powershell]: GoToAssist Files Detected Test on Windows
- **Test 5** [powershell]: ScreenConnect Application Download and Install on Windows
- **Test 6** [powershell]: Ammyy Admin Software Execution
- **Test 7** [powershell]: RemotePC Software Execution
- **Test 8** [powershell]: NetSupport - RAT Execution
- **Test 9** [powershell]: UltraViewer - RAT Execution
- **Test 10** [powershell]: UltraVNC Execution
- **Test 11** [powershell]: MSP360 Connect Execution
- **Test 12** [powershell]: RustDesk Files Detected Test on Windows
- **Test 13** [powershell]: Splashtop Execution
- **Test 14** [powershell]: Splashtop Streamer Execution
- **Test 15** [powershell]: Microsoft App Quick Assist Execution

### T1571: Non-Standard Port (1 Tests)
- **Test 1** [powershell]: Testing usage of uncommonly used port with PowerShell

### T1572: Protocol Tunneling (4 Tests)
- **Test 1** [powershell]: DNS over HTTPS Large Query Volume
- **Test 2** [powershell]: DNS over HTTPS Regular Beaconing
- **Test 3** [powershell]: DNS over HTTPS Long Domain Query
- **Test 4** [powershell]: run ngrok

### T1573: Encrypted Channel (1 Tests)
- **Test 1** [powershell]: OpenSSL C2

### T1659: Content Injection (1 Tests)
- **Test 2** [powershell]: MITM Proxy Injection (Windows)

## Credential Access

### T1003: OS Credential Dumping (7 Tests)
- **Test 1** [command_prompt]: Gsecdump
- **Test 2** [powershell]: Credential Dumping with NPPSpy
- **Test 3** [powershell]: Dump svchost.exe to gather RDP credentials
- **Test 4** [powershell]: Retrieve Microsoft IIS Service Account Credentials Using AppCmd (using list)
- **Test 5** [powershell]: Retrieve Microsoft IIS Service Account Credentials Using AppCmd (using config)
- **Test 6** [powershell]: Dump Credential Manager using keymgr.dll and rundll32.exe
- **Test 7** [powershell]: Send NTLM Hash with RPC Test Connection

### T1003.001: OS Credential Dumping: LSASS Memory (14 Tests)
- **Test 1** [command_prompt]: Dump LSASS.exe Memory using ProcDump
- **Test 2** [powershell]: Dump LSASS.exe Memory using comsvcs.dll
- **Test 3** [command_prompt]: Dump LSASS.exe Memory using direct system calls and API unhooking
- **Test 4** [command_prompt]: Dump LSASS.exe Memory using NanoDump
- **Test 5** [manual]: Dump LSASS.exe Memory using Windows Task Manager
- **Test 6** [command_prompt]: Offline Credential Theft With Mimikatz
- **Test 7** [command_prompt]: LSASS read with pypykatz
- **Test 8** [powershell]: Dump LSASS.exe Memory using Out-Minidump.ps1
- **Test 9** [command_prompt]: Create Mini Dump of LSASS.exe using ProcDump
- **Test 10** [powershell]: Powershell Mimikatz
- **Test 11** [powershell]: Dump LSASS with createdump.exe from .Net v5
- **Test 12** [powershell]: Dump LSASS.exe using imported Microsoft DLLs
- **Test 13** [powershell]: Dump LSASS.exe using lolbin rdrleakdiag.exe
- **Test 14** [command_prompt]: Dump LSASS.exe Memory through Silent Process Exit

### T1003.002: OS Credential Dumping: Security Account Manager (8 Tests)
- **Test 1** [command_prompt]: Registry dump of SAM, creds, and secrets
- **Test 2** [command_prompt]: Registry parse with pypykatz
- **Test 3** [command_prompt]: esentutl.exe SAM copy
- **Test 4** [powershell]: PowerDump Hashes and Usernames from Registry
- **Test 5** [command_prompt]: dump volume shadow copy hives with certutil
- **Test 6** [powershell]: dump volume shadow copy hives with System.IO.File
- **Test 7** [powershell]: WinPwn - Loot local Credentials - Dump SAM-File for NTLM Hashes
- **Test 8** [command_prompt]: Dumping of SAM, creds, and secrets(Reg Export)

### T1003.003: OS Credential Dumping: NTDS (11 Tests)
- **Test 1** [command_prompt]: Create Volume Shadow Copy with vssadmin
- **Test 2** [command_prompt]: Copy NTDS.dit from Volume Shadow Copy
- **Test 3** [command_prompt]: Dump Active Directory Database with NTDSUtil
- **Test 4** [command_prompt]: Create Volume Shadow Copy with WMI
- **Test 5** [command_prompt]: Create Volume Shadow Copy remotely with WMI
- **Test 6** [command_prompt]: Create Volume Shadow Copy remotely (WMI) with esentutl
- **Test 7** [powershell]: Create Volume Shadow Copy with Powershell
- **Test 8** [command_prompt]: Create Symlink to Volume Shadow Copy
- **Test 9** [command_prompt]: Create Volume Shadow Copy with diskshadow
- **Test 10** [powershell]: Copy NTDS in low level NTFS acquisition via MFT parsing
- **Test 11** [powershell]: Copy NTDS in low level NTFS acquisition via fsutil

### T1003.004: OS Credential Dumping: LSA Secrets (2 Tests)
- **Test 1** [command_prompt]: Dumping LSA Secrets
- **Test 2** [powershell]: Dump Kerberos Tickets from LSA using dumper.ps1

### T1003.005: OS Credential Dumping: Cached Domain Credentials (1 Tests)
- **Test 1** [command_prompt]: Cached Credential Dump via Cmdkey

### T1003.006: OS Credential Dumping: DCSync (2 Tests)
- **Test 1** [command_prompt]: DCSync (Active Directory)
- **Test 2** [powershell]: Run DSInternals Get-ADReplAccount

### T1040: Network Sniffing (5 Tests)
- **Test 4** [command_prompt]: Packet Capture Windows Command Prompt
- **Test 5** [command_prompt]: Windows Internal Packet Capture
- **Test 6** [command_prompt]: Windows Internal pktmon capture
- **Test 7** [command_prompt]: Windows Internal pktmon set filter
- **Test 16** [powershell]: PowerShell Network Sniffing

### T1056.001: Input Capture: Keylogging (1 Tests)
- **Test 1** [powershell]: Input Capture

### T1056.002: Input Capture: GUI Input Capture (1 Tests)
- **Test 2** [powershell]: PowerShell - Prompt User for Password

### T1056.004: Input Capture: Credential API Hooking (1 Tests)
- **Test 1** [powershell]: Hook PowerShell TLS Encrypt/Decrypt Messages

### T1110.001: Brute Force: Password Guessing (4 Tests)
- **Test 1** [command_prompt]: Brute Force Credentials of single Active Directory domain users via SMB
- **Test 2** [powershell]: Brute Force Credentials of single Active Directory domain user via LDAP against domain controller (NTLM or Kerberos)
- **Test 4** [powershell]: Password Brute User using Kerbrute Tool
- **Test 8** [powershell]: ESXi - Brute Force Until Account Lockout

### T1110.002: Brute Force: Password Cracking (1 Tests)
- **Test 1** [command_prompt]: Password Cracking with Hashcat

### T1110.003: Brute Force: Password Spraying (6 Tests)
- **Test 1** [command_prompt]: Password Spray all Domain Users
- **Test 2** [powershell]: Password Spray (DomainPasswordSpray)
- **Test 3** [powershell]: Password spray all Active Directory domain users with a single password via LDAP against domain controller (NTLM or Kerberos)
- **Test 5** [powershell]: WinPwn - DomainPasswordSpray Attacks
- **Test 6** [powershell]: Password Spray Invoke-DomainPasswordSpray Light
- **Test 8** [powershell]: Password Spray using Kerbrute Tool

### T1110.004: Brute Force: Credential Stuffing (1 Tests)
- **Test 4** [powershell]: Brute Force:Credential Stuffing using Kerbrute Tool

### T1187: Forced Authentication (3 Tests)
- **Test 1** [powershell]: PetitPotam
- **Test 2** [powershell]: WinPwn - PowerSharpPack - Retrieving NTLM Hashes without Touching LSASS
- **Test 3** [powershell]: Trigger an authenticated RPC call to a target server with no Sign flag set

### T1539: Steal Web Session Cookie (3 Tests)
- **Test 1** [powershell]: Steal Firefox Cookies (Windows)
- **Test 2** [powershell]: Steal Chrome Cookies (Windows)
- **Test 4** [powershell]: Steal Chrome v127+ cookies via Remote Debugging (Windows)

### T1552: Unsecured Credentials (1 Tests)
- **Test 2** [powershell]: Search for Passwords in Powershell History

### T1552.001: Unsecured Credentials: Credentials In Files (10 Tests)
- **Test 4** [powershell]: Extracting passwords with findstr
- **Test 5** [command_prompt]: Access unattend.xml
- **Test 7** [powershell]: WinPwn - sensitivefiles
- **Test 8** [powershell]: WinPwn - Snaffler
- **Test 9** [powershell]: WinPwn - powershellsensitive
- **Test 10** [powershell]: WinPwn - passhunt
- **Test 11** [powershell]: WinPwn - SessionGopher
- **Test 12** [powershell]: WinPwn - Loot local Credentials - AWS, Microsoft Azure, and Google Compute credentials
- **Test 13** [powershell]: List Credential Files via PowerShell
- **Test 14** [command_prompt]: List Credential Files via Command Prompt

### T1552.002: Unsecured Credentials: Credentials in Registry (2 Tests)
- **Test 1** [command_prompt]: Enumeration for Credentials in Registry
- **Test 2** [command_prompt]: Enumeration for PuTTY Credentials in Registry

### T1552.004: Unsecured Credentials: Private Keys (7 Tests)
- **Test 1** [command_prompt]: Private Keys
- **Test 9** [powershell]: ADFS token signing and encryption certificates theft - Local
- **Test 10** [powershell]: ADFS token signing and encryption certificates theft - Remote
- **Test 11** [powershell]: CertUtil ExportPFX
- **Test 12** [powershell]: Export Root Certificate with Export-PFXCertificate
- **Test 13** [powershell]: Export Root Certificate with Export-Certificate
- **Test 14** [command_prompt]: Export Certificates with Mimikatz

### T1552.006: Unsecured Credentials: Group Policy Preferences (2 Tests)
- **Test 1** [command_prompt]: GPP Passwords (findstr)
- **Test 2** [powershell]: GPP Passwords (Get-GPPPassword)

### T1555: Credentials from Password Stores (9 Tests)
- **Test 1** [powershell]: Extract Windows Credential Manager via VBA
- **Test 2** [powershell]: Dump credentials from Windows Credential Manager With PowerShell [windows Credentials]
- **Test 3** [powershell]: Dump credentials from Windows Credential Manager With PowerShell [web Credentials]
- **Test 4** [powershell]: Enumerate credentials from Windows Credential Manager using vaultcmd.exe [Windows Credentials]
- **Test 5** [powershell]: Enumerate credentials from Windows Credential Manager using vaultcmd.exe [Web Credentials]
- **Test 6** [powershell]: WinPwn - Loot local Credentials - lazagne
- **Test 7** [powershell]: WinPwn - Loot local Credentials - Wifi Credentials
- **Test 8** [powershell]: WinPwn - Loot local Credentials - Decrypt Teamviewer Passwords
- **Test 9** [powershell]: Warzone/AveMaria RAT Style Credential Theft via Outlook Registry

### T1555.003: Credentials from Password Stores: Credentials from Web Browsers (14 Tests)
- **Test 1** [powershell]: Run Chrome-password Collector
- **Test 3** [command_prompt]: LaZagne - Credentials from Browser
- **Test 4** [powershell]: Simulating access to Chrome Login Data
- **Test 5** [powershell]: Simulating access to Opera Login Data
- **Test 6** [powershell]: Simulating access to Windows Firefox Login Data
- **Test 7** [powershell]: Simulating access to Windows Edge Login Data
- **Test 8** [powershell]: Decrypt Mozilla Passwords with Firepwd.py
- **Test 10** [powershell]: Stage Popular Credential Files for Exfiltration
- **Test 11** [powershell]: WinPwn - BrowserPwn
- **Test 12** [powershell]: WinPwn - Loot local Credentials - mimi-kittenz
- **Test 13** [powershell]: WinPwn - PowerSharpPack - Sharpweb for Browser Credentials
- **Test 15** [powershell]: WebBrowserPassView - Credentials from Browser
- **Test 16** [powershell]: BrowserStealer (Chrome / Firefox / Microsoft Edge)
- **Test 17** [command_prompt]: Dump Chrome Login Data with esentutl

### T1555.004: Credentials from Password Stores: Windows Credential Manager (2 Tests)
- **Test 1** [command_prompt]: Access Saved Credentials via VaultCmd
- **Test 2** [powershell]: WinPwn - Loot local Credentials - Invoke-WCMDump

### T1556.001: Modify Authentication Process: Domain Controller Authentication (1 Tests)
- **Test 1** [powershell]: Skeleton Key via Mimikatz

### T1556.002: Modify Authentication Process: Password Filter DLL (2 Tests)
- **Test 1** [powershell]: Install and Register Password Filter DLL
- **Test 2** [powershell]: Install Additional Authentication Packages

### T1557.001: Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay (1 Tests)
- **Test 1** [powershell]: LLMNR Poisoning with Inveigh (PowerShell)

### T1558.001: Steal or Forge Kerberos Tickets: Golden Ticket (2 Tests)
- **Test 1** [powershell]: Crafting Active Directory golden tickets with mimikatz
- **Test 2** [powershell]: Crafting Active Directory golden tickets with Rubeus

### T1558.002: Steal or Forge Kerberos Tickets: Silver Ticket (1 Tests)
- **Test 1** [powershell]: Crafting Active Directory silver tickets with mimikatz

### T1558.003: Steal or Forge Kerberos Tickets: Kerberoasting (7 Tests)
- **Test 1** [powershell]: Request for service tickets
- **Test 2** [powershell]: Rubeus kerberoast
- **Test 3** [command_prompt]: Extract all accounts in use as SPN using setspn
- **Test 4** [powershell]: Request A Single Ticket via PowerShell
- **Test 5** [powershell]: Request All Tickets via PowerShell
- **Test 6** [powershell]: WinPwn - Kerberoasting
- **Test 7** [powershell]: WinPwn - PowerSharpPack - Kerberoasting Using Rubeus

### T1558.004: Steal or Forge Kerberos Tickets: AS-REP Roasting (3 Tests)
- **Test 1** [powershell]: Rubeus asreproast
- **Test 2** [powershell]: Get-DomainUser with PowerView
- **Test 3** [powershell]: WinPwn - PowerSharpPack - Kerberoasting Using Rubeus

### T1649: Steal or Forge Authentication Certificates (1 Tests)
- **Test 1** [powershell]: Staging Local Certificates via Export-Certificate

## Defense Impairment

### T1112: Modify Registry (92 Tests)
- **Test 1** [command_prompt]: Modify Registry of Current User Profile - cmd
- **Test 2** [command_prompt]: Modify Registry of Local Machine - cmd
- **Test 3** [command_prompt]: Modify registry to store logon credentials
- **Test 4** [powershell]: Use Powershell to Modify registry to store logon credentials
- **Test 5** [powershell]: Add domain to Trusted sites Zone
- **Test 6** [powershell]: Javascript in registry
- **Test 7** [powershell]: Change Powershell Execution Policy to Bypass
- **Test 8** [command_prompt]: BlackByte Ransomware Registry Changes - CMD
- **Test 9** [powershell]: BlackByte Ransomware Registry Changes - Powershell
- **Test 10** [command_prompt]: Disable Windows Registry Tool
- **Test 11** [powershell]: Disable Windows CMD application
- **Test 12** [command_prompt]: Disable Windows Task Manager application
- **Test 13** [command_prompt]: Disable Windows Notification Center
- **Test 14** [command_prompt]: Disable Windows Shutdown Button
- **Test 15** [command_prompt]: Disable Windows LogOff Button
- **Test 16** [command_prompt]: Disable Windows Change Password Feature
- **Test 17** [command_prompt]: Disable Windows Lock Workstation Feature
- **Test 18** [command_prompt]: Activate Windows NoDesktop Group Policy Feature
- **Test 19** [command_prompt]: Activate Windows NoRun Group Policy Feature
- **Test 20** [command_prompt]: Activate Windows NoFind Group Policy Feature
- **Test 21** [command_prompt]: Activate Windows NoControlPanel Group Policy Feature
- **Test 22** [command_prompt]: Activate Windows NoFileMenu Group Policy Feature
- **Test 23** [command_prompt]: Activate Windows NoClose Group Policy Feature
- **Test 24** [command_prompt]: Activate Windows NoSetTaskbar Group Policy Feature
- **Test 25** [command_prompt]: Activate Windows NoTrayContextMenu Group Policy Feature
- **Test 26** [command_prompt]: Activate Windows NoPropertiesMyDocuments Group Policy Feature
- **Test 27** [command_prompt]: Hide Windows Clock Group Policy Feature
- **Test 28** [command_prompt]: Windows HideSCAHealth Group Policy Feature
- **Test 29** [command_prompt]: Windows HideSCANetwork Group Policy Feature
- **Test 30** [command_prompt]: Windows HideSCAPower Group Policy Feature
- **Test 31** [command_prompt]: Windows HideSCAVolume Group Policy Feature
- **Test 32** [command_prompt]: Windows Modify Show Compress Color And Info Tip Registry
- **Test 33** [command_prompt]: Windows Powershell Logging Disabled
- **Test 34** [command_prompt]: Windows Add Registry Value to Load Service in Safe Mode without Network
- **Test 35** [command_prompt]: Windows Add Registry Value to Load Service in Safe Mode with Network
- **Test 36** [command_prompt]: Disable Windows Toast Notifications
- **Test 37** [command_prompt]: Disable Windows Security Center Notifications
- **Test 38** [command_prompt]: Suppress Win Defender Notifications
- **Test 39** [command_prompt]: Allow RDP Remote Assistance Feature
- **Test 40** [command_prompt]: NetWire RAT Registry Key Creation
- **Test 41** [command_prompt]: Ursnif Malware Registry Key Creation
- **Test 42** [command_prompt]: Terminal Server Client Connection History Cleared
- **Test 43** [command_prompt]: Disable Windows Error Reporting Settings
- **Test 44** [command_prompt]: DisallowRun Execution Of Certain Applications
- **Test 45** [command_prompt]: Enabling Restricted Admin Mode via Command_Prompt
- **Test 46** [command_prompt]: Mimic Ransomware - Enable Multiple User Sessions
- **Test 47** [command_prompt]: Mimic Ransomware - Allow Multiple RDP Sessions per User
- **Test 48** [command_prompt]: Event Viewer Registry Modification - Redirection URL
- **Test 49** [command_prompt]: Event Viewer Registry Modification - Redirection Program
- **Test 50** [command_prompt]: Enabling Remote Desktop Protocol via Remote Registry
- **Test 51** [command_prompt]: Disable Win Defender Notification
- **Test 52** [command_prompt]: Disable Windows OS Auto Update
- **Test 53** [command_prompt]: Disable Windows Auto Reboot for current logon user
- **Test 54** [command_prompt]: Windows Auto Update Option to Notify before download
- **Test 55** [command_prompt]: Do Not Connect To Win Update
- **Test 56** [command_prompt]: Tamper Win Defender Protection
- **Test 57** [powershell]: Snake Malware Registry Blob
- **Test 58** [command_prompt]: Allow Simultaneous Download Registry
- **Test 59** [command_prompt]: Modify Internet Zone Protocol Defaults in Current User Registry - cmd
- **Test 60** [powershell]: Modify Internet Zone Protocol Defaults in Current User Registry - PowerShell
- **Test 61** [command_prompt]: Activities To Disable Secondary Authentication Detected By Modified Registry Value.
- **Test 62** [command_prompt]: Activities To Disable Microsoft [FIDO Aka Fast IDentity Online] Authentication Detected By Modified Registry Value.
- **Test 63** [command_prompt]: Scarab Ransomware Defense Evasion Activities
- **Test 64** [command_prompt]: Disable Remote Desktop Anti-Alias Setting Through Registry
- **Test 65** [command_prompt]: Disable Remote Desktop Security Settings Through Registry
- **Test 66** [command_prompt]: Disabling ShowUI Settings of Windows Error Reporting (WER)
- **Test 67** [command_prompt]: Enable Proxy Settings
- **Test 68** [command_prompt]: Set-Up Proxy Server
- **Test 69** [command_prompt]: RDP Authentication Level Override
- **Test 70** [command_prompt]: Enable RDP via Registry (fDenyTSConnections)
- **Test 71** [command_prompt]: Disable Windows Prefetch Through Registry
- **Test 72** [powershell]: Setting Shadow key in Registry for RDP Shadowing
- **Test 73** [command_prompt]: Flush Shimcache
- **Test 74** [command_prompt]: Disable Windows Remote Desktop Protocol
- **Test 75** [command_prompt]: Enforce Smart Card Authentication Through Registry
- **Test 76** [command_prompt]: Requires the BitLocker PIN for Pre-boot authentication
- **Test 77** [command_prompt]: Modify EnableBDEWithNoTPM Registry entry
- **Test 78** [command_prompt]: Modify UseTPM Registry entry
- **Test 79** [command_prompt]: Modify UseTPMPIN Registry entry
- **Test 80** [command_prompt]: Modify UseTPMKey Registry entry
- **Test 81** [command_prompt]: Modify UseTPMKeyPIN Registry entry
- **Test 82** [command_prompt]: Modify EnableNonTPM Registry entry
- **Test 83** [command_prompt]: Modify UsePartialEncryptionKey Registry entry
- **Test 84** [command_prompt]: Modify UsePIN Registry entry
- **Test 85** [command_prompt]: Abusing Windows TelemetryController Registry Key for Persistence
- **Test 86** [command_prompt]: Modify RDP-Tcp Initial Program Registry Entry
- **Test 87** [command_prompt]: Abusing MyComputer Disk Cleanup Path for Persistence
- **Test 88** [command_prompt]: Abusing MyComputer Disk Fragmentation Path for Persistence
- **Test 89** [command_prompt]: Abusing MyComputer Disk Backup Path for Persistence
- **Test 90** [command_prompt]: Adding custom paths for application execution
- **Test 91** [powershell]: Turla Mosquito - Store Backdoor Path in OneDriveUpdate Registry Key
- **Test 92** [powershell]: Disable UAC remote restrictions via LocalAccountTokenFilterPolicy

### T1207: Rogue Domain Controller (1 Tests)
- **Test 1** [powershell]: DCShadow (Active Directory)

### T1222: File and Directory Permissions Modification (3 Tests)
- **Test 1** [command_prompt]: Enable Local and Remote Symbolic Links via fsutil
- **Test 2** [command_prompt]: Enable Local and Remote Symbolic Links via reg.exe
- **Test 3** [powershell]: Enable Local and Remote Symbolic Links via Powershell

### T1222.001: File and Directory Permissions Modification: Windows File and Directory Permissions Modification (6 Tests)
- **Test 1** [command_prompt]: Take ownership using takeown utility
- **Test 2** [command_prompt]: cacls - Grant permission to specified user or group recursively
- **Test 3** [command_prompt]: attrib - Remove read-only attribute
- **Test 4** [command_prompt]: attrib - hide file
- **Test 5** [command_prompt]: Grant Full Access to folder for Everyone - Ryuk Ransomware Style
- **Test 6** [command_prompt]: SubInAcl Execution

### T1484.001: Domain Policy Modification: Group Policy Modification (2 Tests)
- **Test 1** [command_prompt]: LockBit Black - Modify Group policy settings -cmd
- **Test 2** [powershell]: LockBit Black - Modify Group policy settings -Powershell

### T1553.003: Subvert Trust Controls: SIP and Trust Provider Hijacking (1 Tests)
- **Test 1** [command_prompt]: SIP (Subject Interface Package) Hijacking via Custom DLL

### T1553.004: Subvert Trust Controls: Install Root Certificate (3 Tests)
- **Test 5** [powershell]: Install root CA on Windows
- **Test 6** [powershell]: Install root CA on Windows with certutil
- **Test 7** [powershell]: Add Root Certificate to CurrentUser Certificate Store

### T1553.005: Subvert Trust Controls: Mark-of-the-Web Bypass (4 Tests)
- **Test 1** [powershell]: Mount ISO image
- **Test 2** [powershell]: Mount an ISO image and run executable from the ISO
- **Test 3** [powershell]: Remove the Zone.Identifier alternate data stream
- **Test 4** [powershell]: Execute LNK file from ISO

### T1553.006: Subvert Trust Controls: Code Signing Policy Modification (1 Tests)
- **Test 1** [command_prompt]: Code Signing Policy Modification

### T1556.001: Modify Authentication Process: Domain Controller Authentication (1 Tests)
- **Test 1** [powershell]: Skeleton Key via Mimikatz

### T1556.002: Modify Authentication Process: Password Filter DLL (2 Tests)
- **Test 1** [powershell]: Install and Register Password Filter DLL
- **Test 2** [powershell]: Install Additional Authentication Packages

### T1685: Disable or Modify Tools (52 Tests)
- **Test 1** [command_prompt]: Windows Disable LSA Protection
- **Test 14** [command_prompt]: Unload Sysmon Filter Driver
- **Test 15** [command_prompt]: Uninstall Sysmon
- **Test 16** [powershell]: AMSI Bypass - AMSI InitFailed
- **Test 17** [powershell]: AMSI Bypass - Remove AMSI Provider Reg Key
- **Test 18** [command_prompt]: Disable Arbitrary Security Windows Service
- **Test 19** [powershell]: Tamper with Windows Defender ATP PowerShell
- **Test 20** [command_prompt]: Tamper with Windows Defender Command Prompt
- **Test 21** [powershell]: Tamper with Windows Defender Registry
- **Test 22** [powershell]: Disable Microsoft Office Security Features
- **Test 23** [command_prompt]: Remove Windows Defender Definition Files
- **Test 24** [powershell]: Stop and Remove Arbitrary Security Windows Service
- **Test 25** [powershell]: Uninstall Crowdstrike Falcon on Windows
- **Test 26** [powershell]: Tamper with Windows Defender Evade Scanning -Folder
- **Test 27** [powershell]: Tamper with Windows Defender Evade Scanning -Extension
- **Test 28** [powershell]: Tamper with Windows Defender Evade Scanning -Process
- **Test 30** [command_prompt]: Disable Windows Defender with DISM
- **Test 31** [powershell]: Disable Defender Using NirSoft AdvancedRun
- **Test 32** [powershell]: Kill antimalware protected processes using Backstab
- **Test 33** [powershell]: WinPwn - Kill the event log services for stealth
- **Test 34** [powershell]: Tamper with Windows Defender ATP using Aliases - PowerShell
- **Test 35** [command_prompt]: LockBit Black - Disable Privacy Settings Experience Using Registry -cmd
- **Test 36** [command_prompt]: LockBit Black - Use Registry Editor to turn on automatic logon -cmd
- **Test 37** [powershell]: LockBit Black - Disable Privacy Settings Experience Using Registry -Powershell
- **Test 38** [powershell]: Lockbit Black - Use Registry Editor to turn on automatic logon -Powershell
- **Test 39** [powershell]: Disable Windows Defender with PwSh Disable-WindowsOptionalFeature
- **Test 40** [command_prompt]: WMIC Tamper with Windows Defender Evade Scanning Folder
- **Test 41** [command_prompt]: Delete Windows Defender Scheduled Tasks
- **Test 47** [powershell]: Disable Hypervisor-Enforced Code Integrity (HVCI)
- **Test 48** [command_prompt]: AMSI Bypass - Override AMSI via COM
- **Test 51** [command_prompt]: Tamper with Windows Defender Registry - Reg.exe
- **Test 52** [powershell]: Tamper with Windows Defender Registry - Powershell
- **Test 54** [powershell]: Delete Microsoft Defender ASR Rules - InTune
- **Test 55** [powershell]: Delete Microsoft Defender ASR Rules - GPO
- **Test 56** [powershell]: AMSI Bypass - Create AMSIEnable Reg Key
- **Test 57** [command_prompt]: Disable EventLog-Application Auto Logger Session Via Registry - Cmd
- **Test 58** [powershell]: Disable EventLog-Application Auto Logger Session Via Registry - PowerShell
- **Test 59** [command_prompt]: Disable EventLog-Application ETW Provider Via Registry - Cmd
- **Test 60** [powershell]: Disable EventLog-Application ETW Provider Via Registry - PowerShell
- **Test 61** [powershell]: Freeze PPL-protected process with EDR-Freeze
- **Test 67** [powershell]: Disable Powershell ETW Provider - Windows
- **Test 68** [command_prompt]: Disable .NET Event Tracing for Windows Via Registry (cmd)
- **Test 69** [powershell]: Disable .NET Event Tracing for Windows Via Registry (powershell)
- **Test 70** [command_prompt]: LockBit Black - Disable the ETW Provider of Windows Defender -cmd
- **Test 71** [powershell]: LockBit Black - Disable the ETW Provider of Windows Defender -Powershell
- **Test 72** [command_prompt]: Disable .NET Event Tracing for Windows Via Environment Variable HKCU Registry - Cmd
- **Test 73** [powershell]: Disable .NET Event Tracing for Windows Via Environment Variable HKCU Registry - PowerShell
- **Test 74** [command_prompt]: Disable .NET Event Tracing for Windows Via Environment Variable HKLM Registry - Cmd
- **Test 75** [powershell]: Disable .NET Event Tracing for Windows Via Environment Variable HKLM Registry - PowerShell
- **Test 76** [powershell]: Block Cybersecurity communication by leveraging Windows Name Resolution Policy Table
- **Test 77** [powershell]: Throttle Cybersecurity Agent Network Traffic via QoS Policy
- **Test 78** [powershell]: AMSI Bypass - Patching AmsiScanBuffer

### T1685.001: Disable or Modify Tools: Disable or Modify Windows Event Log (10 Tests)
- **Test 1** [powershell]: Disable Windows IIS HTTP Logging
- **Test 2** [powershell]: Disable Windows IIS HTTP Logging via PowerShell
- **Test 3** [powershell]: Kill Event Log Service Threads
- **Test 4** [command_prompt]: Impair Windows Audit Log Policy
- **Test 5** [command_prompt]: Clear Windows Audit Policy Config
- **Test 6** [command_prompt]: Disable Event Logging with wevtutil
- **Test 7** [command_prompt]: Makes Eventlog blind with Phant0m
- **Test 8** [powershell]: Modify Event Log Channel Access Permissions via Registry - PowerShell
- **Test 9** [powershell]: Modify Event Log Channel Access Permissions via Registry 2 - PowerShell
- **Test 10** [powershell]: Modify Event Log Access Permissions via Registry - PowerShell

### T1685.005: Disable or Modify Tools: Clear Windows Event Logs (4 Tests)
- **Test 1** [command_prompt]: Clear Logs
- **Test 2** [powershell]: Delete System Logs Using Clear-EventLog
- **Test 3** [powershell]: Clear Event Logs via VBA
- **Test 4** [command_prompt]: BlackCat Ransomware Full Log Clear

### T1686: Disable or Modify System Firewall (12 Tests)
- **Test 1** [command_prompt]: Disable Microsoft Defender Firewall
- **Test 2** [command_prompt]: Disable Microsoft Defender Firewall via Registry
- **Test 3** [command_prompt]: Allow SMB and RDP on Microsoft Defender Firewall
- **Test 4** [command_prompt]: Opening ports for proxy - HARDRAIN
- **Test 5** [powershell]: Open a local port through Windows Firewall to any profile
- **Test 6** [powershell]: Allow Executable Through Firewall Located in Non-Standard Location
- **Test 20** [command_prompt]: LockBit Black - Unusual Windows firewall registry modification -cmd
- **Test 21** [powershell]: LockBit Black - Unusual Windows firewall registry modification -Powershell
- **Test 22** [command_prompt]: Blackbit - Disable Windows Firewall using netsh firewall
- **Test 23** [command_prompt]: ESXi - Disable Firewall via Esxcli
- **Test 24** [powershell]: Set a firewall rule using New-NetFirewallRule
- **Test 25** [command_prompt]: ESXi - Set Firewall to PASS Traffic

### T1686.003: Disable or Modify System Firewall: Windows Host Firewall (2 Tests)
- **Test 1** [powershell]: Enable Firewall Rule Group via COM Object (HNetCfg.FwPolicy2)
- **Test 2** [powershell]: Set All Network Profiles to Private via Registry

### T1688: Safe Mode Boot (1 Tests)
- **Test 1** [command_prompt]: Safe Mode Boot

### T1689: Downgrade Attack (2 Tests)
- **Test 2** [command_prompt]: ESXi - Change VIB acceptance level to CommunitySupported via ESXCLI
- **Test 3** [powershell]: PowerShell Version 2 Downgrade

### T1690: Prevent Command History Logging (2 Tests)
- **Test 11** [command_prompt]: Disable Windows Command Line Auditing using reg.exe
- **Test 12** [powershell]: Disable Windows Command Line Auditing using Powershell Cmdlet

## Discovery

### T1007: System Service Discovery (5 Tests)
- **Test 1** [command_prompt]: System Service Discovery
- **Test 2** [command_prompt]: System Service Discovery - net.exe
- **Test 4** [command_prompt]: Get-Service Execution
- **Test 6** [command_prompt]: System Service Discovery - Windows Scheduled Tasks (schtasks)
- **Test 7** [powershell]: System Service Discovery - Services Registry Enumeration

### T1010: Application Window Discovery (1 Tests)
- **Test 1** [command_prompt]: List Process Main Windows - C# .NET

### T1012: Query Registry (6 Tests)
- **Test 1** [command_prompt]: Query Registry
- **Test 2** [powershell]: Query Registry with Powershell cmdlets
- **Test 3** [powershell]: Enumerate COM Objects in Registry with Powershell
- **Test 4** [command_prompt]: Reg query for AlwaysInstallElevated status
- **Test 5** [command_prompt]: Check Software Inventory Logging (SIL) status via Registry
- **Test 6** [command_prompt]: Inspect SystemStartOptions Value in Registry

### T1016: System Network Configuration Discovery (8 Tests)
- **Test 1** [command_prompt]: System Network Configuration Discovery on Windows
- **Test 2** [command_prompt]: List Windows Firewall Rules
- **Test 4** [command_prompt]: System Network Configuration Discovery (TrickBot Style)
- **Test 5** [powershell]: List Open Egress Ports
- **Test 6** [command_prompt]: Adfind - Enumerate Active Directory Subnet Objects
- **Test 7** [command_prompt]: Qakbot Recon
- **Test 9** [command_prompt]: DNS Server Discovery Using nslookup
- **Test 10** [powershell]: IPv4 Enumeration with GetIpAddrTable

### T1016.001: System Network Configuration Discovery: Internet Connection Discovery (4 Tests)
- **Test 1** [command_prompt]: Check internet connection using ping Windows
- **Test 3** [powershell]: Check internet connection using Test-NetConnection in PowerShell (ICMP-Ping)
- **Test 4** [powershell]: Check internet connection using Test-NetConnection in PowerShell (TCP-HTTP)
- **Test 5** [powershell]: Check internet connection using Test-NetConnection in PowerShell (TCP-SMB)

### T1016.002: System Network Configuration Discovery: Wi-Fi Discovery (1 Tests)
- **Test 1** [command_prompt]: Enumerate Stored Wi-Fi Profiles And Passwords via netsh

### T1018: Remote System Discovery (16 Tests)
- **Test 1** [command_prompt]: Remote System Discovery - net
- **Test 2** [command_prompt]: Remote System Discovery - net group Domain Computers
- **Test 3** [command_prompt]: Remote System Discovery - nltest
- **Test 4** [command_prompt]: Remote System Discovery - ping sweep
- **Test 5** [command_prompt]: Remote System Discovery - arp
- **Test 8** [powershell]: Remote System Discovery - nslookup
- **Test 9** [command_prompt]: Remote System Discovery - adidnsdump
- **Test 10** [command_prompt]: Adfind - Enumerate Active Directory Computer Objects
- **Test 11** [command_prompt]: Adfind - Enumerate Active Directory Domain Controller Objects
- **Test 16** [powershell]: Enumerate domain computers within Active Directory using DirectorySearcher
- **Test 17** [powershell]: Enumerate Active Directory Computers with Get-AdComputer
- **Test 18** [powershell]: Enumerate Active Directory Computers with ADSISearcher
- **Test 19** [powershell]: Get-DomainController with PowerView
- **Test 20** [powershell]: Get-WmiObject to Enumerate Domain Controllers
- **Test 21** [command_prompt]: Remote System Discovery - net group Domain Controller
- **Test 22** [powershell]: Enumerate Remote Hosts with Netscan

### T1033: System Owner/User Discovery (7 Tests)
- **Test 1** [command_prompt]: System Owner/User Discovery
- **Test 3** [powershell]: Find computers where user has session - Stealth mode (PowerView)
- **Test 4** [powershell]: User Discovery With Env Vars PowerShell Script
- **Test 5** [powershell]: GetCurrent User with PowerShell Script
- **Test 6** [powershell]: System Discovery - SocGholish whoami
- **Test 7** [command_prompt]: System Owner/User Discovery Using Command Prompt
- **Test 8** [command_prompt]: User Discovery - whoami

### T1040: Network Sniffing (5 Tests)
- **Test 4** [command_prompt]: Packet Capture Windows Command Prompt
- **Test 5** [command_prompt]: Windows Internal Packet Capture
- **Test 6** [command_prompt]: Windows Internal pktmon capture
- **Test 7** [command_prompt]: Windows Internal pktmon set filter
- **Test 16** [powershell]: PowerShell Network Sniffing

### T1046: Network Service Discovery (9 Tests)
- **Test 3** [powershell]: Port Scan NMap for Windows
- **Test 4** [powershell]: Port Scan using python
- **Test 5** [powershell]: WinPwn - spoolvulnscan
- **Test 6** [powershell]: WinPwn - MS17-10
- **Test 7** [powershell]: WinPwn - bluekeep
- **Test 8** [powershell]: WinPwn - fruit
- **Test 10** [powershell]: Port-Scanning /24 Subnet with PowerShell
- **Test 11** [powershell]: Remote Desktop Services Discovery via PowerShell
- **Test 13** [powershell]: Windows - Port Scan using RustScan (Port list)

### T1049: System Network Connections Discovery (4 Tests)
- **Test 1** [command_prompt]: System Network Connections Discovery
- **Test 2** [powershell]: System Network Connections Discovery with PowerShell
- **Test 3** [powershell]: System Network Connections Discovery via PowerShell (Process Mapping)
- **Test 7** [powershell]: System Discovery using SharpView

### T1057: Process Discovery (9 Tests)
- **Test 2** [command_prompt]: Process Discovery - tasklist
- **Test 3** [powershell]: Process Discovery - Get-Process
- **Test 4** [powershell]: Process Discovery - get-wmiObject
- **Test 5** [command_prompt]: Process Discovery - wmic process
- **Test 6** [command_prompt]: Discover Specific Process - tasklist
- **Test 7** [powershell]: Process Discovery - Process Hacker
- **Test 8** [powershell]: Process Discovery - PC Hunter
- **Test 9** [command_prompt]: Launch Taskmgr from cmd to View running processes
- **Test 10** [powershell]: Check Process Token Elevation via GetTokenInformation

### T1069.001: Permission Groups Discovery: Local Groups (5 Tests)
- **Test 2** [command_prompt]: Basic Permission Groups Discovery Windows (Local)
- **Test 3** [powershell]: Permission Groups Discovery PowerShell (Local)
- **Test 4** [powershell]: SharpHound3 - LocalAdmin
- **Test 5** [command_prompt]: Wmic Group Discovery
- **Test 6** [powershell]: WMIObject Group Discovery

### T1069.002: Permission Groups Discovery: Domain Groups (14 Tests)
- **Test 1** [command_prompt]: Basic Permission Groups Discovery Windows (Domain)
- **Test 2** [powershell]: Permission Groups Discovery PowerShell (Domain)
- **Test 3** [command_prompt]: Elevated group enumeration using net group (Domain)
- **Test 4** [powershell]: Find machines where user has local admin access (PowerView)
- **Test 5** [powershell]: Find local admins on all machines in domain (PowerView)
- **Test 6** [powershell]: Find Local Admins via Group Policy (PowerView)
- **Test 7** [powershell]: Enumerate Users Not Requiring Pre Auth (ASRepRoast)
- **Test 8** [command_prompt]: Adfind - Query Active Directory Groups
- **Test 9** [powershell]: Enumerate Active Directory Groups with Get-AdGroup
- **Test 10** [powershell]: Enumerate Active Directory Groups with ADSISearcher
- **Test 11** [powershell]: Get-ADUser Enumeration using UserAccountControl flags (AS-REP Roasting)
- **Test 12** [powershell]: Get-DomainGroupMember with PowerView
- **Test 13** [powershell]: Get-DomainGroup with PowerView
- **Test 14** [command_prompt]: Active Directory Enumeration with LDIFDE

### T1082: System Information Discovery (29 Tests)
- **Test 1** [command_prompt]: System Information Discovery
- **Test 7** [command_prompt]: Hostname Discovery (Windows)
- **Test 9** [command_prompt]: Windows MachineGUID Discovery
- **Test 10** [powershell]: Griffon Recon
- **Test 11** [command_prompt]: Environment variables discovery on windows
- **Test 14** [powershell]: WinPwn - winPEAS
- **Test 15** [powershell]: WinPwn - itm4nprivesc
- **Test 16** [powershell]: WinPwn - Powersploits privesc checks
- **Test 17** [powershell]: WinPwn - General privesc checks
- **Test 18** [powershell]: WinPwn - GeneralRecon
- **Test 19** [powershell]: WinPwn - Morerecon
- **Test 20** [powershell]: WinPwn - RBCD-Check
- **Test 21** [powershell]: WinPwn - PowerSharpPack - Watson searching for missing windows patches
- **Test 22** [powershell]: WinPwn - PowerSharpPack - Sharpup checking common Privesc vectors
- **Test 23** [powershell]: WinPwn - PowerSharpPack - Seatbelt
- **Test 27** [command_prompt]: System Information Discovery with WMIC
- **Test 28** [command_prompt]: System Information Discovery
- **Test 29** [command_prompt]: Check computer location
- **Test 30** [command_prompt]: BIOS Information Discovery through Registry
- **Test 31** [command_prompt]: ESXi - VM Discovery using ESXCLI
- **Test 32** [command_prompt]: ESXi - Darkside system information discovery
- **Test 34** [powershell]: operating system discovery
- **Test 35** [command_prompt]: Check OS version via "ver" command
- **Test 36** [command_prompt]: Display volume shadow copies with "vssadmin"
- **Test 37** [command_prompt]: Identify System Locale and Regional Settings with PowerShell
- **Test 38** [command_prompt]: Enumerate Available Drives via gdr
- **Test 39** [command_prompt]: Discover OS Product Name via Registry
- **Test 40** [command_prompt]: Discover OS Build Number via Registry
- **Test 41** [powershell]: Get System Hardware UUID Via wmic.exe

### T1083: File and Directory Discovery (6 Tests)
- **Test 1** [command_prompt]: File and Directory Discovery (cmd.exe)
- **Test 2** [powershell]: File and Directory Discovery (PowerShell)
- **Test 5** [powershell]: Simulating MAZE Directory Enumeration
- **Test 6** [powershell]: Launch DirLister Executable
- **Test 7** [command_prompt]: ESXi - Enumerate VMDKs available on an ESXi Host
- **Test 9** [powershell]: Recursive Enumerate Files And Directories By Powershell

### T1087.001: Account Discovery: Local Account (4 Tests)
- **Test 8** [command_prompt]: Enumerate all accounts on Windows (Local)
- **Test 9** [powershell]: Enumerate all accounts via PowerShell (Local)
- **Test 10** [command_prompt]: Enumerate logged on users via CMD (Local)
- **Test 11** [command_prompt]: ESXi - Local Account Discovery via ESXCLI

### T1087.002: Account Discovery: Domain Account (22 Tests)
- **Test 1** [command_prompt]: Enumerate all accounts (Domain)
- **Test 2** [powershell]: Enumerate all accounts via PowerShell (Domain)
- **Test 3** [command_prompt]: Enumerate logged on users via CMD (Domain)
- **Test 4** [powershell]: Automated AD Recon (ADRecon)
- **Test 5** [command_prompt]: Adfind -Listing password policy
- **Test 6** [command_prompt]: Adfind - Enumerate Active Directory Admins
- **Test 7** [command_prompt]: Adfind - Enumerate Active Directory User Objects
- **Test 8** [command_prompt]: Adfind - Enumerate Active Directory Exchange AD Objects
- **Test 9** [command_prompt]: Enumerate Default Domain Admin Details (Domain)
- **Test 10** [powershell]: Enumerate Active Directory for Unconstrained Delegation
- **Test 11** [powershell]: Get-DomainUser with PowerView
- **Test 12** [powershell]: Enumerate Active Directory Users with ADSISearcher
- **Test 13** [powershell]: Enumerate Linked Policies In ADSISearcher Discovery
- **Test 14** [powershell]: Enumerate Root Domain linked policies Discovery
- **Test 15** [powershell]: WinPwn - generaldomaininfo
- **Test 16** [powershell]: Kerbrute - userenum
- **Test 17** [powershell]: Wevtutil - Discover NTLM Users Remote
- **Test 18** [powershell]: Suspicious LAPS Attributes Query with Get-ADComputer all properties
- **Test 19** [powershell]: Suspicious LAPS Attributes Query with Get-ADComputer ms-Mcs-AdmPwd property
- **Test 20** [powershell]: Suspicious LAPS Attributes Query with Get-ADComputer all properties and SearchScope
- **Test 21** [powershell]: Suspicious LAPS Attributes Query with adfind all properties
- **Test 22** [powershell]: Suspicious LAPS Attributes Query with adfind ms-Mcs-AdmPwd

### T1120: Peripheral Device Discovery (4 Tests)
- **Test 1** [powershell]: Win32_PnPEntity Hardware Inventory
- **Test 2** [powershell]: WinPwn - printercheck
- **Test 3** [command_prompt]: Peripheral Device Discovery via fsutil
- **Test 4** [powershell]: Get Printer Device List via PowerShell Command

### T1124: System Time Discovery (5 Tests)
- **Test 1** [command_prompt]: System Time Discovery
- **Test 2** [powershell]: System Time Discovery - PowerShell
- **Test 4** [command_prompt]: System Time Discovery W32tm as a Delay
- **Test 5** [command_prompt]: System Time with Windows time Command
- **Test 6** [command_prompt]: Discover System Time Zone via Registry

### T1135: Network Share Discovery (9 Tests)
- **Test 4** [command_prompt]: Network Share Discovery command prompt
- **Test 5** [powershell]: Network Share Discovery PowerShell
- **Test 6** [command_prompt]: View available share drives
- **Test 7** [powershell]: Share Discovery with PowerView
- **Test 8** [powershell]: PowerView ShareFinder
- **Test 9** [powershell]: WinPwn - shareenumeration
- **Test 10** [command_prompt]: Network Share Discovery via dir command
- **Test 11** [powershell]: Enumerate All Network Shares with SharpShares
- **Test 12** [powershell]: Enumerate All Network Shares with Snaffler

### T1201: Password Policy Discovery (5 Tests)
- **Test 6** [command_prompt]: Examine local password policy - Windows
- **Test 7** [command_prompt]: Examine domain password policy - Windows
- **Test 9** [powershell]: Get-DomainPolicy with PowerView
- **Test 10** [powershell]: Enumerate Active Directory Password Policy with get-addefaultdomainpasswordpolicy
- **Test 11** [command_prompt]: Use of SecEdit.exe to export the local security policy (including the password policy)

### T1217: Browser Bookmark Discovery (6 Tests)
- **Test 5** [powershell]: List Google Chrome / Opera Bookmarks on Windows with powershell
- **Test 6** [command_prompt]: List Google Chrome / Edge Chromium Bookmarks on Windows with command prompt
- **Test 7** [command_prompt]: List Mozilla Firefox bookmarks on Windows with command prompt
- **Test 8** [command_prompt]: List Internet Explorer Bookmarks using the command prompt
- **Test 10** [powershell]: Extract Edge Browsing History
- **Test 11** [powershell]: Extract chrome Browsing History

### T1482: Domain Trust Discovery (8 Tests)
- **Test 1** [command_prompt]: Windows - Discover domain trusts with dsquery
- **Test 2** [command_prompt]: Windows - Discover domain trusts with nltest
- **Test 3** [powershell]: Powershell enumerate domains and forests
- **Test 4** [command_prompt]: Adfind - Enumerate Active Directory OUs
- **Test 5** [command_prompt]: Adfind - Enumerate Active Directory Trusts
- **Test 6** [powershell]: Get-DomainTrust with PowerView
- **Test 7** [powershell]: Get-ForestTrust with PowerView
- **Test 8** [command_prompt]: TruffleSnout - Listing AD Infrastructure

### T1497.001: Virtualization/Sandbox Evasion: System Checks (3 Tests)
- **Test 3** [powershell]: Detect Virtualization Environment (Windows)
- **Test 5** [powershell]: Detect Virtualization Environment via WMI Manufacturer/Model Listing (Windows)
- **Test 9** [powershell]: Turla Mosquito Sandbox Evasion via SetupDiGetClassDevs Check

### T1518: Software Discovery (5 Tests)
- **Test 1** [command_prompt]: Find and Display Internet Explorer Browser Version
- **Test 2** [powershell]: Applications Installed
- **Test 4** [powershell]: WinPwn - Dotnetsearch
- **Test 5** [powershell]: WinPwn - DotNet
- **Test 6** [powershell]: WinPwn - powerSQL

### T1518.001: Software Discovery: Security Software Discovery (9 Tests)
- **Test 1** [command_prompt]: Security Software Discovery
- **Test 2** [powershell]: Security Software Discovery - powershell
- **Test 6** [command_prompt]: Security Software Discovery - Sysmon Service
- **Test 7** [command_prompt]: Security Software Discovery - AV Discovery via WMI
- **Test 8** [command_prompt]: Security Software Discovery - AV Discovery via Get-CimInstance and Get-WmiObject cmdlets
- **Test 9** [powershell]: Security Software Discovery - Windows Defender Enumeration
- **Test 10** [powershell]: Security Software Discovery - Windows Firewall Enumeration
- **Test 11** [command_prompt]: Get Windows Defender exclusion settings using WMIC
- **Test 12** [powershell]: Enumerate Windows Defender exclusion paths via MpCmdRun.exe

### T1614: System Location Discovery (1 Tests)
- **Test 1** [command_prompt]: Get geolocation info through IP-Lookup services using curl Windows

### T1614.001: System Location Discovery: System Language Discovery (6 Tests)
- **Test 1** [command_prompt]: Discover System Language by Registry Query
- **Test 2** [command_prompt]: Discover System Language with chcp
- **Test 7** [command_prompt]: Discover System Language with dism.exe
- **Test 8** [command_prompt]: Discover System Language by Windows API Query
- **Test 9** [command_prompt]: Discover System Language with WMIC
- **Test 10** [powershell]: Discover System Language with Powershell

### T1615: Group Policy Discovery (5 Tests)
- **Test 1** [command_prompt]: Display group policy information via gpresult
- **Test 2** [powershell]: Get-DomainGPO to display group policy information via PowerView
- **Test 3** [powershell]: WinPwn - GPOAudit
- **Test 4** [powershell]: WinPwn - GPORemoteAccessPolicy
- **Test 5** [powershell]: MSFT Get-GPO Cmdlet

### T1622: Debugger Evasion (1 Tests)
- **Test 1** [powershell]: Detect a Debugger Presence in the Machine

### T1652: Device Driver Discovery (1 Tests)
- **Test 1** [powershell]: Device Driver Discovery

### T1654: Log Enumeration (2 Tests)
- **Test 1** [powershell]: Get-EventLog To Enumerate Windows Security Log
- **Test 2** [command_prompt]: Enumerate Windows Security Log via WevtUtil

### T1680: Local Storage Discovery (2 Tests)
- **Test 1** [powershell]: Local Storage Discovery via PSDrive
- **Test 2** [command_prompt]: Local Storage Discovery via wmic

## Execution

### T1047: Windows Management Instrumentation (12 Tests)
- **Test 1** [command_prompt]: WMI Reconnaissance Users
- **Test 2** [command_prompt]: WMI Reconnaissance Processes
- **Test 3** [command_prompt]: WMI Reconnaissance Software
- **Test 4** [command_prompt]: WMI Reconnaissance List Remote Services
- **Test 5** [command_prompt]: WMI Execute Local Process
- **Test 6** [command_prompt]: WMI Execute Remote Process
- **Test 7** [command_prompt]: Create a Process using WMI Query and an Encoded Command
- **Test 8** [powershell]: Create a Process using obfuscated Win32_Process
- **Test 9** [command_prompt]: WMI Execute rundll32
- **Test 10** [command_prompt]: Application uninstall using WMIC
- **Test 11** [powershell]: Impacket wmiexec.py
- **Test 12** [powershell]: AveMaria/Warzone program.bat WMIC Process Creation

### T1053.002: Scheduled Task/Job: At (1 Tests)
- **Test 1** [command_prompt]: At.exe Scheduled task

### T1053.005: Scheduled Task/Job: Scheduled Task (14 Tests)
- **Test 1** [command_prompt]: Scheduled Task Startup Script
- **Test 2** [command_prompt]: Scheduled task Local
- **Test 3** [command_prompt]: Scheduled task Remote
- **Test 4** [powershell]: Powershell Cmdlet Scheduled Task
- **Test 5** [powershell]: Task Scheduler via VBA
- **Test 6** [powershell]: WMI Invoke-CimMethod Scheduled Task
- **Test 7** [command_prompt]: Scheduled Task Executing Base64 Encoded Commands From Registry
- **Test 8** [powershell]: Import XML Schedule Task with Hidden Attribute
- **Test 9** [powershell]: PowerShell Modify A Scheduled Task
- **Test 10** [command_prompt]: Scheduled Task ("Ghost Task") via Registry Key Manipulation
- **Test 11** [command_prompt]: Scheduled Task Persistence via CompMgmt.msc
- **Test 12** [command_prompt]: Scheduled Task Persistence via Eventviewer.msc
- **Test 13** [powershell]: Turla Topinambour Dropper and Scheduled Task Persistence
- **Test 14** [command_prompt]: Turla KopiLuwak Scheduled Task for JavaScript Stager

### T1059: Command and Scripting Interpreter (1 Tests)
- **Test 1** [powershell]: AutoIt Script Execution

### T1059.001: Command and Scripting Interpreter: PowerShell (22 Tests)
- **Test 1** [powershell]: Mimikatz
- **Test 2** [powershell]: Run BloodHound from local disk
- **Test 3** [powershell]: Run Bloodhound from Memory using Download Cradle
- **Test 4** [powershell]: Mimikatz - Cradlecraft PsSendKeys
- **Test 5** [command_prompt]: Invoke-AppPathBypass
- **Test 6** [command_prompt]: Powershell MsXml COM object - with prompt
- **Test 7** [command_prompt]: Powershell XML requests
- **Test 8** [command_prompt]: Powershell invoke mshta.exe download
- **Test 9** [manual]: Powershell Invoke-DownloadCradle
- **Test 10** [powershell]: PowerShell Fileless Script Execution
- **Test 11** [powershell]: NTFS Alternate Data Stream Access
- **Test 12** [powershell]: PowerShell Session Creation and Use
- **Test 13** [powershell]: ATHPowerShellCommandLineParameter -Command parameter variations
- **Test 14** [powershell]: ATHPowerShellCommandLineParameter -Command parameter variations with encoded arguments
- **Test 15** [powershell]: ATHPowerShellCommandLineParameter -EncodedCommand parameter variations
- **Test 16** [powershell]: ATHPowerShellCommandLineParameter -EncodedCommand parameter variations with encoded arguments
- **Test 17** [command_prompt]: PowerShell Command Execution
- **Test 18** [powershell]: PowerShell Invoke Known Malicious Cmdlets
- **Test 19** [powershell]: PowerUp Invoke-AllChecks
- **Test 20** [powershell]: Abuse Nslookup with DNS Records
- **Test 21** [powershell]: SOAPHound - Dump BloodHound Data
- **Test 22** [powershell]: SOAPHound - Build Cache

### T1059.003: Command and Scripting Interpreter: Windows Command Shell (6 Tests)
- **Test 1** [powershell]: Create and Execute Batch Script
- **Test 2** [command_prompt]: Writes text to a file and displays it.
- **Test 3** [command_prompt]: Suspicious Execution via Windows Command Shell
- **Test 4** [powershell]: Simulate BlackByte Ransomware Print Bombing
- **Test 5** [command_prompt]: Command Prompt read contents from CMD file and execute
- **Test 6** [command_prompt]: Command prompt writing script to file then executes it

### T1059.005: Command and Scripting Interpreter: Visual Basic (3 Tests)
- **Test 1** [powershell]: Visual Basic script execution to gather local computer information
- **Test 2** [powershell]: Encoded VBS code execution
- **Test 3** [powershell]: Extract Memory via VBA

### T1059.007: Command and Scripting Interpreter: JavaScript (5 Tests)
- **Test 1** [command_prompt]: JScript execution to gather local computer information via cscript
- **Test 2** [command_prompt]: JScript execution to gather local computer information via wscript
- **Test 3** [command_prompt]: Turla Kopiluwak Windows Enumeration
- **Test 4** [command_prompt]: Turla KopiLuwak RC4 Decryption Stager
- **Test 5** [powershell]: Turla KopiLuwak Registry JavaScript Payload Execution

### T1059.010: Command and Scripting Interpreter: AutoHotKey & AutoIT (1 Tests)
- **Test 1** [powershell]: AutoHotKey script execution

### T1072: Software Deployment Tools (3 Tests)
- **Test 1** [command_prompt]: Radmin Viewer Utility
- **Test 2** [command_prompt]: PDQ Deploy RAT
- **Test 3** [powershell]: Deploy 7-Zip Using Chocolatey

### T1106: Native API (5 Tests)
- **Test 1** [command_prompt]: Execution through API - CreateProcess
- **Test 2** [powershell]: WinPwn - Get SYSTEM shell - Pop System Shell using CreateProcess technique
- **Test 3** [powershell]: WinPwn - Get SYSTEM shell - Bind System Shell using CreateProcess technique
- **Test 4** [powershell]: WinPwn - Get SYSTEM shell - Pop System Shell using NamedPipe Impersonation technique
- **Test 5** [powershell]: Run Shellcode via Syscall in Go

### T1127: Trusted Developer Utilities Proxy Execution (2 Tests)
- **Test 1** [command_prompt]: Lolbin Jsc.exe compile javascript to exe
- **Test 2** [command_prompt]: Lolbin Jsc.exe compile javascript to dll

### T1127.001: Trusted Developer Utilities Proxy Execution: MSBuild (2 Tests)
- **Test 1** [command_prompt]: MSBuild Bypass Using Inline Tasks (C#)
- **Test 2** [command_prompt]: MSBuild Bypass Using Inline Tasks (VB)

### T1129: Shared Modules (1 Tests)
- **Test 1** [command_prompt]: ESXi - Install a custom VIB on an ESXi host

### T1197: BITS Jobs (4 Tests)
- **Test 1** [command_prompt]: Bitsadmin Download (cmd)
- **Test 2** [powershell]: Bitsadmin Download (PowerShell)
- **Test 3** [command_prompt]: Persist, Download, & Execute
- **Test 4** [command_prompt]: Bits download using desktopimgdownldr.exe (cmd)

### T1204.002: User Execution: Malicious File (13 Tests)
- **Test 1** [powershell]: OSTap Style Macro Execution
- **Test 2** [command_prompt]: OSTap Payload Download
- **Test 3** [powershell]: Maldoc choice flags command execution
- **Test 4** [powershell]: OSTAP JS version
- **Test 5** [powershell]: Office launching .bat file from AppData
- **Test 6** [powershell]: Excel 4 Macro
- **Test 7** [powershell]: Headless Chrome code execution via VBA
- **Test 8** [powershell]: Potentially Unwanted Applications (PUA)
- **Test 9** [powershell]: Office Generic Payload Download
- **Test 10** [powershell]: LNK Payload Download
- **Test 11** [powershell]: Mirror Blast Emulation
- **Test 12** [powershell]: ClickFix Campaign - Abuse RunMRU to Launch mshta via PowerShell
- **Test 13** [powershell]: Simulate Click-Fix via Downloaded BAT File

### T1204.004: Malicious Copy and Paste (1 Tests)
- **Test 1** [manual]: Malicious Copy and Paste through Run.exe

### T1559: Inter-Process Communication (7 Tests)
- **Test 1** [command_prompt]: Cobalt Strike Artifact Kit pipe
- **Test 2** [command_prompt]: Cobalt Strike Lateral Movement (psexec_psh) pipe
- **Test 3** [command_prompt]: Cobalt Strike SSH (postex_ssh) pipe
- **Test 4** [command_prompt]: Cobalt Strike post-exploitation pipe (4.2 and later)
- **Test 5** [command_prompt]: Cobalt Strike post-exploitation pipe (before 4.2)
- **Test 6** [powershell]: Create Named Pipe
- **Test 7** [powershell]: Named Pipe Integrity Reduction for Turla's RPC backdoor

### T1559.002: Inter-Process Communication: Dynamic Data Exchange (3 Tests)
- **Test 1** [manual]: Execute Commands
- **Test 2** [command_prompt]: Execute PowerShell script via Word DDE
- **Test 3** [manual]: DDEAUTO

### T1569.002: System Services: Service Execution (7 Tests)
- **Test 1** [command_prompt]: Execute a Command as a Service
- **Test 2** [command_prompt]: Use PsExec to execute a command on a remote host
- **Test 4** [powershell]: BlackCat pre-encryption cmds with Lateral Movement
- **Test 5** [command_prompt]: Use RemCom to execute a command on a remote host
- **Test 6** [command_prompt]: Snake Malware Service Create
- **Test 7** [command_prompt]: Modifying ACL of Service Control Manager via SDET
- **Test 8** [powershell]: Pipe Creation - PsExec Tool Execution From Suspicious Locations

### T1574.001: Hijack Execution Flow: DLL (7 Tests)
- **Test 1** [command_prompt]: DLL Search Order Hijacking - amsi.dll
- **Test 2** [command_prompt]: Phantom Dll Hijacking - WinAppXRT.dll
- **Test 3** [command_prompt]: Phantom Dll Hijacking - ualapi.dll
- **Test 4** [command_prompt]: DLL Side-Loading using the Notepad++ GUP.exe binary
- **Test 5** [command_prompt]: DLL Side-Loading using the dotnet startup hook environment variable
- **Test 6** [powershell]: DLL Search Order Hijacking,DLL Sideloading Of KeyScramblerIE.DLL Via KeyScrambler.EXE
- **Test 7** [command_prompt]: DLL Search Order Hijacking - ntprint

### T1574.008: Hijack Execution Flow: Path Interception by Search Order Hijacking (1 Tests)
- **Test 1** [powershell]: powerShell Persistence via hijacking default modules - Get-Variable.exe

### T1574.009: Hijack Execution Flow: Path Interception by Unquoted Path (1 Tests)
- **Test 1** [command_prompt]: Execution of program.exe as service with unquoted service path

### T1574.011: Hijack Execution Flow: Services Registry Permissions Weakness (2 Tests)
- **Test 1** [powershell]: Service Registry Permissions Weakness
- **Test 2** [command_prompt]: Service ImagePath Change with reg.exe

### T1574.012: Hijack Execution Flow: COR_PROFILER (3 Tests)
- **Test 1** [powershell]: User scope COR_PROFILER
- **Test 2** [powershell]: System Scope COR_PROFILER
- **Test 3** [powershell]: Registry-free process scope COR_PROFILER

## Exfiltration

### T1020: Automated Exfiltration (2 Tests)
- **Test 1** [powershell]: IcedID Botnet HTTP PUT
- **Test 2** [powershell]: Exfiltration via Encrypted FTP

### T1030: Data Transfer Size Limits (1 Tests)
- **Test 2** [powershell]: Network-Based Data Transfer in Small Chunks

### T1041: Exfiltration Over C2 Channel (2 Tests)
- **Test 1** [powershell]: C2 Data Exfiltration
- **Test 2** [powershell]: Text Based Data Exfiltration using DNS subdomains

### T1048: Exfiltration Over Alternative Protocol (1 Tests)
- **Test 3** [powershell]: DNSExfiltration (doh)

### T1048.002: Exfiltration Over Alternative Protocol - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol (1 Tests)
- **Test 1** [command_prompt]: Exfiltrate data HTTPS using curl windows

### T1048.003: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol (5 Tests)
- **Test 2** [powershell]: Exfiltration Over Alternative Protocol - ICMP
- **Test 4** [powershell]: Exfiltration Over Alternative Protocol - HTTP
- **Test 5** [powershell]: Exfiltration Over Alternative Protocol - SMTP
- **Test 6** [powershell]: MAZE FTP Upload
- **Test 7** [powershell]: Exfiltration Over Alternative Protocol - FTP - Rclone

### T1567.002: Exfiltration Over Web Service: Exfiltration to Cloud Storage (1 Tests)
- **Test 1** [powershell]: Exfiltrate data with rclone to cloud Storage - Mega (Windows)

### T1567.003: Exfiltration Over Web Service: Exfiltration to Text Storage Sites (1 Tests)
- **Test 1** [powershell]: Exfiltrate data with HTTP POST to text storage sites - pastebin.com (Windows)

### T1567.004: Exfiltration Over Web Service: Exfiltration Over Webhook (2 Tests)
- **Test 1** [powershell]: Exfiltrate staged data to a Discord webhook (PowerShell)
- **Test 4** [powershell]: Exfiltrate staged data to a Microsoft Teams webhook (PowerShell)

## Impact

### T1485: Data Destruction (3 Tests)
- **Test 1** [powershell]: Windows - Overwrite file with SysInternals SDelete
- **Test 3** [command_prompt]: Overwrite deleted data on C drive
- **Test 5** [command_prompt]: ESXi - Delete VM Snapshots

### T1486: Data Encrypted for Impact (4 Tests)
- **Test 5** [command_prompt]: PureLocker Ransom Note
- **Test 8** [powershell]: Data Encrypted with GPG4Win
- **Test 9** [command_prompt]: Data Encrypt Using DiskCryptor
- **Test 10** [powershell]: Akira Ransomware drop Files with .akira Extension and Ransomnote

### T1489: Service Stop (4 Tests)
- **Test 1** [command_prompt]: Windows - Stop service using Service Controller
- **Test 2** [command_prompt]: Windows - Stop service using net.exe
- **Test 3** [command_prompt]: Windows - Stop service by killing process
- **Test 9** [powershell]: Windows - iisreset.exe to stop Internet services

### T1490: Inhibit System Recovery (12 Tests)
- **Test 1** [command_prompt]: Windows - Delete Volume Shadow Copies
- **Test 2** [command_prompt]: Windows - Delete Volume Shadow Copies via WMI
- **Test 3** [command_prompt]: Windows - wbadmin Delete Windows Backup Catalog
- **Test 4** [command_prompt]: Windows - Disable Windows Recovery Console Repair
- **Test 5** [powershell]: Windows - Delete Volume Shadow Copies via WMI with PowerShell
- **Test 6** [command_prompt]: Windows - Delete Backup Files
- **Test 7** [command_prompt]: Windows - wbadmin Delete systemstatebackup
- **Test 8** [command_prompt]: Windows - Disable the SR scheduled task
- **Test 9** [command_prompt]: Disable System Restore Through Registry
- **Test 10** [powershell]: Windows - vssadmin Resize Shadowstorage Volume
- **Test 11** [command_prompt]: Modify VSS Service Permissions
- **Test 13** [powershell]: Windows - Delete Volume Shadow Copies via Diskshadow

### T1491.001: Defacement: Internal Defacement (4 Tests)
- **Test 1** [powershell]: Replace Desktop Wallpaper
- **Test 2** [powershell]: Configure LegalNoticeCaption and LegalNoticeText registry keys to display ransom message
- **Test 3** [command_prompt]: ESXi - Change Welcome Message on Direct Console User Interface (DCUI)
- **Test 4** [powershell]: Windows - Display a simulated ransom note via Notepad (non-destructive)

### T1496: Resource Hijacking (1 Tests)
- **Test 2** [powershell]: Windows - Simulate CPU Load with PowerShell

### T1529: System Shutdown/Reboot (6 Tests)
- **Test 1** [command_prompt]: Shutdown System - Windows
- **Test 2** [command_prompt]: Restart System - Windows
- **Test 12** [command_prompt]: Logoff System - Windows
- **Test 13** [command_prompt]: ESXi - Terminates VMs using pkill
- **Test 14** [command_prompt]: ESXi - Avoslocker enumerates VMs and forcefully kills VMs
- **Test 15** [command_prompt]: ESXi - vim-cmd Used to Power Off VMs

### T1531: Account Access Removal (3 Tests)
- **Test 1** [command_prompt]: Change User Password - Windows
- **Test 2** [command_prompt]: Delete User - Windows
- **Test 3** [powershell]: Remove Account From Domain Admin Group

## Initial Access

### T1078.001: Valid Accounts: Default Accounts (2 Tests)
- **Test 1** [command_prompt]: Enable Guest account with RDP capability and admin privileges
- **Test 2** [command_prompt]: Activate Guest Account

### T1078.003: Valid Accounts: Local Accounts (4 Tests)
- **Test 1** [command_prompt]: Create local account with admin privileges
- **Test 6** [powershell]: WinPwn - Loot local Credentials - powerhell kittie
- **Test 7** [powershell]: WinPwn - Loot local Credentials - Safetykatz
- **Test 13** [command_prompt]: Use PsExec to elevate to NT Authority\SYSTEM account

### T1091: Replication Through Removable Media (1 Tests)
- **Test 1** [powershell]: USB Malware Spread Simulation

### T1133: External Remote Services (1 Tests)
- **Test 1** [powershell]: Running Chrome VPN Extensions via the Registry 2 vpn extension

### T1195: Supply Chain Compromise (1 Tests)
- **Test 1** [command_prompt]: Octopus Scanner Malware Open Source Supply Chain

### T1566.001: Phishing: Spearphishing Attachment (2 Tests)
- **Test 1** [powershell]: Download Macro-Enabled Phishing Attachment
- **Test 2** [powershell]: Word spawned a command shell and used an IP address in the command line

### T1566.002: Phishing: Spearphishing Link (1 Tests)
- **Test 1** [powershell]: Paste and run technique

### T1659: Content Injection (1 Tests)
- **Test 2** [powershell]: MITM Proxy Injection (Windows)

## Lateral Movement

### T1021.001: Remote Services: Remote Desktop Protocol (4 Tests)
- **Test 1** [powershell]: RDP to Remote Host
- **Test 2** [powershell]: Changing RDP Port to Non Standard Port via Powershell
- **Test 3** [command_prompt]: Changing RDP Port to Non Standard Port via Command_Prompt
- **Test 4** [command_prompt]: Disable NLA for RDP via Command Prompt

### T1021.002: Remote Services: SMB/Windows Admin Shares (4 Tests)
- **Test 1** [command_prompt]: Map admin share
- **Test 2** [powershell]: Map Admin Share PowerShell
- **Test 3** [command_prompt]: Copy and Execute File with PsExec
- **Test 4** [command_prompt]: Execute command writing output to local Admin Share

### T1021.003: Remote Services: Distributed Component Object Model (2 Tests)
- **Test 1** [powershell]: PowerShell Lateral Movement using MMC20
- **Test 2** [powershell]: PowerShell Lateral Movement Using Excel Application Object

### T1021.006: Remote Services: Windows Remote Management (3 Tests)
- **Test 1** [powershell]: Enable Windows Remote Management
- **Test 2** [powershell]: Remote Code Execution with PS Credentials Using Invoke-Command
- **Test 3** [powershell]: WinRM Access with Evil-WinRM

### T1072: Software Deployment Tools (3 Tests)
- **Test 1** [command_prompt]: Radmin Viewer Utility
- **Test 2** [command_prompt]: PDQ Deploy RAT
- **Test 3** [powershell]: Deploy 7-Zip Using Chocolatey

### T1091: Replication Through Removable Media (1 Tests)
- **Test 1** [powershell]: USB Malware Spread Simulation

### T1550.002: Use Alternate Authentication Material: Pass the Hash (3 Tests)
- **Test 1** [command_prompt]: Mimikatz Pass the Hash
- **Test 2** [command_prompt]: crackmapexec Pass the Hash
- **Test 3** [powershell]: Invoke-WMIExec Pass the Hash

### T1550.003: Use Alternate Authentication Material: Pass the Ticket (2 Tests)
- **Test 1** [command_prompt]: Mimikatz Kerberos Ticket Attack
- **Test 2** [powershell]: Rubeus Kerberos Pass The Ticket

### T1563.002: Remote Service Session Hijacking: RDP Hijacking (1 Tests)
- **Test 1** [command_prompt]: RDP hijacking

### T1570: Lateral Tool Transfer (2 Tests)
- **Test 1** [powershell]: Exfiltration Over SMB over QUIC (New-SmbMapping)
- **Test 2** [powershell]: Exfiltration Over SMB over QUIC (NET USE)

## Persistence

### T1037.001: Boot or Logon Initialization Scripts: Logon Script (Windows) (1 Tests)
- **Test 1** [command_prompt]: Logon Scripts

### T1053.002: Scheduled Task/Job: At (1 Tests)
- **Test 1** [command_prompt]: At.exe Scheduled task

### T1053.005: Scheduled Task/Job: Scheduled Task (14 Tests)
- **Test 1** [command_prompt]: Scheduled Task Startup Script
- **Test 2** [command_prompt]: Scheduled task Local
- **Test 3** [command_prompt]: Scheduled task Remote
- **Test 4** [powershell]: Powershell Cmdlet Scheduled Task
- **Test 5** [powershell]: Task Scheduler via VBA
- **Test 6** [powershell]: WMI Invoke-CimMethod Scheduled Task
- **Test 7** [command_prompt]: Scheduled Task Executing Base64 Encoded Commands From Registry
- **Test 8** [powershell]: Import XML Schedule Task with Hidden Attribute
- **Test 9** [powershell]: PowerShell Modify A Scheduled Task
- **Test 10** [command_prompt]: Scheduled Task ("Ghost Task") via Registry Key Manipulation
- **Test 11** [command_prompt]: Scheduled Task Persistence via CompMgmt.msc
- **Test 12** [command_prompt]: Scheduled Task Persistence via Eventviewer.msc
- **Test 13** [powershell]: Turla Topinambour Dropper and Scheduled Task Persistence
- **Test 14** [command_prompt]: Turla KopiLuwak Scheduled Task for JavaScript Stager

### T1078.001: Valid Accounts: Default Accounts (2 Tests)
- **Test 1** [command_prompt]: Enable Guest account with RDP capability and admin privileges
- **Test 2** [command_prompt]: Activate Guest Account

### T1078.003: Valid Accounts: Local Accounts (4 Tests)
- **Test 1** [command_prompt]: Create local account with admin privileges
- **Test 6** [powershell]: WinPwn - Loot local Credentials - powerhell kittie
- **Test 7** [powershell]: WinPwn - Loot local Credentials - Safetykatz
- **Test 13** [command_prompt]: Use PsExec to elevate to NT Authority\SYSTEM account

### T1098: Account Manipulation (10 Tests)
- **Test 1** [powershell]: Admin Account Manipulate
- **Test 2** [powershell]: Domain Account and Group Manipulate
- **Test 9** [command_prompt]: Password Change on Directory Service Restore Mode (DSRM) Account
- **Test 10** [powershell]: Domain Password Policy Check: Short Password
- **Test 11** [powershell]: Domain Password Policy Check: No Number in Password
- **Test 12** [powershell]: Domain Password Policy Check: No Special Character in Password
- **Test 13** [powershell]: Domain Password Policy Check: No Uppercase Character in Password
- **Test 14** [powershell]: Domain Password Policy Check: No Lowercase Character in Password
- **Test 15** [powershell]: Domain Password Policy Check: Only Two Character Classes
- **Test 16** [powershell]: Domain Password Policy Check: Common Password Use

### T1112: Modify Registry (92 Tests)
- **Test 1** [command_prompt]: Modify Registry of Current User Profile - cmd
- **Test 2** [command_prompt]: Modify Registry of Local Machine - cmd
- **Test 3** [command_prompt]: Modify registry to store logon credentials
- **Test 4** [powershell]: Use Powershell to Modify registry to store logon credentials
- **Test 5** [powershell]: Add domain to Trusted sites Zone
- **Test 6** [powershell]: Javascript in registry
- **Test 7** [powershell]: Change Powershell Execution Policy to Bypass
- **Test 8** [command_prompt]: BlackByte Ransomware Registry Changes - CMD
- **Test 9** [powershell]: BlackByte Ransomware Registry Changes - Powershell
- **Test 10** [command_prompt]: Disable Windows Registry Tool
- **Test 11** [powershell]: Disable Windows CMD application
- **Test 12** [command_prompt]: Disable Windows Task Manager application
- **Test 13** [command_prompt]: Disable Windows Notification Center
- **Test 14** [command_prompt]: Disable Windows Shutdown Button
- **Test 15** [command_prompt]: Disable Windows LogOff Button
- **Test 16** [command_prompt]: Disable Windows Change Password Feature
- **Test 17** [command_prompt]: Disable Windows Lock Workstation Feature
- **Test 18** [command_prompt]: Activate Windows NoDesktop Group Policy Feature
- **Test 19** [command_prompt]: Activate Windows NoRun Group Policy Feature
- **Test 20** [command_prompt]: Activate Windows NoFind Group Policy Feature
- **Test 21** [command_prompt]: Activate Windows NoControlPanel Group Policy Feature
- **Test 22** [command_prompt]: Activate Windows NoFileMenu Group Policy Feature
- **Test 23** [command_prompt]: Activate Windows NoClose Group Policy Feature
- **Test 24** [command_prompt]: Activate Windows NoSetTaskbar Group Policy Feature
- **Test 25** [command_prompt]: Activate Windows NoTrayContextMenu Group Policy Feature
- **Test 26** [command_prompt]: Activate Windows NoPropertiesMyDocuments Group Policy Feature
- **Test 27** [command_prompt]: Hide Windows Clock Group Policy Feature
- **Test 28** [command_prompt]: Windows HideSCAHealth Group Policy Feature
- **Test 29** [command_prompt]: Windows HideSCANetwork Group Policy Feature
- **Test 30** [command_prompt]: Windows HideSCAPower Group Policy Feature
- **Test 31** [command_prompt]: Windows HideSCAVolume Group Policy Feature
- **Test 32** [command_prompt]: Windows Modify Show Compress Color And Info Tip Registry
- **Test 33** [command_prompt]: Windows Powershell Logging Disabled
- **Test 34** [command_prompt]: Windows Add Registry Value to Load Service in Safe Mode without Network
- **Test 35** [command_prompt]: Windows Add Registry Value to Load Service in Safe Mode with Network
- **Test 36** [command_prompt]: Disable Windows Toast Notifications
- **Test 37** [command_prompt]: Disable Windows Security Center Notifications
- **Test 38** [command_prompt]: Suppress Win Defender Notifications
- **Test 39** [command_prompt]: Allow RDP Remote Assistance Feature
- **Test 40** [command_prompt]: NetWire RAT Registry Key Creation
- **Test 41** [command_prompt]: Ursnif Malware Registry Key Creation
- **Test 42** [command_prompt]: Terminal Server Client Connection History Cleared
- **Test 43** [command_prompt]: Disable Windows Error Reporting Settings
- **Test 44** [command_prompt]: DisallowRun Execution Of Certain Applications
- **Test 45** [command_prompt]: Enabling Restricted Admin Mode via Command_Prompt
- **Test 46** [command_prompt]: Mimic Ransomware - Enable Multiple User Sessions
- **Test 47** [command_prompt]: Mimic Ransomware - Allow Multiple RDP Sessions per User
- **Test 48** [command_prompt]: Event Viewer Registry Modification - Redirection URL
- **Test 49** [command_prompt]: Event Viewer Registry Modification - Redirection Program
- **Test 50** [command_prompt]: Enabling Remote Desktop Protocol via Remote Registry
- **Test 51** [command_prompt]: Disable Win Defender Notification
- **Test 52** [command_prompt]: Disable Windows OS Auto Update
- **Test 53** [command_prompt]: Disable Windows Auto Reboot for current logon user
- **Test 54** [command_prompt]: Windows Auto Update Option to Notify before download
- **Test 55** [command_prompt]: Do Not Connect To Win Update
- **Test 56** [command_prompt]: Tamper Win Defender Protection
- **Test 57** [powershell]: Snake Malware Registry Blob
- **Test 58** [command_prompt]: Allow Simultaneous Download Registry
- **Test 59** [command_prompt]: Modify Internet Zone Protocol Defaults in Current User Registry - cmd
- **Test 60** [powershell]: Modify Internet Zone Protocol Defaults in Current User Registry - PowerShell
- **Test 61** [command_prompt]: Activities To Disable Secondary Authentication Detected By Modified Registry Value.
- **Test 62** [command_prompt]: Activities To Disable Microsoft [FIDO Aka Fast IDentity Online] Authentication Detected By Modified Registry Value.
- **Test 63** [command_prompt]: Scarab Ransomware Defense Evasion Activities
- **Test 64** [command_prompt]: Disable Remote Desktop Anti-Alias Setting Through Registry
- **Test 65** [command_prompt]: Disable Remote Desktop Security Settings Through Registry
- **Test 66** [command_prompt]: Disabling ShowUI Settings of Windows Error Reporting (WER)
- **Test 67** [command_prompt]: Enable Proxy Settings
- **Test 68** [command_prompt]: Set-Up Proxy Server
- **Test 69** [command_prompt]: RDP Authentication Level Override
- **Test 70** [command_prompt]: Enable RDP via Registry (fDenyTSConnections)
- **Test 71** [command_prompt]: Disable Windows Prefetch Through Registry
- **Test 72** [powershell]: Setting Shadow key in Registry for RDP Shadowing
- **Test 73** [command_prompt]: Flush Shimcache
- **Test 74** [command_prompt]: Disable Windows Remote Desktop Protocol
- **Test 75** [command_prompt]: Enforce Smart Card Authentication Through Registry
- **Test 76** [command_prompt]: Requires the BitLocker PIN for Pre-boot authentication
- **Test 77** [command_prompt]: Modify EnableBDEWithNoTPM Registry entry
- **Test 78** [command_prompt]: Modify UseTPM Registry entry
- **Test 79** [command_prompt]: Modify UseTPMPIN Registry entry
- **Test 80** [command_prompt]: Modify UseTPMKey Registry entry
- **Test 81** [command_prompt]: Modify UseTPMKeyPIN Registry entry
- **Test 82** [command_prompt]: Modify EnableNonTPM Registry entry
- **Test 83** [command_prompt]: Modify UsePartialEncryptionKey Registry entry
- **Test 84** [command_prompt]: Modify UsePIN Registry entry
- **Test 85** [command_prompt]: Abusing Windows TelemetryController Registry Key for Persistence
- **Test 86** [command_prompt]: Modify RDP-Tcp Initial Program Registry Entry
- **Test 87** [command_prompt]: Abusing MyComputer Disk Cleanup Path for Persistence
- **Test 88** [command_prompt]: Abusing MyComputer Disk Fragmentation Path for Persistence
- **Test 89** [command_prompt]: Abusing MyComputer Disk Backup Path for Persistence
- **Test 90** [command_prompt]: Adding custom paths for application execution
- **Test 91** [powershell]: Turla Mosquito - Store Backdoor Path in OneDriveUpdate Registry Key
- **Test 92** [powershell]: Disable UAC remote restrictions via LocalAccountTokenFilterPolicy

### T1133: External Remote Services (1 Tests)
- **Test 1** [powershell]: Running Chrome VPN Extensions via the Registry 2 vpn extension

### T1136.001: Create Account: Local Account (4 Tests)
- **Test 4** [command_prompt]: Create a new user in a command prompt
- **Test 5** [powershell]: Create a new user in PowerShell
- **Test 8** [command_prompt]: Create a new Windows admin user
- **Test 9** [powershell]: Create a new Windows admin user via .NET

### T1136.002: Create Account: Domain Account (3 Tests)
- **Test 1** [command_prompt]: Create a new Windows domain admin user
- **Test 2** [command_prompt]: Create a new account similar to ANONYMOUS LOGON
- **Test 3** [powershell]: Create a new Domain Account using PowerShell

### T1137: Office Application Startup (1 Tests)
- **Test 1** [command_prompt]: Office Application Startup - Outlook as a C2

### T1137.001: Office Application Startup: Office Template Macros. (1 Tests)
- **Test 1** [powershell]: Injecting a Macro into the Word Normal.dotm Template for Persistence via PowerShell

### T1137.002: Office Application Startup: Office Test (1 Tests)
- **Test 1** [powershell]: Office Application Startup Test Persistence (HKCU)

### T1137.004: Office Application Startup: Outlook Home Page (1 Tests)
- **Test 1** [command_prompt]: Install Outlook Home Page Persistence

### T1137.005: Office Application Startup: Outlook Rules (5 Tests)
- **Test 1** [powershell]: Outlook Rule - Subject Trigger with DeletePermanently Action via COM Object
- **Test 2** [powershell]: Outlook Rule - Sender Address Trigger with DeletePermanently Action via COM Object
- **Test 3** [powershell]: Outlook Rule - Auto-Forward Emails to External Address via COM Object
- **Test 4** [powershell]: Outlook Rules - Enumerate Existing Rules via PowerShell COM Object
- **Test 5** [powershell]: Outlook Rule - Create Rule with Obfuscated Blank Name (MAPI Evasion)

### T1137.006: Office Application Startup: Add-ins (5 Tests)
- **Test 1** [powershell]: Code Executed Via Excel Add-in File (XLL)
- **Test 2** [powershell]: Persistent Code Execution Via Excel Add-in File (XLL)
- **Test 3** [powershell]: Persistent Code Execution Via Word Add-in File (WLL)
- **Test 4** [powershell]: Persistent Code Execution Via Excel VBA Add-in File (XLAM)
- **Test 5** [powershell]: Persistent Code Execution Via PowerPoint VBA Add-in File (PPAM)

### T1176: Browser Extensions (4 Tests)
- **Test 1** [manual]: Chrome/Chromium (Developer Mode)
- **Test 2** [manual]: Firefox
- **Test 3** [manual]: Edge Chromium Addon - VPN
- **Test 4** [powershell]: Google Chrome Load Unpacked Extension With Command Line

### T1197: BITS Jobs (4 Tests)
- **Test 1** [command_prompt]: Bitsadmin Download (cmd)
- **Test 2** [powershell]: Bitsadmin Download (PowerShell)
- **Test 3** [command_prompt]: Persist, Download, & Execute
- **Test 4** [command_prompt]: Bits download using desktopimgdownldr.exe (cmd)

### T1505.002: Server Software Component: Transport Agent (1 Tests)
- **Test 1** [powershell]: Install MS Exchange Transport Agent Persistence

### T1505.003: Server Software Component: Web Shell (1 Tests)
- **Test 1** [command_prompt]: Web Shell Written to Disk

### T1505.004: IIS Components (2 Tests)
- **Test 1** [command_prompt]: Install IIS Module using AppCmd.exe
- **Test 2** [powershell]: Install IIS Module using PowerShell Cmdlet New-WebGlobalModule

### T1505.005: Server Software Component: Terminal Services DLL (2 Tests)
- **Test 1** [powershell]: Simulate Patching termsrv.dll
- **Test 2** [powershell]: Modify Terminal Services DLL Path

### T1542.001: Pre-OS Boot: System Firmware (1 Tests)
- **Test 1** [powershell]: UEFI Persistence via Wpbbin.exe File Creation

### T1543.003: Create or Modify System Process: Windows Service (6 Tests)
- **Test 1** [command_prompt]: Modify Fax service to run PowerShell
- **Test 2** [command_prompt]: Service Installation CMD
- **Test 3** [powershell]: Service Installation PowerShell
- **Test 4** [command_prompt]: TinyTurla backdoor service w64time
- **Test 5** [command_prompt]: Remote Service Installation CMD
- **Test 6** [powershell]: Modify Service to Run Arbitrary Binary (Powershell)

### T1546: Event Triggered Execution (9 Tests)
- **Test 1** [powershell]: Persistence with Custom AutodialDLL
- **Test 2** [powershell]: HKLM - Persistence using CommandProcessor AutoRun key (With Elevation)
- **Test 3** [powershell]: HKCU - Persistence using CommandProcessor AutoRun key (Without Elevation)
- **Test 4** [powershell]: WMI Invoke-CimMethod Start Process
- **Test 5** [command_prompt]: Adding custom debugger for Windows Error Reporting
- **Test 6** [command_prompt]: Load custom DLL on mstsc execution
- **Test 7** [command_prompt]: Persistence using automatic execution of custom DLL during RDP session
- **Test 8** [powershell]: Persistence via ErrorHandler.cmd script execution
- **Test 9** [command_prompt]: Persistence using STARTUP-PATH in MS-WORD

### T1546.001: Event Triggered Execution: Change Default File Association (1 Tests)
- **Test 1** [command_prompt]: Change Default File Association

### T1546.002: Event Triggered Execution: Screensaver (1 Tests)
- **Test 1** [command_prompt]: Set Arbitrary Binary as Screensaver

### T1546.003: Event Triggered Execution: Windows Management Instrumentation Event Subscription (4 Tests)
- **Test 1** [powershell]: Persistence via WMI Event Subscription - CommandLineEventConsumer
- **Test 2** [powershell]: Persistence via WMI Event Subscription - ActiveScriptEventConsumer
- **Test 3** [powershell]: Windows MOFComp.exe Load MOF File
- **Test 4** [powershell]: Turla WMI Persistence - Dual Filter with Base64 Payload

### T1546.007: Event Triggered Execution: Netsh Helper DLL (1 Tests)
- **Test 1** [command_prompt]: Netsh Helper DLL Registration

### T1546.008: Event Triggered Execution: Accessibility Features (10 Tests)
- **Test 1** [powershell]: Attaches Command Prompt as a Debugger to a List of Target Processes
- **Test 2** [command_prompt]: Replace binary of sticky keys
- **Test 3** [command_prompt]: Create Symbolic Link From osk.exe to cmd.exe
- **Test 4** [command_prompt]: Atbroker.exe (AT) Executes Arbitrary Command via Registry Key
- **Test 5** [command_prompt]: Auto-start application on user logon
- **Test 6** [command_prompt]: Replace utilman.exe (Ease of Access Binary) with cmd.exe
- **Test 7** [command_prompt]: Replace Magnify.exe (Magnifier binary) with cmd.exe
- **Test 8** [command_prompt]: Replace Narrator.exe (Narrator binary) with cmd.exe
- **Test 9** [command_prompt]: Replace DisplaySwitch.exe (Display Switcher binary) with cmd.exe
- **Test 10** [command_prompt]: Replace AtBroker.exe (App Switcher binary) with cmd.exe

### T1546.009: Event Triggered Execution: AppCert DLLs (1 Tests)
- **Test 1** [powershell]: Create registry persistence via AppCert DLL

### T1546.010: Event Triggered Execution: AppInit DLLs (1 Tests)
- **Test 1** [command_prompt]: Install AppInit Shim

### T1546.011: Event Triggered Execution: Application Shimming (3 Tests)
- **Test 1** [command_prompt]: Application Shim Installation
- **Test 2** [powershell]: New shim database files created in the default shim database directory
- **Test 3** [powershell]: Registry key creation and/or modification events for SDB

### T1546.012: Event Triggered Execution: Image File Execution Options Injection (3 Tests)
- **Test 1** [command_prompt]: IFEO Add Debugger
- **Test 2** [command_prompt]: IFEO Global Flags
- **Test 3** [powershell]: GlobalFlags in Image File Execution Options

### T1546.013: Event Triggered Execution: PowerShell Profile (2 Tests)
- **Test 1** [powershell]: Append malicious start-process cmdlet
- **Test 2** [powershell]: Turla Malicious Powershell Profile for Persistence

### T1546.015: Event Triggered Execution: Component Object Model Hijacking (4 Tests)
- **Test 1** [powershell]: COM Hijacking - InprocServer32
- **Test 2** [powershell]: Powershell Execute COM Object
- **Test 3** [powershell]: COM Hijacking with RunDLL32 (Local Server Switch)
- **Test 4** [powershell]: COM hijacking via TreatAs

### T1546.018: Event Triggered Execution: Python Startup Hooks (2 Tests)
- **Test 1** [powershell]: Python Startup Hook - atomic_hook.pth (Windows)
- **Test 2** [powershell]: Python Startup Hook - usercustomize.py (Windows)

### T1547: Boot or Logon Autostart Execution (3 Tests)
- **Test 1** [command_prompt]: Add a driver
- **Test 2** [powershell]: Driver Installation Using pnputil.exe
- **Test 3** [command_prompt]: Leverage Virtual Channels to execute custom DLL during successful RDP session

### T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (21 Tests)
- **Test 1** [command_prompt]: Reg Key Run
- **Test 2** [command_prompt]: Reg Key RunOnce
- **Test 3** [powershell]: PowerShell Registry RunOnce
- **Test 4** [powershell]: Suspicious vbs file run from startup Folder
- **Test 5** [powershell]: Suspicious jse file run from startup Folder
- **Test 6** [powershell]: Suspicious bat file run from startup Folder
- **Test 7** [powershell]: Add Executable Shortcut Link to User Startup Folder
- **Test 8** [command_prompt]: Add persistance via Recycle bin
- **Test 9** [powershell]: SystemBC Malware-as-a-Service Registry
- **Test 10** [powershell]: Change Startup Folder - HKLM Modify User Shell Folders Common Startup Value
- **Test 11** [powershell]: Change Startup Folder - HKCU Modify User Shell Folders Startup Value
- **Test 12** [powershell]: HKCU - Policy Settings Explorer Run Key
- **Test 13** [powershell]: HKLM - Policy Settings Explorer Run Key
- **Test 14** [powershell]: HKLM - Append Command to Winlogon Userinit KEY Value
- **Test 15** [powershell]: HKLM - Modify default System Shell - Winlogon Shell KEY Value
- **Test 16** [command_prompt]: secedit used to create a Run key in the HKLM Hive
- **Test 17** [powershell]: Modify BootExecute Value
- **Test 18** [command_prompt]: Allowing custom application to execute during new RDP logon session
- **Test 19** [command_prompt]: Creating Boot Verification Program Key for application execution during successful boot
- **Test 20** [command_prompt]: Add persistence via Windows Context Menu
- **Test 21** [powershell]: Turla Mosquito Run Key Persistence via rundll32 DLL Export

### T1547.002: Authentication Package (1 Tests)
- **Test 1** [powershell]: Authentication Package

### T1547.003: Time Providers (2 Tests)
- **Test 1** [powershell]: Create a new time provider
- **Test 2** [powershell]: Edit an existing time provider

### T1547.004: Boot or Logon Autostart Execution: Winlogon Helper DLL (5 Tests)
- **Test 1** [powershell]: Winlogon Shell Key Persistence - PowerShell
- **Test 2** [powershell]: Winlogon Userinit Key Persistence - PowerShell
- **Test 3** [powershell]: Winlogon Notify Key Logon Persistence - PowerShell
- **Test 4** [powershell]: Winlogon HKLM Shell Key Persistence - PowerShell
- **Test 5** [powershell]: Winlogon HKLM Userinit Key Persistence - PowerShell

### T1547.005: Boot or Logon Autostart Execution: Security Support Provider (2 Tests)
- **Test 1** [powershell]: Modify HKLM:\System\CurrentControlSet\Control\Lsa Security Support Provider configuration in registry
- **Test 2** [powershell]: Modify HKLM:\System\CurrentControlSet\Control\Lsa\OSConfig Security Support Provider configuration in registry

### T1547.008: Boot or Logon Autostart Execution: LSASS Driver (1 Tests)
- **Test 1** [powershell]: Modify Registry to load Arbitrary DLL into LSASS - LsaDbExtPt

### T1547.009: Boot or Logon Autostart Execution: Shortcut Modification (2 Tests)
- **Test 1** [command_prompt]: Shortcut Modification
- **Test 2** [powershell]: Create shortcut to cmd in startup folders

### T1547.010: Boot or Logon Autostart Execution: Port Monitors (1 Tests)
- **Test 1** [command_prompt]: Add Port Monitor persistence in Registry

### T1547.012: Boot or Logon Autostart Execution: Print Processors (1 Tests)
- **Test 1** [powershell]: Print Processors

### T1547.014: Active Setup (3 Tests)
- **Test 1** [powershell]: HKLM - Add atomic_test key to launch executable as part of user setup
- **Test 2** [powershell]: HKLM - Add malicious StubPath value to existing Active Setup Entry
- **Test 3** [powershell]: HKLM - re-execute 'Internet Explorer Core Fonts' StubPath payload by decreasing version number

### T1556.001: Modify Authentication Process: Domain Controller Authentication (1 Tests)
- **Test 1** [powershell]: Skeleton Key via Mimikatz

### T1556.002: Modify Authentication Process: Password Filter DLL (2 Tests)
- **Test 1** [powershell]: Install and Register Password Filter DLL
- **Test 2** [powershell]: Install Additional Authentication Packages

## Privilege Escalation

### T1037.001: Boot or Logon Initialization Scripts: Logon Script (Windows) (1 Tests)
- **Test 1** [command_prompt]: Logon Scripts

### T1053.002: Scheduled Task/Job: At (1 Tests)
- **Test 1** [command_prompt]: At.exe Scheduled task

### T1053.005: Scheduled Task/Job: Scheduled Task (14 Tests)
- **Test 1** [command_prompt]: Scheduled Task Startup Script
- **Test 2** [command_prompt]: Scheduled task Local
- **Test 3** [command_prompt]: Scheduled task Remote
- **Test 4** [powershell]: Powershell Cmdlet Scheduled Task
- **Test 5** [powershell]: Task Scheduler via VBA
- **Test 6** [powershell]: WMI Invoke-CimMethod Scheduled Task
- **Test 7** [command_prompt]: Scheduled Task Executing Base64 Encoded Commands From Registry
- **Test 8** [powershell]: Import XML Schedule Task with Hidden Attribute
- **Test 9** [powershell]: PowerShell Modify A Scheduled Task
- **Test 10** [command_prompt]: Scheduled Task ("Ghost Task") via Registry Key Manipulation
- **Test 11** [command_prompt]: Scheduled Task Persistence via CompMgmt.msc
- **Test 12** [command_prompt]: Scheduled Task Persistence via Eventviewer.msc
- **Test 13** [powershell]: Turla Topinambour Dropper and Scheduled Task Persistence
- **Test 14** [command_prompt]: Turla KopiLuwak Scheduled Task for JavaScript Stager

### T1055: Process Injection (13 Tests)
- **Test 1** [powershell]: Shellcode execution via VBA
- **Test 2** [command_prompt]: Remote Process Injection in LSASS via mimikatz
- **Test 3** [powershell]: Section View Injection
- **Test 4** [powershell]: Dirty Vanity process Injection
- **Test 5** [powershell]: Read-Write-Execute process Injection
- **Test 6** [powershell]: Process Injection with Go using UuidFromStringA WinAPI
- **Test 7** [powershell]: Process Injection with Go using EtwpCreateEtwThread WinAPI
- **Test 8** [powershell]: Remote Process Injection with Go using RtlCreateUserThread WinAPI
- **Test 9** [powershell]: Remote Process Injection with Go using CreateRemoteThread WinAPI
- **Test 10** [powershell]: Remote Process Injection with Go using CreateRemoteThread WinAPI (Natively)
- **Test 11** [powershell]: Process Injection with Go using CreateThread WinAPI
- **Test 12** [powershell]: Process Injection with Go using CreateThread WinAPI (Natively)
- **Test 13** [powershell]: UUID custom process Injection

### T1055.001: Process Injection: Dynamic-link Library Injection (2 Tests)
- **Test 1** [powershell]: Process Injection via mavinject.exe
- **Test 2** [powershell]: WinPwn - Get SYSTEM shell - Bind System Shell using UsoClient DLL load technique

### T1055.002: Process Injection: Portable Executable Injection (1 Tests)
- **Test 1** [powershell]: Portable Executable Injection

### T1055.003: Thread Execution Hijacking (1 Tests)
- **Test 1** [powershell]: Thread Execution Hijacking

### T1055.004: Process Injection: Asynchronous Procedure Call (3 Tests)
- **Test 1** [command_prompt]: Process Injection via C#
- **Test 2** [powershell]: EarlyBird APC Queue Injection in Go
- **Test 3** [powershell]: Remote Process Injection with Go using NtQueueApcThreadEx WinAPI

### T1055.011: Process Injection: Extra Window Memory Injection (1 Tests)
- **Test 1** [powershell]: Process Injection via Extra Window Memory (EWM) x64 executable

### T1055.012: Process Injection: Process Hollowing (4 Tests)
- **Test 1** [powershell]: Process Hollowing using PowerShell
- **Test 2** [powershell]: RunPE via VBA
- **Test 3** [powershell]: Process Hollowing in Go using CreateProcessW WinAPI
- **Test 4** [powershell]: Process Hollowing in Go using CreateProcessW and CreatePipe WinAPIs (T1055.012)

### T1055.015: Process Injection: ListPlanting (1 Tests)
- **Test 1** [powershell]: Process injection ListPlanting

### T1068: Exploitation for Privilege Escalation (2 Tests)
- **Test 1** [powershell]: Scattered Spider BYOVD (CVE-2015-2291 for Intel Ethernet Diagnostics Driver)
- **Test 2** [powershell]: Turla Snake Malware Privilege Escalation Through VM Driver

### T1078.001: Valid Accounts: Default Accounts (2 Tests)
- **Test 1** [command_prompt]: Enable Guest account with RDP capability and admin privileges
- **Test 2** [command_prompt]: Activate Guest Account

### T1078.003: Valid Accounts: Local Accounts (4 Tests)
- **Test 1** [command_prompt]: Create local account with admin privileges
- **Test 6** [powershell]: WinPwn - Loot local Credentials - powerhell kittie
- **Test 7** [powershell]: WinPwn - Loot local Credentials - Safetykatz
- **Test 13** [command_prompt]: Use PsExec to elevate to NT Authority\SYSTEM account

### T1098: Account Manipulation (10 Tests)
- **Test 1** [powershell]: Admin Account Manipulate
- **Test 2** [powershell]: Domain Account and Group Manipulate
- **Test 9** [command_prompt]: Password Change on Directory Service Restore Mode (DSRM) Account
- **Test 10** [powershell]: Domain Password Policy Check: Short Password
- **Test 11** [powershell]: Domain Password Policy Check: No Number in Password
- **Test 12** [powershell]: Domain Password Policy Check: No Special Character in Password
- **Test 13** [powershell]: Domain Password Policy Check: No Uppercase Character in Password
- **Test 14** [powershell]: Domain Password Policy Check: No Lowercase Character in Password
- **Test 15** [powershell]: Domain Password Policy Check: Only Two Character Classes
- **Test 16** [powershell]: Domain Password Policy Check: Common Password Use

### T1134.001: Access Token Manipulation: Token Impersonation/Theft (5 Tests)
- **Test 1** [powershell]: Named pipe client impersonation
- **Test 2** [powershell]: `SeDebugPrivilege` token duplication
- **Test 3** [powershell]: Launch NSudo Executable
- **Test 4** [powershell]: Bad Potato
- **Test 5** [powershell]: Juicy Potato

### T1134.002: Create Process with Token (2 Tests)
- **Test 1** [powershell]: Access Token Manipulation
- **Test 2** [powershell]: WinPwn - Get SYSTEM shell - Pop System Shell using Token Manipulation technique

### T1134.004: Access Token Manipulation: Parent PID Spoofing (5 Tests)
- **Test 1** [powershell]: Parent PID Spoofing using PowerShell
- **Test 2** [powershell]: Parent PID Spoofing - Spawn from Current Process
- **Test 3** [powershell]: Parent PID Spoofing - Spawn from Specified Process
- **Test 4** [powershell]: Parent PID Spoofing - Spawn from svchost.exe
- **Test 5** [powershell]: Parent PID Spoofing - Spawn from New Process

### T1134.005: Access Token Manipulation: SID-History Injection (1 Tests)
- **Test 1** [command_prompt]: Injection SID-History with mimikatz

### T1484.001: Domain Policy Modification: Group Policy Modification (2 Tests)
- **Test 1** [command_prompt]: LockBit Black - Modify Group policy settings -cmd
- **Test 2** [powershell]: LockBit Black - Modify Group policy settings -Powershell

### T1543.003: Create or Modify System Process: Windows Service (6 Tests)
- **Test 1** [command_prompt]: Modify Fax service to run PowerShell
- **Test 2** [command_prompt]: Service Installation CMD
- **Test 3** [powershell]: Service Installation PowerShell
- **Test 4** [command_prompt]: TinyTurla backdoor service w64time
- **Test 5** [command_prompt]: Remote Service Installation CMD
- **Test 6** [powershell]: Modify Service to Run Arbitrary Binary (Powershell)

### T1546: Event Triggered Execution (9 Tests)
- **Test 1** [powershell]: Persistence with Custom AutodialDLL
- **Test 2** [powershell]: HKLM - Persistence using CommandProcessor AutoRun key (With Elevation)
- **Test 3** [powershell]: HKCU - Persistence using CommandProcessor AutoRun key (Without Elevation)
- **Test 4** [powershell]: WMI Invoke-CimMethod Start Process
- **Test 5** [command_prompt]: Adding custom debugger for Windows Error Reporting
- **Test 6** [command_prompt]: Load custom DLL on mstsc execution
- **Test 7** [command_prompt]: Persistence using automatic execution of custom DLL during RDP session
- **Test 8** [powershell]: Persistence via ErrorHandler.cmd script execution
- **Test 9** [command_prompt]: Persistence using STARTUP-PATH in MS-WORD

### T1546.001: Event Triggered Execution: Change Default File Association (1 Tests)
- **Test 1** [command_prompt]: Change Default File Association

### T1546.002: Event Triggered Execution: Screensaver (1 Tests)
- **Test 1** [command_prompt]: Set Arbitrary Binary as Screensaver

### T1546.003: Event Triggered Execution: Windows Management Instrumentation Event Subscription (4 Tests)
- **Test 1** [powershell]: Persistence via WMI Event Subscription - CommandLineEventConsumer
- **Test 2** [powershell]: Persistence via WMI Event Subscription - ActiveScriptEventConsumer
- **Test 3** [powershell]: Windows MOFComp.exe Load MOF File
- **Test 4** [powershell]: Turla WMI Persistence - Dual Filter with Base64 Payload

### T1546.007: Event Triggered Execution: Netsh Helper DLL (1 Tests)
- **Test 1** [command_prompt]: Netsh Helper DLL Registration

### T1546.008: Event Triggered Execution: Accessibility Features (10 Tests)
- **Test 1** [powershell]: Attaches Command Prompt as a Debugger to a List of Target Processes
- **Test 2** [command_prompt]: Replace binary of sticky keys
- **Test 3** [command_prompt]: Create Symbolic Link From osk.exe to cmd.exe
- **Test 4** [command_prompt]: Atbroker.exe (AT) Executes Arbitrary Command via Registry Key
- **Test 5** [command_prompt]: Auto-start application on user logon
- **Test 6** [command_prompt]: Replace utilman.exe (Ease of Access Binary) with cmd.exe
- **Test 7** [command_prompt]: Replace Magnify.exe (Magnifier binary) with cmd.exe
- **Test 8** [command_prompt]: Replace Narrator.exe (Narrator binary) with cmd.exe
- **Test 9** [command_prompt]: Replace DisplaySwitch.exe (Display Switcher binary) with cmd.exe
- **Test 10** [command_prompt]: Replace AtBroker.exe (App Switcher binary) with cmd.exe

### T1546.009: Event Triggered Execution: AppCert DLLs (1 Tests)
- **Test 1** [powershell]: Create registry persistence via AppCert DLL

### T1546.010: Event Triggered Execution: AppInit DLLs (1 Tests)
- **Test 1** [command_prompt]: Install AppInit Shim

### T1546.011: Event Triggered Execution: Application Shimming (3 Tests)
- **Test 1** [command_prompt]: Application Shim Installation
- **Test 2** [powershell]: New shim database files created in the default shim database directory
- **Test 3** [powershell]: Registry key creation and/or modification events for SDB

### T1546.012: Event Triggered Execution: Image File Execution Options Injection (3 Tests)
- **Test 1** [command_prompt]: IFEO Add Debugger
- **Test 2** [command_prompt]: IFEO Global Flags
- **Test 3** [powershell]: GlobalFlags in Image File Execution Options

### T1546.013: Event Triggered Execution: PowerShell Profile (2 Tests)
- **Test 1** [powershell]: Append malicious start-process cmdlet
- **Test 2** [powershell]: Turla Malicious Powershell Profile for Persistence

### T1546.015: Event Triggered Execution: Component Object Model Hijacking (4 Tests)
- **Test 1** [powershell]: COM Hijacking - InprocServer32
- **Test 2** [powershell]: Powershell Execute COM Object
- **Test 3** [powershell]: COM Hijacking with RunDLL32 (Local Server Switch)
- **Test 4** [powershell]: COM hijacking via TreatAs

### T1546.018: Event Triggered Execution: Python Startup Hooks (2 Tests)
- **Test 1** [powershell]: Python Startup Hook - atomic_hook.pth (Windows)
- **Test 2** [powershell]: Python Startup Hook - usercustomize.py (Windows)

### T1547: Boot or Logon Autostart Execution (3 Tests)
- **Test 1** [command_prompt]: Add a driver
- **Test 2** [powershell]: Driver Installation Using pnputil.exe
- **Test 3** [command_prompt]: Leverage Virtual Channels to execute custom DLL during successful RDP session

### T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (21 Tests)
- **Test 1** [command_prompt]: Reg Key Run
- **Test 2** [command_prompt]: Reg Key RunOnce
- **Test 3** [powershell]: PowerShell Registry RunOnce
- **Test 4** [powershell]: Suspicious vbs file run from startup Folder
- **Test 5** [powershell]: Suspicious jse file run from startup Folder
- **Test 6** [powershell]: Suspicious bat file run from startup Folder
- **Test 7** [powershell]: Add Executable Shortcut Link to User Startup Folder
- **Test 8** [command_prompt]: Add persistance via Recycle bin
- **Test 9** [powershell]: SystemBC Malware-as-a-Service Registry
- **Test 10** [powershell]: Change Startup Folder - HKLM Modify User Shell Folders Common Startup Value
- **Test 11** [powershell]: Change Startup Folder - HKCU Modify User Shell Folders Startup Value
- **Test 12** [powershell]: HKCU - Policy Settings Explorer Run Key
- **Test 13** [powershell]: HKLM - Policy Settings Explorer Run Key
- **Test 14** [powershell]: HKLM - Append Command to Winlogon Userinit KEY Value
- **Test 15** [powershell]: HKLM - Modify default System Shell - Winlogon Shell KEY Value
- **Test 16** [command_prompt]: secedit used to create a Run key in the HKLM Hive
- **Test 17** [powershell]: Modify BootExecute Value
- **Test 18** [command_prompt]: Allowing custom application to execute during new RDP logon session
- **Test 19** [command_prompt]: Creating Boot Verification Program Key for application execution during successful boot
- **Test 20** [command_prompt]: Add persistence via Windows Context Menu
- **Test 21** [powershell]: Turla Mosquito Run Key Persistence via rundll32 DLL Export

### T1547.002: Authentication Package (1 Tests)
- **Test 1** [powershell]: Authentication Package

### T1547.003: Time Providers (2 Tests)
- **Test 1** [powershell]: Create a new time provider
- **Test 2** [powershell]: Edit an existing time provider

### T1547.004: Boot or Logon Autostart Execution: Winlogon Helper DLL (5 Tests)
- **Test 1** [powershell]: Winlogon Shell Key Persistence - PowerShell
- **Test 2** [powershell]: Winlogon Userinit Key Persistence - PowerShell
- **Test 3** [powershell]: Winlogon Notify Key Logon Persistence - PowerShell
- **Test 4** [powershell]: Winlogon HKLM Shell Key Persistence - PowerShell
- **Test 5** [powershell]: Winlogon HKLM Userinit Key Persistence - PowerShell

### T1547.005: Boot or Logon Autostart Execution: Security Support Provider (2 Tests)
- **Test 1** [powershell]: Modify HKLM:\System\CurrentControlSet\Control\Lsa Security Support Provider configuration in registry
- **Test 2** [powershell]: Modify HKLM:\System\CurrentControlSet\Control\Lsa\OSConfig Security Support Provider configuration in registry

### T1547.008: Boot or Logon Autostart Execution: LSASS Driver (1 Tests)
- **Test 1** [powershell]: Modify Registry to load Arbitrary DLL into LSASS - LsaDbExtPt

### T1547.009: Boot or Logon Autostart Execution: Shortcut Modification (2 Tests)
- **Test 1** [command_prompt]: Shortcut Modification
- **Test 2** [powershell]: Create shortcut to cmd in startup folders

### T1547.010: Boot or Logon Autostart Execution: Port Monitors (1 Tests)
- **Test 1** [command_prompt]: Add Port Monitor persistence in Registry

### T1547.012: Boot or Logon Autostart Execution: Print Processors (1 Tests)
- **Test 1** [powershell]: Print Processors

### T1547.014: Active Setup (3 Tests)
- **Test 1** [powershell]: HKLM - Add atomic_test key to launch executable as part of user setup
- **Test 2** [powershell]: HKLM - Add malicious StubPath value to existing Active Setup Entry
- **Test 3** [powershell]: HKLM - re-execute 'Internet Explorer Core Fonts' StubPath payload by decreasing version number

### T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control (28 Tests)
- **Test 1** [command_prompt]: Bypass UAC using Event Viewer (cmd)
- **Test 2** [powershell]: Bypass UAC using Event Viewer (PowerShell)
- **Test 3** [command_prompt]: Bypass UAC using Fodhelper
- **Test 4** [powershell]: Bypass UAC using Fodhelper - PowerShell
- **Test 5** [powershell]: Bypass UAC using ComputerDefaults (PowerShell)
- **Test 6** [command_prompt]: Bypass UAC by Mocking Trusted Directories
- **Test 7** [powershell]: Bypass UAC using sdclt DelegateExecute
- **Test 8** [command_prompt]: Disable UAC using reg.exe
- **Test 9** [command_prompt]: Bypass UAC using SilentCleanup task
- **Test 10** [command_prompt]: UACME Bypass Method 23
- **Test 11** [command_prompt]: UACME Bypass Method 31
- **Test 12** [command_prompt]: UACME Bypass Method 33
- **Test 13** [command_prompt]: UACME Bypass Method 34
- **Test 14** [command_prompt]: UACME Bypass Method 39
- **Test 15** [command_prompt]: UACME Bypass Method 56
- **Test 16** [command_prompt]: UACME Bypass Method 59
- **Test 17** [command_prompt]: UACME Bypass Method 61
- **Test 18** [powershell]: WinPwn - UAC Magic
- **Test 19** [powershell]: WinPwn - UAC Bypass ccmstp technique
- **Test 20** [powershell]: WinPwn - UAC Bypass DiskCleanup technique
- **Test 21** [powershell]: WinPwn - UAC Bypass DccwBypassUAC technique
- **Test 22** [powershell]: Disable UAC admin consent prompt via ConsentPromptBehaviorAdmin registry key
- **Test 23** [powershell]: UAC Bypass with WSReset Registry Modification
- **Test 24** [powershell]: Disable UAC - Switch to the secure desktop when prompting for elevation via registry key
- **Test 25** [command_prompt]: Disable UAC notification via registry keys
- **Test 26** [command_prompt]: Disable ConsentPromptBehaviorAdmin via registry keys
- **Test 27** [command_prompt]: UAC bypassed by Utilizing ProgIDs registry.
- **Test 28** [powershell]: Warzone/AveMaria RAT style UAC bypass

## Stealth

### T1006: Direct Volume Access (1 Tests)
- **Test 1** [powershell]: Read volume boot sector via DOS device path (PowerShell)

### T1027: Obfuscated Files or Information (10 Tests)
- **Test 2** [powershell]: Execute base64-encoded PowerShell
- **Test 3** [powershell]: Execute base64-encoded PowerShell from Windows Registry
- **Test 4** [command_prompt]: Execution from Compressed File
- **Test 5** [powershell]: DLP Evasion via Sensitive Data in VBA Macro over email
- **Test 6** [powershell]: DLP Evasion via Sensitive Data in VBA Macro over HTTP
- **Test 7** [powershell]: Obfuscated Command in PowerShell
- **Test 8** [manual]: Obfuscated Command Line using special Unicode characters
- **Test 9** [powershell]: Snake Malware Encrypted crmlog file
- **Test 10** [command_prompt]: Execution from Compressed JScript File
- **Test 11** [powershell]: Obfuscated PowerShell Command via Character Array

### T1027.004: Obfuscated Files or Information: Compile After Delivery (2 Tests)
- **Test 1** [command_prompt]: Compile After Delivery using csc.exe
- **Test 2** [powershell]: Dynamic C# Compile

### T1027.006: HTML Smuggling (1 Tests)
- **Test 1** [powershell]: HTML Smuggling Remote Payload

### T1027.007: Obfuscated Files or Information: Dynamic API Resolution (1 Tests)
- **Test 1** [powershell]: Dynamic API Resolution-Ninja-syscall

### T1027.013: Obfuscated Files or Information: Encrypted/Encoded File (3 Tests)
- **Test 1** [powershell]: Decode Eicar File and Write to File
- **Test 2** [powershell]: Decrypt Eicar File and Write to File
- **Test 4** [powershell]: Turla Snake Queue File Artifact

### T1027.018: Obfuscated Files or Information: Invisible Unicode (3 Tests)
- **Test 1** [powershell]: File Masquerading with Zero-Width Space
- **Test 2** [powershell]: Invisible Unicode in Environment Variables
- **Test 3** [powershell]: Binary Masquerading via Invisible Unicode

### T1036: Masquerading (2 Tests)
- **Test 1** [powershell]: System File Copied to Unusual Location
- **Test 2** [powershell]: Malware Masquerading and Execution from Zip File

### T1036.002: Masquerading:Right-to-Left Override (2 Tests)
- **Test 1** [powershell]: Masquerading: Right-to-Left Override Batch File Creation and Execution
- **Test 2** [powershell]: Masquerading: RTLO Masqueraded File Download and Execution

### T1036.003: Masquerading: Rename System Utilities (7 Tests)
- **Test 1** [command_prompt]: Masquerading as Windows LSASS process
- **Test 3** [command_prompt]: Masquerading - cscript.exe running as notepad.exe
- **Test 4** [command_prompt]: Masquerading - wscript.exe running as svchost.exe
- **Test 5** [command_prompt]: Masquerading - powershell.exe running as taskhostw.exe
- **Test 6** [powershell]: Masquerading - non-windows exe running as windows exe
- **Test 7** [powershell]: Masquerading - windows exe running as different windows exe
- **Test 8** [command_prompt]: Malicious process Masquerading as LSM.exe

### T1036.004: Masquerading: Masquerade Task or Service (2 Tests)
- **Test 1** [command_prompt]: Creating W32Time similar named service using schtasks
- **Test 2** [command_prompt]: Creating W32Time similar named service using sc

### T1036.005: Masquerading: Match Legitimate Name or Location (2 Tests)
- **Test 2** [powershell]: Masquerade as a built-in system executable
- **Test 3** [powershell]: Masquerading cmd.exe as VEDetector.exe

### T1036.007: Masquerading: Double File Extension (1 Tests)
- **Test 1** [command_prompt]: File Extension Masquerading

### T1055: Process Injection (13 Tests)
- **Test 1** [powershell]: Shellcode execution via VBA
- **Test 2** [command_prompt]: Remote Process Injection in LSASS via mimikatz
- **Test 3** [powershell]: Section View Injection
- **Test 4** [powershell]: Dirty Vanity process Injection
- **Test 5** [powershell]: Read-Write-Execute process Injection
- **Test 6** [powershell]: Process Injection with Go using UuidFromStringA WinAPI
- **Test 7** [powershell]: Process Injection with Go using EtwpCreateEtwThread WinAPI
- **Test 8** [powershell]: Remote Process Injection with Go using RtlCreateUserThread WinAPI
- **Test 9** [powershell]: Remote Process Injection with Go using CreateRemoteThread WinAPI
- **Test 10** [powershell]: Remote Process Injection with Go using CreateRemoteThread WinAPI (Natively)
- **Test 11** [powershell]: Process Injection with Go using CreateThread WinAPI
- **Test 12** [powershell]: Process Injection with Go using CreateThread WinAPI (Natively)
- **Test 13** [powershell]: UUID custom process Injection

### T1055.001: Process Injection: Dynamic-link Library Injection (2 Tests)
- **Test 1** [powershell]: Process Injection via mavinject.exe
- **Test 2** [powershell]: WinPwn - Get SYSTEM shell - Bind System Shell using UsoClient DLL load technique

### T1055.002: Process Injection: Portable Executable Injection (1 Tests)
- **Test 1** [powershell]: Portable Executable Injection

### T1055.003: Thread Execution Hijacking (1 Tests)
- **Test 1** [powershell]: Thread Execution Hijacking

### T1055.004: Process Injection: Asynchronous Procedure Call (3 Tests)
- **Test 1** [command_prompt]: Process Injection via C#
- **Test 2** [powershell]: EarlyBird APC Queue Injection in Go
- **Test 3** [powershell]: Remote Process Injection with Go using NtQueueApcThreadEx WinAPI

### T1055.011: Process Injection: Extra Window Memory Injection (1 Tests)
- **Test 1** [powershell]: Process Injection via Extra Window Memory (EWM) x64 executable

### T1055.012: Process Injection: Process Hollowing (4 Tests)
- **Test 1** [powershell]: Process Hollowing using PowerShell
- **Test 2** [powershell]: RunPE via VBA
- **Test 3** [powershell]: Process Hollowing in Go using CreateProcessW WinAPI
- **Test 4** [powershell]: Process Hollowing in Go using CreateProcessW and CreatePipe WinAPIs (T1055.012)

### T1055.015: Process Injection: ListPlanting (1 Tests)
- **Test 1** [powershell]: Process injection ListPlanting

### T1070: Indicator Removal on Host (2 Tests)
- **Test 1** [command_prompt]: Indicator Removal using FSUtil
- **Test 2** [powershell]: Indicator Manipulation using FSUtil

### T1070.003: Indicator Removal on Host: Clear Command History (4 Tests)
- **Test 11** [powershell]: Prevent Powershell History Logging
- **Test 12** [powershell]: Clear Powershell History by Deleting History File
- **Test 13** [powershell]: Set Custom AddToHistoryHandler to Avoid History File Logging
- **Test 14** [powershell]: Clear PowerShell Session History

### T1070.004: Indicator Removal on Host: File Deletion (7 Tests)
- **Test 4** [command_prompt]: Delete a single file - Windows cmd
- **Test 5** [command_prompt]: Delete an entire folder - Windows cmd
- **Test 6** [powershell]: Delete a single file - Windows PowerShell
- **Test 7** [powershell]: Delete an entire folder - Windows PowerShell
- **Test 9** [powershell]: Delete Prefetch File
- **Test 10** [powershell]: Delete TeamViewer Log Files
- **Test 11** [command_prompt]: Clears Recycle bin via rd

### T1070.005: Indicator Removal on Host: Network Share Connection Removal (5 Tests)
- **Test 1** [command_prompt]: Add Network Share
- **Test 2** [command_prompt]: Remove Network Share
- **Test 3** [powershell]: Remove Network Share PowerShell
- **Test 4** [command_prompt]: Disable Administrative Share Creation at Startup
- **Test 5** [command_prompt]: Remove Administrative Shares

### T1070.006: Indicator Removal on Host: Timestomp (5 Tests)
- **Test 5** [powershell]: Windows - Modify file creation timestamp with PowerShell
- **Test 6** [powershell]: Windows - Modify file last modified timestamp with PowerShell
- **Test 7** [powershell]: Windows - Modify file last access timestamp with PowerShell
- **Test 8** [powershell]: Windows - Timestomp a File
- **Test 10** [powershell]: Event Log Manipulations- Time slipping via Powershell

### T1070.008: Email Collection: Mailbox Manipulation (2 Tests)
- **Test 1** [powershell]: Copy and Delete Mailbox Data on Windows
- **Test 4** [powershell]: Copy and Modify Mailbox Data on Windows

### T1078.001: Valid Accounts: Default Accounts (2 Tests)
- **Test 1** [command_prompt]: Enable Guest account with RDP capability and admin privileges
- **Test 2** [command_prompt]: Activate Guest Account

### T1078.003: Valid Accounts: Local Accounts (4 Tests)
- **Test 1** [command_prompt]: Create local account with admin privileges
- **Test 6** [powershell]: WinPwn - Loot local Credentials - powerhell kittie
- **Test 7** [powershell]: WinPwn - Loot local Credentials - Safetykatz
- **Test 13** [command_prompt]: Use PsExec to elevate to NT Authority\SYSTEM account

### T1127: Trusted Developer Utilities Proxy Execution (2 Tests)
- **Test 1** [command_prompt]: Lolbin Jsc.exe compile javascript to exe
- **Test 2** [command_prompt]: Lolbin Jsc.exe compile javascript to dll

### T1127.001: Trusted Developer Utilities Proxy Execution: MSBuild (2 Tests)
- **Test 1** [command_prompt]: MSBuild Bypass Using Inline Tasks (C#)
- **Test 2** [command_prompt]: MSBuild Bypass Using Inline Tasks (VB)

### T1134.001: Access Token Manipulation: Token Impersonation/Theft (5 Tests)
- **Test 1** [powershell]: Named pipe client impersonation
- **Test 2** [powershell]: `SeDebugPrivilege` token duplication
- **Test 3** [powershell]: Launch NSudo Executable
- **Test 4** [powershell]: Bad Potato
- **Test 5** [powershell]: Juicy Potato

### T1134.002: Create Process with Token (2 Tests)
- **Test 1** [powershell]: Access Token Manipulation
- **Test 2** [powershell]: WinPwn - Get SYSTEM shell - Pop System Shell using Token Manipulation technique

### T1134.004: Access Token Manipulation: Parent PID Spoofing (5 Tests)
- **Test 1** [powershell]: Parent PID Spoofing using PowerShell
- **Test 2** [powershell]: Parent PID Spoofing - Spawn from Current Process
- **Test 3** [powershell]: Parent PID Spoofing - Spawn from Specified Process
- **Test 4** [powershell]: Parent PID Spoofing - Spawn from svchost.exe
- **Test 5** [powershell]: Parent PID Spoofing - Spawn from New Process

### T1134.005: Access Token Manipulation: SID-History Injection (1 Tests)
- **Test 1** [command_prompt]: Injection SID-History with mimikatz

### T1140: Deobfuscate/Decode Files or Information (3 Tests)
- **Test 1** [command_prompt]: Deobfuscate/Decode Files Or Information
- **Test 2** [command_prompt]: Certutil Rename and Decode
- **Test 11** [command_prompt]: Expand CAB with expand.exe

### T1197: BITS Jobs (4 Tests)
- **Test 1** [command_prompt]: Bitsadmin Download (cmd)
- **Test 2** [powershell]: Bitsadmin Download (PowerShell)
- **Test 3** [command_prompt]: Persist, Download, & Execute
- **Test 4** [command_prompt]: Bits download using desktopimgdownldr.exe (cmd)

### T1202: Indirect Command Execution (5 Tests)
- **Test 1** [command_prompt]: Indirect Command Execution - pcalua.exe
- **Test 2** [command_prompt]: Indirect Command Execution - forfiles.exe
- **Test 3** [command_prompt]: Indirect Command Execution - conhost.exe
- **Test 4** [powershell]: Indirect Command Execution - Scriptrunner.exe
- **Test 5** [powershell]: Indirect Command Execution - RunMRU Dialog

### T1216: Signed Script Proxy Execution (1 Tests)
- **Test 1** [command_prompt]: manage-bde.wsf Signed Script Command Execution

### T1216.001: Signed Script Proxy Execution: Pubprn (1 Tests)
- **Test 1** [command_prompt]: PubPrn.vbs Signed Script Bypass

### T1216.002: System Script Proxy Execution: SyncAppvPublishingServer (1 Tests)
- **Test 1** [command_prompt]: SyncAppvPublishingServer Signed Script PowerShell Command Execution

### T1218: Signed Binary Proxy Execution (16 Tests)
- **Test 1** [command_prompt]: mavinject - Inject DLL into running process
- **Test 2** [command_prompt]: Register-CimProvider - Execute evil dll
- **Test 3** [command_prompt]: InfDefaultInstall.exe .inf Execution
- **Test 4** [command_prompt]: ProtocolHandler.exe Downloaded a Suspicious File
- **Test 5** [powershell]: Microsoft.Workflow.Compiler.exe Payload Execution
- **Test 6** [powershell]: Renamed Microsoft.Workflow.Compiler.exe Payload Executions
- **Test 7** [powershell]: Invoke-ATHRemoteFXvGPUDisablementCommand base test
- **Test 8** [powershell]: DiskShadow Command Execution
- **Test 9** [command_prompt]: Load Arbitrary DLL via Wuauclt (Windows Update Client)
- **Test 10** [command_prompt]: Lolbin Gpscript logon option
- **Test 11** [command_prompt]: Lolbin Gpscript startup option
- **Test 12** [command_prompt]: Lolbas ie4uinit.exe use as proxy
- **Test 13** [powershell]: LOLBAS CustomShellHost to Spawn Process
- **Test 14** [command_prompt]: Provlaunch.exe Executes Arbitrary Command via Registry Key
- **Test 15** [powershell]: LOLBAS Msedge to Spawn Process
- **Test 16** [powershell]: System Binary Proxy Execution - Wlrmdr Lolbin

### T1218.001: Signed Binary Proxy Execution: Compiled HTML File (8 Tests)
- **Test 1** [command_prompt]: Compiled HTML Help Local Payload
- **Test 2** [command_prompt]: Compiled HTML Help Remote Payload
- **Test 3** [powershell]: Invoke CHM with default Shortcut Command Execution
- **Test 4** [powershell]: Invoke CHM with InfoTech Storage Protocol Handler
- **Test 5** [powershell]: Invoke CHM Simulate Double click
- **Test 6** [powershell]: Invoke CHM with Script Engine and Help Topic
- **Test 7** [powershell]: Invoke CHM Shortcut Command with ITS and Help Topic
- **Test 8** [command_prompt]: Decompile Local CHM File

### T1218.002: Signed Binary Proxy Execution: Control Panel (1 Tests)
- **Test 1** [command_prompt]: Control Panel Items

### T1218.003: Signed Binary Proxy Execution: CMSTP (2 Tests)
- **Test 1** [command_prompt]: CMSTP Executing Remote Scriptlet
- **Test 2** [command_prompt]: CMSTP Executing UAC Bypass

### T1218.004: Signed Binary Proxy Execution: InstallUtil (8 Tests)
- **Test 1** [powershell]: CheckIfInstallable method call
- **Test 2** [powershell]: InstallHelper method call
- **Test 3** [powershell]: InstallUtil class constructor method call
- **Test 4** [powershell]: InstallUtil Install method call
- **Test 5** [powershell]: InstallUtil Uninstall method call - /U variant
- **Test 6** [powershell]: InstallUtil Uninstall method call - '/installtype=notransaction /action=uninstall' variant
- **Test 7** [powershell]: InstallUtil HelpText method call
- **Test 8** [powershell]: InstallUtil evasive invocation

### T1218.005: Signed Binary Proxy Execution: Mshta (10 Tests)
- **Test 1** [command_prompt]: Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject
- **Test 2** [command_prompt]: Mshta executes VBScript to execute malicious command
- **Test 3** [powershell]: Mshta Executes Remote HTML Application (HTA)
- **Test 4** [powershell]: Invoke HTML Application - Jscript Engine over Local UNC Simulating Lateral Movement
- **Test 5** [powershell]: Invoke HTML Application - Jscript Engine Simulating Double Click
- **Test 6** [powershell]: Invoke HTML Application - Direct download from URI
- **Test 7** [powershell]: Invoke HTML Application - JScript Engine with Rundll32 and Inline Protocol Handler
- **Test 8** [powershell]: Invoke HTML Application - JScript Engine with Inline Protocol Handler
- **Test 9** [powershell]: Invoke HTML Application - Simulate Lateral Movement over UNC Path
- **Test 10** [command_prompt]: Mshta used to Execute PowerShell

### T1218.007: Signed Binary Proxy Execution: Msiexec (11 Tests)
- **Test 1** [command_prompt]: Msiexec.exe - Execute Local MSI file with embedded JScript
- **Test 2** [command_prompt]: Msiexec.exe - Execute Local MSI file with embedded VBScript
- **Test 3** [command_prompt]: Msiexec.exe - Execute Local MSI file with an embedded DLL
- **Test 4** [command_prompt]: Msiexec.exe - Execute Local MSI file with an embedded EXE
- **Test 5** [powershell]: WMI Win32_Product Class - Execute Local MSI file with embedded JScript
- **Test 6** [powershell]: WMI Win32_Product Class - Execute Local MSI file with embedded VBScript
- **Test 7** [powershell]: WMI Win32_Product Class - Execute Local MSI file with an embedded DLL
- **Test 8** [powershell]: WMI Win32_Product Class - Execute Local MSI file with an embedded EXE
- **Test 9** [command_prompt]: Msiexec.exe - Execute the DllRegisterServer function of a DLL
- **Test 10** [command_prompt]: Msiexec.exe - Execute the DllUnregisterServer function of a DLL
- **Test 11** [command_prompt]: Msiexec.exe - Execute Remote MSI file

### T1218.008: Signed Binary Proxy Execution: Odbcconf (2 Tests)
- **Test 1** [command_prompt]: Odbcconf.exe - Execute Arbitrary DLL
- **Test 2** [command_prompt]: Odbcconf.exe - Load Response File

### T1218.009: Signed Binary Proxy Execution: Regsvcs/Regasm (2 Tests)
- **Test 1** [command_prompt]: Regasm Uninstall Method Call Test
- **Test 2** [powershell]: Regsvcs Uninstall Method Call Test

### T1218.010: Signed Binary Proxy Execution: Regsvr32 (5 Tests)
- **Test 1** [command_prompt]: Regsvr32 local COM scriptlet execution
- **Test 2** [command_prompt]: Regsvr32 remote COM scriptlet execution
- **Test 3** [command_prompt]: Regsvr32 local DLL execution
- **Test 4** [command_prompt]: Regsvr32 Registering Non DLL
- **Test 5** [command_prompt]: Regsvr32 Silent DLL Install Call DllRegisterServer

### T1218.011: Signed Binary Proxy Execution: Rundll32 (16 Tests)
- **Test 1** [command_prompt]: Rundll32 execute JavaScript Remote Payload With GetObject
- **Test 2** [command_prompt]: Rundll32 execute VBscript command
- **Test 3** [command_prompt]: Rundll32 execute VBscript command using Ordinal number
- **Test 4** [command_prompt]: Rundll32 advpack.dll Execution
- **Test 5** [command_prompt]: Rundll32 ieadvpack.dll Execution
- **Test 6** [command_prompt]: Rundll32 syssetup.dll Execution
- **Test 7** [command_prompt]: Rundll32 setupapi.dll Execution
- **Test 8** [command_prompt]: Execution of HTA and VBS Files using Rundll32 and URL.dll
- **Test 9** [command_prompt]: Launches an executable using Rundll32 and pcwutl.dll
- **Test 10** [powershell]: Execution of non-dll using rundll32.exe
- **Test 11** [command_prompt]: Rundll32 with Ordinal Value
- **Test 12** [command_prompt]: Rundll32 with Control_RunDLL
- **Test 13** [command_prompt]: Rundll32 with desk.cpl
- **Test 14** [command_prompt]: Running DLL with .init extension and function
- **Test 15** [command_prompt]: Rundll32 execute command via FileProtocolHandler
- **Test 16** [powershell]: Rundll32 execute payload by calling RouteTheCall

### T1220: XSL Script Processing (4 Tests)
- **Test 1** [command_prompt]: MSXSL Bypass using local files
- **Test 2** [command_prompt]: MSXSL Bypass using remote files
- **Test 3** [command_prompt]: WMIC bypass using local XSL file
- **Test 4** [command_prompt]: WMIC bypass using remote XSL file

### T1221: Template Injection (1 Tests)
- **Test 1** [command_prompt]: WINWORD Remote Template Injection

### T1497.001: Virtualization/Sandbox Evasion: System Checks (3 Tests)
- **Test 3** [powershell]: Detect Virtualization Environment (Windows)
- **Test 5** [powershell]: Detect Virtualization Environment via WMI Manufacturer/Model Listing (Windows)
- **Test 9** [powershell]: Turla Mosquito Sandbox Evasion via SetupDiGetClassDevs Check

### T1542.001: Pre-OS Boot: System Firmware (1 Tests)
- **Test 1** [powershell]: UEFI Persistence via Wpbbin.exe File Creation

### T1564: Hide Artifacts (5 Tests)
- **Test 1** [powershell]: Extract binary files via VBA
- **Test 2** [command_prompt]: Create a Hidden User Called "$"
- **Test 3** [powershell]: Create an "Administrator " user (with a space on the end)
- **Test 4** [command_prompt]: Create and Hide a Service with sc.exe
- **Test 5** [powershell]: Command Execution with NirCmd

### T1564.001: Hide Artifacts: Hidden Files and Directories (5 Tests)
- **Test 3** [command_prompt]: Create Windows System File with Attrib
- **Test 4** [command_prompt]: Create Windows Hidden File with Attrib
- **Test 8** [command_prompt]: Hide Files Through Registry
- **Test 9** [powershell]: Create Windows Hidden File with powershell
- **Test 10** [powershell]: Create Windows System File with powershell

### T1564.002: Hide Artifacts: Hidden Users (1 Tests)
- **Test 3** [command_prompt]: Create Hidden User in Registry

### T1564.003: Hide Artifacts: Hidden Window (3 Tests)
- **Test 1** [powershell]: Hidden Window
- **Test 2** [command_prompt]: Headless Browser Accessing Mockbin
- **Test 3** [powershell]: Hidden Window-Conhost Execution

### T1564.004: Hide Artifacts: NTFS File Attributes (5 Tests)
- **Test 1** [command_prompt]: Alternate Data Streams (ADS)
- **Test 2** [powershell]: Store file in Alternate Data Stream (ADS)
- **Test 3** [command_prompt]: Create ADS command prompt
- **Test 4** [powershell]: Create ADS PowerShell
- **Test 5** [command_prompt]: Create Hidden Directory via $index_allocation

### T1564.006: Run Virtual Instance (3 Tests)
- **Test 1** [command_prompt]: Register Portable Virtualbox
- **Test 2** [command_prompt]: Create and start VirtualBox virtual machine
- **Test 3** [powershell]: Create and start Hyper-V virtual machine

### T1564.012: Hide Artifacts: File/Path Exclusions (1 Tests)
- **Test 1** [powershell]: Stage and execute a payload from a Windows Defender excluded path

### T1574.001: Hijack Execution Flow: DLL (7 Tests)
- **Test 1** [command_prompt]: DLL Search Order Hijacking - amsi.dll
- **Test 2** [command_prompt]: Phantom Dll Hijacking - WinAppXRT.dll
- **Test 3** [command_prompt]: Phantom Dll Hijacking - ualapi.dll
- **Test 4** [command_prompt]: DLL Side-Loading using the Notepad++ GUP.exe binary
- **Test 5** [command_prompt]: DLL Side-Loading using the dotnet startup hook environment variable
- **Test 6** [powershell]: DLL Search Order Hijacking,DLL Sideloading Of KeyScramblerIE.DLL Via KeyScrambler.EXE
- **Test 7** [command_prompt]: DLL Search Order Hijacking - ntprint

### T1574.008: Hijack Execution Flow: Path Interception by Search Order Hijacking (1 Tests)
- **Test 1** [powershell]: powerShell Persistence via hijacking default modules - Get-Variable.exe

### T1574.009: Hijack Execution Flow: Path Interception by Unquoted Path (1 Tests)
- **Test 1** [command_prompt]: Execution of program.exe as service with unquoted service path

### T1574.011: Hijack Execution Flow: Services Registry Permissions Weakness (2 Tests)
- **Test 1** [powershell]: Service Registry Permissions Weakness
- **Test 2** [command_prompt]: Service ImagePath Change with reg.exe

### T1574.012: Hijack Execution Flow: COR_PROFILER (3 Tests)
- **Test 1** [powershell]: User scope COR_PROFILER
- **Test 2** [powershell]: System Scope COR_PROFILER
- **Test 3** [powershell]: Registry-free process scope COR_PROFILER

### T1620: Reflective Code Loading (3 Tests)
- **Test 1** [powershell]: WinPwn - Reflectively load Mimik@tz into memory
- **Test 2** [powershell]: Reflective PE Injection via PowerSploit
- **Test 3** [powershell]: Turla Mosquito (CommanderDLL.dll) Dynamic Export Address Table (EAT) Patching

### T1622: Debugger Evasion (1 Tests)
- **Test 1** [powershell]: Detect a Debugger Presence in the Machine

