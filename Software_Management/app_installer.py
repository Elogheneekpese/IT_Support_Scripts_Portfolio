import subprocess

# List of apps to install (Display name, Winget package ID)
apps_to_install = [
    ("Google Chrome", "Google.Chrome"),
    ("Zoom", "Zoom.Zoom"),
    ("VLC Media Player", "VideoLAN.VLC"),
    ("Microsoft Teams", "Microsoft.Teams")
]

def install_app(name, package_id):
    print(f"\n📦 Installing {name}...")

    try:
        # Winget command with necessary arguments
        command = [
            "winget", "install", "--id", package_id,
            "-e",  # Exact match
            "--silent",
            "--accept-source-agreements",
            "--accept-package-agreements",
            "--force"
        ]
        
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8',
            errors='replace'
        )
        print(f"✅ {name} installed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {name}.")
        print("Error details:")
        if e.stderr:
            print("  (Stderr):", e.stderr)
        if e.stdout:
            print("  (Stdout):", e.stdout)
        if not e.stderr and not e.stdout:
            print("  No additional output. Possible UAC prompt or network issue.")

    except FileNotFoundError:
        print("❌ Error: 'winget' command not found. Ensure Winget is installed and in your system PATH.")

    except Exception as e:
        print(f"❌ Unexpected error while installing {name}: {e}")

def main():
    print("🚀 Starting application installations using Python + Winget...\n")

    # Confirm winget is available
    try:
        subprocess.run(["winget", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("🚨 Winget is not available on this system.")
        print("Please install it from the Microsoft Store (App Installer) before proceeding.")
        return

    for app_name, package_id in apps_to_install:
        install_app(app_name, package_id)

    print("\n✅ All installations attempted. Review the output above.")

if __name__ == "__main__":
    main()
