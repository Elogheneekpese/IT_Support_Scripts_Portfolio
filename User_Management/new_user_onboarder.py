import os
import csv
import random
import string
from datetime import datetime

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

def create_user_folder(username):
    base_path = os.path.join(os.getcwd(), "New_Users")
    os.makedirs(base_path, exist_ok=True)

    user_folder = os.path.join(base_path, username)
    os.makedirs(user_folder, exist_ok=True)

    return user_folder

def write_welcome_file(folder_path, username, password):
    welcome_message = f"""\
Welcome {username}!

Your account has been created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.

Temporary Password: {password}

Please change your password on first login.

- IT Support Team
"""
    with open(os.path.join(folder_path, "welcome.txt"), "w") as file:
        file.write(welcome_message)

def write_checklist_file(folder_path):
    checklist = """\
 Onboarding Checklist:
 - [ ] Add to domain
 - [ ] Configure email account
 - [ ] Install required software
 - [ ] Grant folder permissions
 - [ ] Email welcome message
"""
    with open(os.path.join(folder_path, "checklist.txt"), "w") as file:
        file.write(checklist)

def log_to_csv(username, password):
    log_path = os.path.join(os.getcwd(), "user_log.csv")
    file_exists = os.path.isfile(log_path)

    with open(log_path, "a", newline="") as csvfile:
        fieldnames = ["Username", "Password", "Created_At"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Username": username,
            "Password": password,
            "Created_At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

def new_user_onboarder():
    print("\n👤 New User Onboarding Script")
    username = input("Enter the new user's username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    print(f"\nCreating folder for {username}...")
    folder_path = create_user_folder(username)

    print("Generating a temporary password...")
    password = generate_password()

    print("Writing welcome file and IT checklist...")
    write_welcome_file(folder_path, username, password)
    write_checklist_file(folder_path)

    print("Logging user to CSV...")
    log_to_csv(username, password)

    print(f"\nOnboarding complete for '{username}'!")
    print(f"User folder created at: {folder_path}")
    print("Welcome file, checklist, and user log have been created.")

if __name__ == "__main__":
    new_user_onboarder()
