import os
import platform

def run_command(command):
    """Runs a shell command and returns its output and success status."""
    print(f"\n--- Running: {command} ---")
    result = os.system(command)
    return result == 0

def check_internet_connectivity():
    """Checks basic internet connectivity."""
    print("Checking internet connectivity...")

    # Determine the ping command based on the operating system
    if platform.system() == "Windows":
        ping_command = "ping -n 1 google.com" # -n 1 means send 1 packet
        ip_command = "ipconfig"
    else: # Linux or macOS
        ping_command = "ping -c 1 google.com" # -c 1 means send 1 packet
        ip_command = "ip addr show" # or 'ifconfig' on older systems

    # Try to ping Google
    if run_command(ping_command):
        print("SUCCESS: Google.com is reachable! Your internet seems to be working.")
        print("Let's check your IP address too:")
        run_command(ip_command) # Show IP config even if ping succeeds
    else:
        print("FAILURE: Cannot reach google.com. Internet connection issues suspected.")
        print("Let's check your computer's network setup:")
        run_command(ip_command) # Show IP config if ping fails
        print("\n--- Basic Troubleshooting Tips ---")
        print("1. Is your network cable plugged in tightly? (if wired connection)")
        print("2. Is your Wi-Fi turned on? Are you connected to the right network?")
        print("3. Try restarting your router/modem.")
        print("4. Restart your computer.")
        print("5. Call your internet provider if none of the above work.")

# This is like the main starting point of our script
if __name__ == "__main__":
    check_internet_connectivity()
    print("\n--- End of Internet Connectivity Check ---")