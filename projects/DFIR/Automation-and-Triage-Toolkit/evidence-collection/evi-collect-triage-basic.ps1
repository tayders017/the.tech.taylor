# Collect running processes
Get-Process | Export-Csv processes.csv

# Collect network connections
netstat -ano > netstat.txt

# Collect scheduled tasks
schtasks /query /fo LIST /v > scheduled_tasks.txt

# Collect local users
Get-LocalUser > local_users.txt

# Collect startup items
Get-CimInstance Win32_StartupCommand > startup_items.txt
