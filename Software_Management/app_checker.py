import shutil

def check_app(app_name, command):
    print(f"\nChecking for {app_name}...")

    if shutil.which(command):
        print(f"{app_name} is installed and available in PATH.")
    else:
        print(f"{app_name} is NOT installed or not in PATH.")

def main():
    print("Installed Applications Checker\n")

    # Define the apps to check: (Name, command to look for)
    apps_to_check = [
        ("Google Chrome", "chrome"),
        ("Mozilla Firefox", "firefox"),
        ("Zoom", "zoom"),
        ("Microsoft Teams", "teams"),
        ("VLC Media Player", "vlc"),
        ("Python", "python")
    ]

    for app_name, command in apps_to_check:
        check_app(app_name, command)

    print("\nSoftware check complete.")

if __name__ == "__main__":
    main()
