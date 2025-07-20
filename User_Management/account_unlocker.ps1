# This script unlocks a specified user account in Active Directory.
# It requires Active Directory PowerShell module and Administrator privileges.

# Function to check if the Active Directory module is available
function Test-ADModule {
    try {
        Get-Module -ListAvailable -Name ActiveDirectory | Out-Null
        return $true
    }
    catch {
        return $false
    }
}

# Function to unlock an AD account
function Unlock-UserAccount {
    param (
        [Parameter(Mandatory=$true)]
        [string]$UserName
    )

    Write-Host "`n--- Attempting to unlock account for '$UserName' ---" -ForegroundColor Cyan

    # Check if Active Directory module is loaded. If not, try to import it.
    # This module is typically installed as part of RSAT (Remote Server Administration Tools)
    if (-not (Get-Module -Name ActiveDirectory)) {
        Write-Host "Active Directory module not loaded. Attempting to import..." -ForegroundColor Yellow
        try {
            Import-Module ActiveDirectory -ErrorAction Stop
            Write-Host "Active Directory module imported successfully." -ForegroundColor Green
        }
        catch {
            Write-Host "Error: Could not import Active Directory module. This script requires it to be installed and available." -ForegroundColor Red
            Write-Host "If you are not on a Domain Controller or a machine with RSAT installed, this script will not work." -ForegroundColor Red
            return $false
        }
    }

    # Check if the module is available after attempt to import
    if (-not (Get-Module -Name ActiveDirectory)) {
        return $false
    }

    try {
        # Check if the user exists
        $user = Get-ADUser -Identity $UserName -ErrorAction SilentlyContinue

        if ($null -eq $user) {
            Write-Host "Error: User '$UserName' not found in Active Directory." -ForegroundColor Red
            return $false
        }

        # Check if the account is already unlocked
        if ($user.LockedOut -eq $false) {
            Write-Host "Account '$UserName' is not currently locked out." -ForegroundColor Green
            return $true
        }

        # Attempt to unlock the account
        Unlock-ADAccount -Identity $UserName -ErrorAction Stop
        Write-Host "Account '$UserName' has been successfully unlocked." -ForegroundColor Green
        return $true

    }
    catch {
        Write-Host "An error occurred while trying to unlock '$UserName':" -ForegroundColor Red
        Write-Host $_.Exception.Message -ForegroundColor Red
        Write-Host "Ensure you have sufficient permissions and the user exists." -ForegroundColor Red
        return $false
    }
}

# --- Main Script Execution ---

Write-Host "This script attempts to unlock a user account in Active Directory." -ForegroundColor Yellow
Write-Host "NOTE: This requires the Active Directory PowerShell module and administrator privileges." -ForegroundColor Yellow
Write-Host "It will NOT work for local accounts on a standalone PC." -ForegroundColor Yellow

$usernameToUnlock = Read-Host "Enter the username to unlock"

if ([string]::IsNullOrWhiteSpace($usernameToUnlock)) {
    Write-Host "No username entered. Exiting script." -ForegroundColor Red
} else {
    # Call the function to unlock the account
    Unlock-UserAccount -UserName $usernameToUnlock
}