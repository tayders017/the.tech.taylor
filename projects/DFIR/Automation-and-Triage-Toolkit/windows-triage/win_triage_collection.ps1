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

param (
    [string]$ExportBaseDir = "C:\"
)

# 1. PRE-FLIGHT LOGIC
Write-Host "--- Performing Pre-Flight Environment Checks ---" -ForegroundColor Yellow

$IsAdmin = ([Security.Principal.WindowsIdentity]::GetCurrent().Groups -contains "S-1-5-32-544")
$FreeSpace = (Get-PSDrive $ExportBaseDir.Substring(0,1)).Free / 1MB
$DefenderAvailable = Get-Command Get-MpThreatDetection -ErrorAction SilentlyContinue

$AbortScript = $false

# Check Admin Rights (Critical for Event Logs)
if (-not $IsAdmin) {
    Write-Host "[!] ERROR: Script not running as Administrator. Collection aborted." -ForegroundColor Red
    $AbortScript = $true
}

# Check Disk Space (Safety first)
if ($FreeSpace -lt 100) {
    Write-Host "[!] ERROR: Insufficient disk space ($([math]::Round($FreeSpace,2)) MB). 100MB required." -ForegroundColor Red
    $AbortScript = $true
}

# Exit if critical checks fail
if ($AbortScript) { exit }

Write-Host "[✓] Pre-flight checks passed. Initializing collection..." -ForegroundColor Green

# 2. CONFIGURATION AND ENVIRONMENT SETUP
$ComputerName = $env:COMPUTERNAME
$Timestamp = Get-Date -Format "yyyyMMdd_HHmm"
$ExportPath = Join-Path -Path $ExportBaseDir -ChildPath "IR_Triage_$($ComputerName)_$Timestamp"

New-Item -Path $ExportPath -ItemType Directory -Force | Out-Null
Write-Host "--- Starting Forensic Collection on $ComputerName ---" -ForegroundColor Cyan


# 3. Collection Modules
# 3a. System Metadata
Write-Host "[+] Collecting System Metadata..."
[PSCustomObject]@{
    Hostname   = $ComputerName
    User       = [Security.Principal.WindowsIdentity]::GetCurrent().Name
    Collection = Get-Date
    OS_Version = (Get-CimInstance Win32_OperatingSystem).Caption
} | Export-Csv -Path "$ExportPath\Collection_Metadata.csv" -NoTypeInformation

# 3b. PowerShell Logs
Write-Host "[+] Collecting PowerShell Logs..."
try {
    Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -MaxEvents 5000 -ErrorAction Stop | 
    Select-Object TimeCreated, Id, LevelDisplayName, Message | 
    Export-Csv -Path "$ExportPath\PowerShell_Logs.csv" -NoTypeInformation
} catch {
    "Could not access PS Logs: $($_.Exception.Message)" | Out-File "$ExportPath\Errors.log" -Append
}

# 3c. Windows Defender Detections
if ($DefenderAvailable) {
    Write-Host "[+] Collecting Defender Alerts..."
    Get-MpThreatDetection | Export-Csv -Path "$ExportPath\Defender_Alerts.csv" -NoTypeInformation
} else {
    Write-Host "[!] Defender module not found. Skipping..." -ForegroundColor Gray
}

# 3d. Network Artifacts
Write-Host "[+] Collecting Network Artifacts..."
arp -a | Out-File "$ExportPath\ARP_Cache.txt"
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess | 
Export-Csv -Path "$ExportPath\Network_Connections.csv" -NoTypeInformation

# 3e. Volatile Process List
Write-Host "[+] Collecting Process List..."
Get-Process | Select-Object Id, ProcessName, StartTime, Path, Company | 
Export-Csv -Path "$ExportPath\Process_List.csv" -NoTypeInformation

# 4. WRAP UP
Write-Host "`n--- Collection Complete! Data saved to: $ExportPath ---" -ForegroundColor Green

Write-Host "--- Collection Complete! Data saved to: $ExportPath ---" -ForegroundColor Green
