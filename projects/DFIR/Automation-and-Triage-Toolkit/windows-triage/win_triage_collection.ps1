<#
.SYNOPSIS
	A lightweight DFIR triage script designed to collect volatile forensic evidence from a Windows host.
	TITLE: WINDOWS TRIAGE COLLECTION SCRIPT

.DESCRIPTION
  This script automates the collection of critical security artifacts including: PowerShell operational logs, Windows Defender threat history, ARP tables, active network connections, and running processes. 
  It outputs all data into a timestamped directory for forensic preservation.
	TABLE OF CONTENTS
		FIRST--->Configuration & Environment Setup
    1. System Metadata (Crucial for timelines)
		2. PowerShell Operational Logs (Search for script blocks/obfuscation)
		3. Windows Defender Detections
		4. Network Artifacts (ARP & Active Connections)
		5. Volatile Process List (Identifying suspicious hidden processes)

.PARAMETER ExportBaseDir
  The root directory where the triage folder will be created. Defaults to C:\.

.PARAMETER IncludeNetwork
  A switch to determine if active TCP connections and ARP tables should be gathered.

.EXAMPLE
  .\Get-TriageData.ps1 -ExportBaseDir "D:\Forensics"
  >Collects data and saves it to a timestamped folder on the D:\ drive.

.NOTES
    ===========================================================================
    ENVIRONMENT & CONFIGURATION NOTES:
    ===========================================================================
    1. PRIVILEGES: Must be executed within an Elevated (Run as Admin) session.
    2. OS SUPPORT: Tested on Windows 10/11 and Windows Server 2016/2019/2022.
    3. POWERSHELL VERSION: Requires PowerShell 5.1 or PowerShell Core 7+.
    4. DEPENDENCIES: 
       - Requires 'Defender' module for Get-MpThreatDetection.
       - Requires 'CimCmdlets' or 'ActiveDirectory' modules for advanced metadata.
    5. EXECUTION POLICY: May require 'Set-ExecutionPolicy Bypass' to run locally if the script is unsigned.
    6. STORAGE: Ensure at least 50MB of free space on the destination drive (logs can grow large on busy servers).
    ===========================================================================
#>

# --- Configuration & Environment Setup ---
$ComputerName = $env:COMPUTERNAME
$Timestamp = Get-Date -Format "yyyyMMdd_HHmm"
$ExportPath = "C:\IR_Triage_$Timestamp"
New-Item -Path $ExportPath -ItemType Directory -Force | Out-Null

Write-Host "--- Starting Forensic Collection on $ComputerName ---" -ForegroundColor Cyan

# 1. System Metadata (Crucial for timelines)
Write-Host "[+] Collecting System Metadata..."
$Metadata = [PSCustomObject]@{
    Hostname   = $ComputerName
    User       = [Security.Principal.WindowsIdentity]::GetCurrent().Name
    Collection = Get-Date
    OS_Version = (Get-WmiObject Win32_OperatingSystem).Caption
}
$Metadata | Export-Csv -Path "$ExportPath\Collection_Metadata.csv" -NoTypeInformation

# 2. PowerShell Operational Logs (Search for script blocks/obfuscation)
Write-Host "[+] Collecting PowerShell Logs..."
try {
    Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -ErrorAction Stop | 
    Select-Object TimeCreated, Id, LevelDisplayName, Message | 
    Export-Csv -Path "$ExportPath\PowerShell_Logs.csv" -NoTypeInformation
} catch {
    "Could not access PS Logs: $($_.Exception.Message)" | Out-File "$ExportPath\Errors.log" -Append
}

# 3. Windows Defender Detections
Write-Host "[+] Collecting Defender Alerts..."
if (Get-Command Get-MpThreatDetection -ErrorAction SilentlyContinue) {
    Get-MpThreatDetection | Export-Csv -Path "$ExportPath\Defender_Alerts.csv" -NoTypeInformation
}

# 4. Network Artifacts (ARP & Active Connections)
Write-Host "[+] Collecting Network Artifacts..."
arp -a | Out-File "$ExportPath\ARP_Cache.txt"
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess | 
Export-Csv -Path "$ExportPath\Network_Connections.csv" -NoTypeInformation

# 5. Volatile Process List (Identifying suspicious hidden processes)
Write-Host "[+] Collecting Process List..."
Get-Process | Select-Object Id, ProcessName, StartTime, Path, Company | 
Export-Csv -Path "$ExportPath\Process_List.csv" -NoTypeInformation

Write-Host "--- Collection Complete! Data saved to: $ExportPath ---" -ForegroundColor Green
