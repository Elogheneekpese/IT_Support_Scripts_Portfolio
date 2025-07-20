import socket
import subprocess
import platform

def dns_lookup(domain="google.com"):
    print(f"\n🔍 Looking up DNS info for: {domain}")

    try:
        ip = socket.gethostbyname(domain)
        print(f"✅ {domain} resolved to IP: {ip}")
    except socket.gaierror:
        print(f"❌ Could not resolve {domain}. DNS might be broken.")

def run_nslookup(domain="google.com"):
    print("\n🛠 Running nslookup...")

    try:
        if platform.system() == "Windows":
            result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
        else:
            result = subprocess.run(["nslookup", domain], capture_output=True, text=True)

        print(result.stdout)
    except Exception as e:
        print(f"Error running nslookup: {e}")

def flush_dns_cache():
    print("\n🧹 Flushing DNS cache...")

    try:
        if platform.system() == "Windows":
            subprocess.run(["ipconfig", "/flushdns"])
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"])
        else:  # Linux
            subprocess.run(["sudo", "systemd-resolve", "--flush-caches"])
        print("✅ DNS cache flushed.")
    except Exception as e:
        print(f"⚠️ Could not flush DNS cache: {e}")

if __name__ == "__main__":
    domain = input("🌐 Enter a domain to check (e.g. google.com): ").strip()
    if not domain:
        domain = "google.com"

    dns_lookup(domain)
    run_nslookup(domain)

    flush_choice = input("\nDo you want to flush DNS cache? (y/n): ").strip().lower()
    if flush_choice == 'y':
        flush_dns_cache()
