# ==============================================================================
# INITIAL EVIDENCE COLLECTION SCRIPT / INCIDENT RESPONSE TRIAGE SCRIPT
# ==============================================================================
# PURPOSE: Rapid collection of volatile data and persistence mechanisms.
# REQUIREMENTS: Run with Administrator privileges.
# ==============================================================================
# TABLE OF CONTENTS
#    1. System Identification & Environment ........ [Metadata & OS Info]
#    2. Process & Execution Analysis .......... [Running Tasks & CMD Lines]
#    3. Network & Connectivity ................ [Network State, Connections & DNS Cache]
#    4. Persistence Mechanisms .................. [Startup & Scheduled Tasks]
#    5. User & Session Activity ...... [Users & Active Logons]
#    6. Service Inventory ............ [Background Services]
#    7. Recent File Activity ......... [Recent Changes (Last 24 hours) & Temp Files]
# ==============================================================================

# 1. System Information & Environment
Write-Host "Collecting System Info..."
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsArchitecture, LastBootUpTime | Export-Csv system_info.csv

# 2. Process & Execution Analysis
# Including ParentProcessId and Path helps identify masquerading malware
Write-Host "Collecting Processes..."
Get-CimInstance Win32_Process | Select-Object Name, ProcessId, ParentProcessId, CommandLine, ExecutablePath | Export-Csv processes_detailed.csv

# 3. Network & Connectivity
Write-Host "Collecting Network State..."
# netstat is classic, but Get-NetTCPConnection provides more PowerShell-friendly output
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess | Export-Csv network_connections.csv
Get-DnsClientCache | Export-Csv dns_cache.csv
Get-Content C:\Windows\System32\drivers\etc\hosts > hosts_file_backup.txt

# 4. Persistence Mechanisms (Startup & Tasks)
Write-Host "Collecting Persistence Data..."
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User | Export-Csv startup_items.csv
# Using Get-ScheduledTask provides better filtering than the legacy schtasks
Get-ScheduledTask | Where-Object {$_.State -ne "Disabled"} | Select-Object TaskName, TaskPath, State | Export-Csv scheduled_tasks.csv

# 5. User & Session Activity
Write-Host "Collecting User Data..."
Get-LocalUser | Select-Object Name, Enabled, LastLogon | Export-Csv local_users.csv
# Shows who is currently logged in (useful for spotting lateral movement)
quser > active_sessions.txt

# 6. Services Inventory
Write-Host "Collecting Services..."
Get-Service | Where-Object {$_.Status -eq "Running"} | Select-Object Name, DisplayName, ServiceType | Export-Csv running_services.csv

# 7. Recent File Activity (Last 24 Hours)
Write-Host "Collecting Recent File Changes..."
$TimeLimit = (Get-Date).AddDays(-1)
Get-ChildItem -Path C:\Users\*\Downloads, C:\Windows\Temp -Recurse -ErrorAction SilentlyContinue | Where-Object {$_.LastWriteTime -gt $TimeLimit} | Select-Object FullName, LastWriteTime | Export-Csv recent_files.csv

Write-Host "Triage Collection Complete."
