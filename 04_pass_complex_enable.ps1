# Script: 04 - Password must meet complexity requirements
# Author: Robert Gregor
# Date of latest revision: 19 APR 23

# Objectives
    # Write a powershell script that enables "Password must meet complexity requirements"

Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters" -Name "RequireComplexPassword" -Value 1