# Script: Lab 07 Stretch Goal - FDE via Powershell
# Author: Robert Gregor
# Date of latest revision: 26 APR 23

# Objectives
    # Write and test a PowerShell script that enables BitLocker and initializes the same FDE process performed through the GUI
        # 

# My Sources:
    # [BitLocker: Use BitLocker Drive Encryption Tools to manage BitLocker](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-use-bitlocker-drive-encryption-tools-to-manage-bitlocker)
    # []()

# Main

cls
Write-Host ""
Write-Host "Below are the available drives on your computer"
Get-PSDrive
Write-Host ""
$user_drive = Read-Host "Please enter the letter of the drive you would like to encrypt"
$drive_mount_point = $user_drive + ":"
Write-Host ""
$user_pass = Read-Host -AsSecureString "Please provide a secure password"
Write-Host ""
# Enables bitlocker for user_drive with user_pass
Enable-BitLocker -MountPoint $drive_mount_point -EncryptionMethod XtsAes256 -UsedSpaceOnly:$false -PasswordProtector -Password $user_pass
Write-Host "You have successfully enabled bitlocker, your computer will now reboot and encrypt the drive to complete the process"
Write-Host ""
Read-Host "Please press ENTER to reboot"
Restart-Computer -Force

