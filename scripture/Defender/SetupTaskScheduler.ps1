# Define script path
$ScriptPath = "C:\ProgramData\SoftwareInventory.ps1"
$TaskName = "SoftwareInventoryCollection"

# Creating scheduled task action (run PowerShell silently)
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"$ScriptPath`""

# Setting trigger (daily at 3 AM) and run if missed
$Trigger = New-ScheduledTaskTrigger -Daily -At 3AM
$Trigger.MissedTaskPolicy = "RunImmediately"

# Setting principal (run as SYSTEM with highest privileges)
$Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest

# Additional task settings to ensure silent execution
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -Hidden

# Registering the scheduled task
$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Principal $Principal -Settings $Settings
Register-ScheduledTask -TaskName $TaskName -InputObject $Task -Force

Write-Host "Scheduled task '$TaskName' has been created to run silently daily at 3 AM, and will run if missed."
