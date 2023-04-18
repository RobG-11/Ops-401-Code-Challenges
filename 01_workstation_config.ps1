# Script: 01 - Automating Workstation Configuration
# Author: Robert Gregor
# Date of latest revision: 18APR23

# Objectives
    # Write a PowerShell script that achieves the following objectives
        # Automatic OS updates enabled
        # Automatic screen lock
        # Antivirus installed and scanning
    # Test and validate the script works

# My Sources:
    # [What is the Absolute Path to a Registry Value?](https://learn.microsoft.com/en-us/answers/questions/150269/what-is-the-absolute-path-to-a-registry-value)
    # [Configure Automatic Updates in a Non–Active Directory Environment](https://learn.microsoft.com/de-de/security-updates/windowsupdateservices/18127499)
    # [How to Specify Screen Saver Timeout in Windows](https://www.tenforums.com/tutorials/118662-specify-screen-saver-timeout-windows.html)
    # [Set-ItemProperty](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.3)
    # [Invoke-WebRequest](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.3)
    # [Out-File](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/out-file?view=powershell-7.3)
    # [Start-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process?view=powershell-7.3)


# Main

function Auto-OS-Update{

    # Declares $RegPath Variable equal to location of OS update registry key
    $RegPath = "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate/AU"

    # Use Set-ItemProperty command to set AUOptions value to 4 (Automatic download and scheduled installation)
    Set-ItemProperty -Path $RegPath -Name AUOptions -Value 4

    Write-Host ""
    Read-Host "Windows updates are now set for automatic download and scheduled installation, press ENTER to return to menu..."

}

function Enable-ScreenLock{

    # Declares $RegPath Variable equal to location of OS update registry key
    $RegPath = "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Control Panel\Desktop"

    # Use Set-ItemProperty command to set ScreenSaveTimeOut value to 300 seconds (5 minutes)
    Set-ItemProperty -Path $RegPath -Name ScreenSaveTimeOut -Value 300

    Write-Host ""
    Read-Host "ScreenSaveTimeOut is now enabled and set to lock after five minutes of no use, press ENTER to return to menu..."

}

function Install-AV-Scan{

    # Declares $InstallPath Variable equal to location of AVG anti-virus software installation executable
    $InstallPath = "https://www.avg.com/en-us/download-thank-you.php?product=FREEGSR#pc/avg_antivirus_free_setup.exe"

    # Invokes a Web Request to copy AVG anti-virus installation executable to a temporary folder
    Invoke-WebRequest -Uri $InstallPath -OutFile $env:TEMP\avg_antivirus_free_setup.exe

    # Execute installation file saved in global TEMP variable
    Start-Process -FilePath $env:TEMP\avg_antivirus_free_setup.exe

    Write-Host ""
    Read-Host "AVG anti-virus installation initiated, follow prompts, once completed, press ENTER to conduct a scan..."

    # Next step TBD
    exit
}

while($true) {
    clear
    Write-Host "Welcome to the Workstation Configuration Wizard"
    Write-Host "-----------------------------------------------"
    Write-Host "1) Enable automatic Operating System updates"
    Write-Host "2) Enable automatic screen lock"
    Write-Host "3) Install AVG Anti-Virus and conduct scan"
    Write-Host "exit) Exit Workstation Configuration Wizard"
    Write-Host "-----------------------------------------------"
    $Selection = Read-Host "Please make a selection..."

    if ($Selection -eq 1) {
    Auto-OS-Update
    } elseif ($Selection -eq 2) {
    Enable-ScreenLock
    } elseif ($Selection -eq 3) {
    Install-AV-Scan
    } elseif ($Selection -eq "exit") {
    Write-Host ""
    Write-Host "You have exited the Workstation Configuration Wizard successfully!"
    Write-Host ""
    exit
    } else {
    Write-Host "Invalid Input!"
    }
}

# End
