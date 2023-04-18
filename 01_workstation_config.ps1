# Script: 01 - Automating Workstation Configuration
# Author: Robert Gregor
# Date of latest revision: 18APR23

# Objectives
    # Write a PowerShell script that achieves the following objectives
        # Automatic screen lock
        # Antivirus installed and scanning
        # Automatic OS updates enabled
    # Test and validate the script works

# My Sources:
    # [What is the Absolute Path to a Registry Value?](https://learn.microsoft.com/en-us/answers/questions/150269/what-is-the-absolute-path-to-a-registry-value)
    # [Configure Automatic Updates in a Non–Active Directory Environment](https://learn.microsoft.com/de-de/security-updates/windowsupdateservices/18127499)
    # [Set-ItemProperty](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.3)

# Main

# Declares $RegPath Variable equal to location of OS update registry key

$RegPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"

# Use Set-ItemProperty command to set AUOptions value to 4 (Automatic download and scheduled installation)

Set-ItemProperty -Path $RegPath -Name AUOptions -Value 4

# End