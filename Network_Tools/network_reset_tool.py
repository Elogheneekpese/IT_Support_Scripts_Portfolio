import subprocess  # To run system commands
import platform    # To check the operating system
import os          # Needed to check for files (like DNS cache services)

def run_command(command, description):
    """Executes a shell command and prints its output. Returns True if successful."""
    print(f"\n--- {description} ---")
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8',
            errors='replace'
        )
        print(result.stdout)
        if result.stderr:
            print(f"Error Output:\n{result.stderr}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: '{command}'")
        print(f"Return Code: {e.returncode}")
        print(f"Error Output (stderr):\n{e.stderr}")
        print(f"Standard Output (stdout):\n{e.stdout}")
        return False
    except FileNotFoundError:
        print(f"Command not found: '{command.split(' ')[0]}'. Make sure it's in your system's PATH.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def network_reset_tool():
    """Performs a series of network resets based on the operating system."""
    print("--- Initiating Network Reset Process ---")

    if platform.system() == "Windows":
        print("\nApplying Windows network reset commands...")
        run_command("ipconfig /release", "Releasing current IP address")
        run_command("ipconfig /renew", "Renewing IP address")
        run_command("ipconfig /flushdns", "Flushing DNS resolver cache")

        print("\nNOTE: 'netsh winsock reset' and 'netsh int ip reset' often require a system restart.")
        run_command("netsh winsock reset", "Resetting Winsock Catalog")
        run_command("netsh int ip reset", "Resetting TCP/IP stack")

        print("\nWindows network reset commands executed. Please consider restarting your computer.")
        print("This tool attempts to reset common network components. If issues persist, further diagnosis may be needed.")

    elif platform.system() in ["Linux", "Darwin"]:
        print("\nApplying Linux/macOS network reset commands...")
        print("Note: You may be prompted for your password if using sudo.")

        run_command("sudo ip link set dev eth0 down && sudo ip link set dev eth0 up", "Resetting Ethernet Interface (eth0 - common)")
        run_command("sudo systemctl restart NetworkManager", "Restarting NetworkManager (if present)")
        run_command("sudo service networking restart", "Restarting Networking Service (older systems)")

        if platform.system() == "Darwin":
            run_command("sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder", "Flushing DNS Cache (macOS)")
        elif os.path.exists("/etc/init.d/nscd"):
            run_command("sudo /etc/init.d/nscd restart", "Restarting NSCD (DNS cache service)")
        else:
            print("No common DNS cache service found to flush on Linux.")
            print("Consider restarting your browser or system for DNS changes to take effect.")

        print("\nLinux/macOS network reset commands executed. Restarting your computer is recommended.")
        print("This tool attempts to reset common network components. If issues persist, further diagnosis may be needed.")

    else:
        print(f"Operating system '{platform.system()}' not supported by this script.")
        print("This script is designed for Windows, Linux, and macOS.")

    print("\n--- Network Reset Process Complete ---")

if __name__ == "__main__":
    network_reset_tool()
