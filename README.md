# IT Support: Automated Troubleshooting Scripts for Common Errors

## Project Overview

This repository contains a collection of simple Python scripts designed to automate the initial troubleshooting steps for common IT support issues. The goal is to provide quick diagnostic tools that can be run by IT technicians (or even end-users with guidance) to quickly identify and suggest solutions for everyday technical problems.

This project demonstrates practical skills in:
* **Scripting & Automation:** Using Python to automate repetitive diagnostic tasks.
* **Problem Solving:** Addressing common user complaints.
* **System Diagnostics:** Gathering relevant system information.
* **Basic Troubleshooting Logic:** Implementing "if-then" scenarios for common fixes.
* **Documentation:** Providing clear instructions and explanations.
* **Version Control:** Using Git and GitHub to manage code.

## Scripts Included:

### 1. `internet_fixer.py` - Internet Connectivity Troubleshooter

* **Problem Addressed:** "My internet isn't working!" or general network connection issues.
* **What it does:**
    * Attempts to ping `google.com` to check external connectivity.
    * Displays local IP configuration (`ipconfig` on Windows, `ip addr show` on Linux/macOS).
    * Provides basic troubleshooting tips if internet connectivity is not detected.
* **How to run:**
    ```bash
    python internet_fixer.py
    ```
* **Expected Output:** Will show success/failure for ping, followed by network adapter details and tips if needed.

---

## How to Use This Repository

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_GITHUB_REPO_URL_HERE]
    cd IT_Support_Scripts_Portfolio # Or whatever you named your folder
    ```
2.  **Run a Script:**
    ```bash
    python <script_name>.py
    # Example: python internet_fixer.py
    ```

## Future Enhancements

This project is continually evolving. I plan to expand this toolkit with additional scripts and guides to cover a wider range of IT support scenarios. My ongoing plans include:

* **Disk Management:** Developing a script for checking disk space and performing routine cleanup of temporary files to improve system performance.
* **Process Monitoring:** Creating a tool to identify and display top running processes, helping diagnose system slowdowns.
* **Software Deployment & Inventory:** Building scripts for automated installation of common applications and verifying their presence.
* **User Account Automation:** Expanding into more advanced user onboarding and offboarding procedures (e.g., account creation/deletion, password resets).
* **Interactive Menu:** Designing a main script with an interactive menu to easily select and run specific troubleshooting tools.

Developed by Eloghene Tracy Ekpese