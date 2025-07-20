import subprocess # This module helps us run commands like you would in the terminal
import platform   # To check if we are on Windows, Linux, or macOS

def check_service_status(service_name):
    """Checks the status of a specific system service."""
    print(f"\n--- Checking status of '{service_name}' service ---")

    if platform.system() == "Windows":
        # On Windows, we use the 'sc query' command to check service status.
        # 'sc' stands for Service Control.
        command = ["sc", "query", service_name]
        try:
            # subprocess.run executes the command.
            # capture_output=True means we want to grab the text that the command prints.
            # text=True decodes the output as readable text.
            # check=True means if the command fails (returns an error), Python will raise an error.
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            output = result.stdout.lower() # Convert all output to lowercase to make checking easier

            if "running" in output:
                print(f"Service '{service_name}' is RUNNING.")
                return True # Return True if the service is running
            elif "stopped" in output:
                print(f"Service '{service_name}' is STOPPED.")
                return False # Return False if the service is stopped
            else:
                print(f"Could not determine status for '{service_name}'. Here's the output:\n{result.stdout}")
                return None # Return None if status is unknown
        except subprocess.CalledProcessError as e:
            # This error happens if 'sc' command itself had an issue (e.g., service not found)
            print(f"Error querying service '{service_name}': Service might not exist or permission denied.")
            print(f"Error output:\n{e.stderr}")
            return None
        except FileNotFoundError:
            # This error happens if 'sc' command isn't found (e.g., running on wrong OS)
            print("Error: 'sc' command not found. Are you sure you are on a Windows operating system?")
            return None
    else: # This block is for Linux or macOS
        # For modern Linux systems that use systemd (most common nowadays).
        # We use 'systemctl is-active' to check if a service is active (running).
        command = ["systemctl", "is-active", service_name]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            # If 'systemctl is-active' outputs 'active', the service is running
            if "active" in result.stdout.lower():
                print(f"Service '{service_name}' is RUNNING.")
                return True
            else:
                # If it outputs anything else (e.g., 'inactive', 'failed'), it's not running
                print(f"Service '{service_name}' is STOPPED or inactive. Here's the output:\n{result.stdout}")
                return False
        except subprocess.CalledProcessError as e:
            # This error often means the service doesn't exist or permissions are an issue
            print(f"Error querying service '{service_name}': Service might not exist or permission denied.")
            print(f"Error output:\n{e.stderr}")
            return None
        except FileNotFoundError:
            print("Error: 'systemctl' command not found. Are you sure you are on a Linux system with systemd?")
            return None

def main():
    """Main function to prompt for service name and check its status."""
    print("This script helps you check the status (Running/Stopped) of a specific system service.")
    service_name = input("Enter the name of the service to check (e.g., 'Spooler' for Windows, 'apache2' for Linux): ")

    if service_name: # Check if the user actually typed something
        check_service_status(service_name.strip()) # .strip() removes any extra spaces
    else:
        print("No service name entered. Please try again.")

# This line makes sure the 'main()' function runs when you execute the script directly
if __name__ == "__main__":
    main()