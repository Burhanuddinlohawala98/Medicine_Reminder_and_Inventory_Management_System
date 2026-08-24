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

# Storage for accounts using a dictionary:
# Dictionary structure: {login_id: {"password": password, "username": username, "dob": dob, "gender": gender}}

accounts = {}

FILE_NAME = "accounts.txt"


def load_accounts():
    # Reads accounts from text file into memory with error handling
    try:
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
    except FileNotFoundError:
        # File doesn't exist yet; create an empty file safely
        try:
            with open(FILE_NAME, "w") as file:
                pass
        except IOError as e:
            print("Error creating file:", e)
    except IOError as e:
        print("Error reading file:", e)


def save_account(login_id, password, username, dob, gender):
    # Appends new user details to text file with error handling
    try:
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
    except IOError as e:
        print("Error saving account to file:", e)


def create_account():
    print("-" * 45)
    print("--- CREATE NEW ACCOUNT ---")
    print("-" * 45)

    # Loop for choosing creation method
    while True:
        print("Choose account creation method:")
        print("1. Email ID")
        print("2. Phone Number")

        mode = input("Enter choice (1 or 2): ").strip()
        if mode == "1" or mode == "2":
            break
        else:
            print("Error: Invalid option selected! Please select 1 or 2.")
            print("-" * 45)

    # Loop for Email or Phone Number input until valid and unique
    while True:
        if mode == "1":
            login_id = input("Enter your email ID: ").strip()
            # Email validation: check if email contains required symbols
            if "@" not in login_id or "." not in login_id:
                print("Error: Invalid Email ID format! Must contain '@' and '.'")
                print("-" * 45)
                continue
        elif mode == "2":
            login_id = input("Enter your phone number: ").strip()
            # Phone validation: check length and ensure all characters are numbers
            is_valid_phone = True
            digits = "0123456789"
            
            if len(login_id) < 10 or len(login_id) > 15:
                is_valid_phone = False
            else:
                for char in login_id:
                    if char not in digits:
                        is_valid_phone = False
                        break

            if not is_valid_phone:
                print("Error: Phone number must contain only numbers and be between 10 and 15 digits!")
                print("-" * 45)
                continue

        # Check if this email/phone number is already registered
        if login_id in accounts:
            print("Error: An account with this Email/Phone already exists! Enter a different one.")
            print("-" * 45)
            continue
        
        break

    # Full Name validation loop (no numbers allowed)
    while True:
        username = input("Enter your full name: ").strip()
        has_number = False
        digits = "0123456789"

        for char in username:
            if char in digits:
                has_number = True
                break

        if username == "" or has_number:
            print("Error: Name cannot be empty and must not contain numbers!")
            print("-" * 45)
        else:
            break

    # Date of Birth validation loop (Format: DD/MM/YYYY)
    while True:
        dob = input("Enter your date of birth (DD/MM/YYYY): ").strip()
        parts = dob.split("/")
        
        is_valid_dob = True
        digits = "0123456789"

        # Ensure exactly three parts are provided
        if len(parts) != 3:
            is_valid_dob = False
        else:
            day, month, year = parts[0], parts[1], parts[2]
            
            # Check length of DD, MM, YYYY
            if len(day) != 2 or len(month) != 2 or len(year) != 4:
                is_valid_dob = False
            else:
                # Ensure all parts contain only numbers
                for text in [day, month, year]:
                    for char in text:
                        if char not in digits:
                            is_valid_dob = False
                            break
                
                # Check calendar range boundaries
                if is_valid_dob:
                    d_num = int(day)
                    m_num = int(month)
                    y_num = int(year)
                    
                    if d_num < 1 or d_num > 31 or m_num < 1 or m_num > 12 or y_num < 1900 or y_num > 2026:
                        is_valid_dob = False

        if not is_valid_dob:
            print("Error: Invalid Date of Birth format! Please enter in DD/MM/YYYY format with valid values.")
            print("-" * 45)
        else:
            break

    # Gender validation loop (must be 'm' or 'f')
    while True:
        gender = input("Enter your gender (M/F): ").strip()
        if gender != "m" and gender != "M" and gender != "f" and gender != "F":
            print("Error: Invalid entry! Gender must be 'M' or 'F'.")
            print("-" * 45)
        else:
            break

    # Password validation loop
    print("-" * 45)
    print("Password Rules: 6 to 16 characters & at least 1 uppercase letter.")
    
    while True:
        password = input("Enter password: ").strip()

        # Check length range between 6 and 16
        is_length_valid = 6 <= len(password) <= 16

        # Check for uppercase character presence
        has_uppercase = False
        uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in password:
            if char in uppercase_chars:
                has_uppercase = True
                break

        if not is_length_valid or not has_uppercase:
            print("Error: Password must be 6 to 16 characters long and contain at least one uppercase letter!")
            print("-" * 45)
            continue

        confirm_password = input("Confirm your password: ").strip()
        if password != confirm_password:
            print("Error: Passwords do not match!")
            print("-" * 45)
            continue
        else:
            break

    # Store the account details in the dictionary
    accounts[login_id] = {
        "password": password,
        "username": username,
        "dob": dob,
        "gender": gender,
    }

    # Save details to text file
    save_account(login_id, password, username, dob, gender)

    print("-" * 45)
    print("Success! Account created for " + username + ".")
    print("-" * 45)


def login():
    print("-" * 45)
    print("--- USER LOGIN ---")
    print("-" * 45)

    # Loop until valid login details are supplied
    while True:
        login_id = input("Enter your Email ID or Phone Number: ").strip()
        password = input("Enter your password: ").strip()

        found_account = None

        # Check credentials using dictionary lookup
        if login_id in accounts:
            user_data = accounts[login_id]
            if user_data["password"] == password:
                found_account = user_data

        if found_account is not None:
            print("-" * 45)
            print("Welcome back, " + found_account["username"] + "! Login successful.")
            print("-" * 45)

            # Display profile details using dictionary keys
            # print("--- USER PROFILE DETAILS ---")
            # print("Username: " + found_account["username"])
            # print("Date of Birth: " + found_account["dob"])
            # print("Gender: " + found_account["gender"])
            # print("-" * 45)
            return login_id
        else:
            print("Error: Invalid Email/Phone Number or password! Please try again.")
            print("-" * 45)


def user_profile_menu():
    load_accounts()
    while True:
        print("\n" + "=" * 45)
        print("--- MEDICINE REMINDER: USER PROFILE SYSTEM ---")
        print("=" * 45)
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        print("-" * 45)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            current_user = login()
            if current_user != None:
                return current_user
        elif choice == "2":
            create_account()
        elif choice == "3":
            print("-" * 45)
            print("Thank you for using the system. Goodbye!")
            print("-" * 45)
            break
        else:
            print("Error: Invalid choice! Please select an option between 1 and 3.")


if __name__ == "__main__":
    user_profile_menu()