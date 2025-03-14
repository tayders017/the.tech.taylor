# Output file path
$outputFile = "C:\ProgramData\SoftwareInventory.json"

# Collect installed software and their executables
$SoftwareInventory = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |
Where-Object { $_.InstallLocation -ne $null } | 
ForEach-Object {
    $Executable = Get-ChildItem -Path $_.InstallLocation -Recurse -Include *.exe -ErrorAction SilentlyContinue |
    Select-Object -First 1 FullName
    [PSCustomObject]@{
        SoftwareName = $_.DisplayName
        Version = $_.DisplayVersion
        ExecutableFileName = $Executable.FullName
    }
}

# Convert to JSON and save
$SoftwareInventory | ConvertTo-Json -Depth 3 | Out-File $outputFile -ErrorAction SilentlyContinue
