IT Support Scripts Portfolio
Automated Tools for Helpdesk and Junior SysAdmins

Overview
This portfolio is a practical collection of Python and PowerShell tools designed to automate routine IT support tasks. It includes system diagnostics, network resets, user management, app deployment, and Markdown guides: ideal for showcasing real-world support experience.

Skills Demonstrated
Python scripting for automation and troubleshooting

PowerShell for Windows and Active Directory tasks

Network, system, and user account diagnostics

Software installation via Winget

Technical documentation using Markdown

Git and GitHub version control

Folder Structure
IT_Support_Scripts_Portfolio/
├── Core_Utilities/
│   ├── system_info_collector.py
│   ├── temp_file_cleaner.py
│   └── service_checker.py
├── Network_Tools/
│   ├── internet_fixer.py
│   ├── network_reset_tool.py
│   └── dns_diagnostic.py
├── User_Management/
│   ├── new_user_onboarder.py  # Script for new user setup
│   └── account_unlocker.ps1
├── Software_Management/
│   ├── app_checker.py
│   ├── program_uninstaller.py
│   └── app_installer.py
├── Troubleshooting_Guides/
│   ├── Printer_Troubleshooting_Guide.md
│   └── VPN_Connection_Fixes.md
└── README.md

Script Highlights
Core Utilities
system_info_collector.py: Gathers CPU, RAM, disk, and OS info

temp_file_cleaner.py: Cleans temp folders to free up space

service_checker.py: Checks status of important Windows services

Network Tools
internet_fixer.py: Tests and fixes internet connection

network_reset_tool.py: Resets IP, DNS, and adapter settings

dns_diagnostic.py: Diagnoses DNS issues and resolution problems

User Management
new_user_onboarder.py: Creates a folder and welcome file for new users

(Note: This script's detailed functionality is assumed based on its name. If you have specific details, you can expand this description.)

account_unlocker.ps1: Unlocks locked Active Directory accounts

Software Management
app_checker.py: Checks if common apps are installed

program_uninstaller.py: Lists installed programs and initiates uninstallation (Windows)

app_installer.py: Installs apps via Winget silently

Troubleshooting Guides
Markdown documents for printable or shareable step-by-step user help:

Printer_Troubleshooting_Guide.md: Fixes for common printer problems

(Note: This guide's detailed content is a placeholder. If you've created content for it, you can expand this description.)

VPN_Connection_Fixes.md: Deep dive into VPN errors and fixes

How to Run
General Prerequisites
Windows Operating System: All scripts are primarily designed for Windows environments.

Python 3: Ensure Python 3 is installed and added to your system's PATH.

Windows PowerShell: Required for .ps1 scripts.

Administrator Privileges: Many scripts require the PowerShell or Command Prompt window to be run "As Administrator" for full functionality.

RSAT (Remote Server Administration Tools): For Active Directory-specific PowerShell scripts (account_unlocker.ps1), ensure RSAT: Active Directory Domain Services and Lightweight Directory Services Tools is installed via Windows Optional Features or Add-WindowsCapability.

Winget: For app_installer.py, ensure Windows Package Manager (Winget) is installed.

Executing Scripts
Clone the Repository (if on a new machine):

git clone https://github.com/Elogheneekpese/IT_Support_Scripts_Portfolio
cd IT_Support_Scripts_Portfolio

Open your Terminal: Use PowerShell for .ps1 scripts and either PowerShell or Git Bash (or Command Prompt) for .py scripts. Ensure it's run As Administrator for scripts requiring elevated privileges.

Navigate to the Script's Directory:

# Example for a Python script in Core_Utilities
cd Core_Utilities
```bash
# Example for a PowerShell script in User_Management
cd User_Management

Run the Script:

For Python Scripts (.py):

python <script_name>.py
# Example: python system_info_collector.py

For PowerShell Scripts (.ps1):

.\<script_name>.ps1
# Example: .\account_unlocker.ps1

Created By
Eloghene Tracy Ekpese
IT Support Specialist | Automation Enthusiast | Junior SysAdmin
