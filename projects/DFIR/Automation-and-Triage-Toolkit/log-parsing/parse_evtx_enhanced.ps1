<#
.SYNOPSIS
	Parses an offline Windows Security Event Log (.evtx) for Failed Logon attempts.

.DESCRIPTION
	This script targets Event ID 4625 (An account failed to log on). 
	Uses the highly efficient -FilterHashtable method to reduce memory consumption.
	The script extracts specific indexed properties for Username and Source IP.
	TABLE OF CONTENTS:
	1. Configuration & Path Setup
	2. Validation
	3. Define Filter Criteria
	4. Execution & Data Extraction
	5. Summary Output

.PARAMETER LogPath
	The full file path to the .evtx file to be analyzed.

.EXAMPLE
	.\Parse-SecurityLog.ps1
#>

# 1. Configuration & Path Setup
$LogPath = "C:\Logs\Security.evtx"

# 2. Validation
# Ensure the log file exists before proceeding to avoid pipeline errors.
if (-not (Test-Path $LogPath)) {
    Write-Error "Log file not found at $LogPath. Please check the path and try again."
    return
}

# 3. Define Filter Criteria
# Using a Hashtable for filtering is significantly faster than using 'Where-Object'.
$Filter = @{
    Path = $LogPath
    Id   = 4625
}

Write-Host "Searching for Failed Logons in: $LogPath..." -ForegroundColor Cyan

# 4. Execution & Data Extraction
# 4a. Get-WinEvent pulls the raw XML data.
# 4b. Select-Object uses 'Calculated Properties' to grab specific data points:
#    - Properties[5]  = TargetUserName
#    - Properties[19] = IpAddress
Get-WinEvent -FilterHashtable $Filter -ErrorAction SilentlyContinue | 
    Select-Object TimeCreated, Id, 
    @{Name='Username';      Expression={$_.Properties[5].Value}},
    @{Name='SourceAddress'; Expression={$_.Properties[19].Value}} |
    Format-Table -AutoSize

# 5. Summary Output
Write-Host "Parsing Complete." -ForegroundColor Green

