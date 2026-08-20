# Medicine Reminder & Inventory Manager
# File: user_profile.py
# Owner: Bibin Rufaz L
# Purpose:
# Manage all user profile operations.

# Responsibilities:
# - Create new user profiles.
# - Login existing users.
# - Store and retrieve profile information.
# - Read and write profiles.
# user_profile.py


# Storage for accounts using a dictionary:
# Dictionary structure: {login_id: {"password": password, "username": username, "dob": dob, "gender": gender}}

accounts = {}

FILE_NAME = "accounts.txt"


def load_accounts():
    # Automatically creates the file if it does not exist and closes it in a single line
    with open(FILE_NAME, "a"):
        pass

    # Opens and reads the file, automatically closing it when finished
    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split("|")[0]
            if line != "":
                parts = line.split(",")
                if len(parts) == 5:
                    login_id = parts[0]
                    password = parts[1]
                    username = parts[2]
                    dob = parts[3]
                    gender = parts[4]
                    accounts[login_id] = {
                        "password": password,
                        "username": username,
                        "dob": dob,
                        "gender": gender,
                    }


def save_account(login_id, password, username, dob, gender):
    with open(FILE_NAME, "a") as file:
        file.write(
            login_id
            + ","
            + password
            + ","
            + username
            + ","
            + dob
            + ","
            + gender
            + "\n"
        )


def create_account():
    print("CREATE ACCOUNT")

    print("Choose account creation method:")
    print("1. Email ID")
    print("2. Phone Number")

    mode = input("Enter choice (1 or 2): ").strip()

    if mode == "1":
        login_id = input("Enter your email ID: ").strip()
    elif mode == "2":
        login_id = input("Enter your phone number: ").strip()
    else:
        print("Invalid option selected!")
        return

    if login_id == "":
        print("Error: Email or Phone Number cannot be empty!")
        return

    # Check if this email/phone number is already registered using dictionary lookup
    if login_id in accounts:
        print("Error: An account with this Email/Phone already exists!")
        return

    username = input("Enter your full name: ").strip()
    dob = input("Enter your date of birth (e.g., DD/MM/YYYY): ").strip()
    gender = input("Enter your gender: ").strip()

    password = input("Enter a password: ").strip()
    if password == "":
        print("Error: Password cannot be empty!")
        return

    confirm_password = input("Confirm your password: ").strip()
    if password != confirm_password:
        print("Error: Passwords do not match!")
        return

    # Store the account details in the dictionary
    accounts[login_id] = {
        "password": password,
        "username": username,
        "dob": dob,
        "gender": gender,
    }

    # Save details to text file
    save_account(login_id, password, username, dob, gender)

    print("Success! Account created for " + username + ".")


def login():
    print("LOGIN")

    login_id = input("Enter your Email ID or Phone Number: ").strip()
    password = input("Enter your password: ").strip()

    found_account = None

    # Check credentials using dictionary lookup
    if login_id in accounts:
        user_data = accounts[login_id]
        if user_data["password"] == password:
            found_account = user_data

    if found_account is not None:
        print("Welcome back, " + found_account["username"] + "! Login successful.")

        # Display profile details using dictionary keys
        print("USER PROFILE DETAILS")
        print("Username: " + found_account["username"])
        print("Date of Birth: " + found_account["dob"])
        print("Gender: " + found_account["gender"])
        return login_id
    else:
        print("Error: Invalid Email/Phone Number or password.")


def user_profile_menu():
    load_accounts()
    while True:
        print("USER PROFILE SYSTEM")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            current_user= login()
            if current_user!=None:
                return current_user
        elif choice == "2":
            create_account()
        elif choice == "3":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 3.")


if __name__ == "__main__":
    user_profile_menu()