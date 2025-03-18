# Define output file path
$outputFile = "C:\ProgramData\Inventory\SoftwareInventory.json"

# Get the directory path from the output file path
$outputDirectory = [System.IO.Path]::GetDirectoryName($outputFile)

# Check if the directory exists, and create it if it doesn't
if (!(Test-Path -Path $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
}

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
