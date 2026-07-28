# Medicine Reminder & Inventory Manager
# File: user_profile.py
# Owner: Burhanuddin Lohawala

# Purpose:
# Manage all user profile operations.

# Responsibilities:
# - Create new user profiles.
# - Login existing users.
# - Store and retrieve profile information.
# - Read and write profiles.json.


# Login_function 
def login_function():
    while True:
        print("====Login using=====")
        print("1. Email Address")
        print("2. Phone Number")
        print("3. Create an account")
        print("4. Exit")



        try:
            # Taking user input for menu choice
            login_choice = int(input("Enter your Login choice: "))



            # if user choose email for login
            if login_choice == 1: 
                email_address = input("Enter your Email: ").strip() 

                # Input validation for email
                if len(email_address) > 0 and "@" in email_address and '.com' in email_address:
                    password = input("Enter your Password: ").strip()

                    # input validation for password
                    if len(password) >= 8 and password[0].isupper():
                            return {
                                "action":"login_email",
                                "email":email_address,
                                "password":password
                                }
                    else:
                        print("Error! Please enter password again")
                else:
                    print("Invalid email! Please try again.")



            # if user choose phone option for login
            elif login_choice == 2:
                phone_number = input("Enter your Phone number: ").strip()

                # Phone number validation
                if len(phone_number) == 10 and phone_number.isdigit():
                    password = input("Enter your Password: ").strip()

                    # password validation
                    if len(password) >= 8 and password[0].isupper():
                        return{
                            "action":"login_phone",
                            "phone":phone_number,
                            "password":password
                            }
                    else:
                        print("incorrect! Password please try again")
                else:
                    print("Please enter valid Phone address")
                        



            # if user choose create accouont option 
            elif login_choice == 3:
                user_name = input("Enter your Name: ").strip()

                # name validation
                if user_name.replace(" ","").isalpha():
                    user_email = input("Enter your Email: ").strip()

                    # email validation
                    if len(user_email) > 0 and "@" in user_email and ".com" in user_email:
                        user_phone_number = input("Enter your Phone number: ").strip()

                        # phone number validation
                        if len(user_phone_number) == 10 and user_phone_number.isdigit():
                                while True:
                                    create_password = input("Create a password: ").strip()

                                    # password validation
                                    if len(create_password) >= 8 and create_password[0].isupper():
                                        confirm_password = input("Enter your password again: ").strip()

                                        # matching create password with confirm password
                                        if create_password == confirm_password:
                                            print("Password created successfully!")
                                            return{
                                                "action":"create_account",
                                                "name":user_name,
                                                "email":user_email,
                                                "phone":user_phone_number,
                                                "password":create_password,
                                                } 
                                        else:
                                            print("Password does not match")
                                    else:
                                        print('Invalid Password! Please try again.')
                        else:
                            print("Error! Please enter phone number again.")
                    else:
                        print("Error! Please enter valid email.")
                else:
                    print("Error! Please enter valid name.")




            # if user choose exit option
            elif login_choice == 4:
                return None
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid entry please try again.")




# Importing Json
import json


# Load_profiles function
def load_profiles():
    try:
        with open("storage.json",'r') as profiles:
            users_data = json.load(profiles)
            return users_data
    except FileNotFoundError:
        print("Profile file not found.")
        return {}
    except json.JSONDecodeError:
        print("Profile file is empty.")
        return {}
    
# save_profile function
def save_profiles(user_profiles):
    with open("storage.json","w") as profiles:
        json.dump(user_profiles,profiles, indent=4)
            

# Create account function
def create_account(user_data):
    profiles = load_profiles()

    # cheching if email already exists 
    if user_data["email"] in profiles:
        print("Email already exists.")
        return
        
    for email in profiles:
        if profiles[email]['phone'] == user_data['phone']:
            print("Phone number already exists")
            return
    
    profiles[user_data["email"]] = user_data
    save_profiles(profiles)
    print("Account created successfully.")



# Login by email
def login_by_email(user_data):
    user_profiles = load_profiles()
    if user_data['email'] in user_profiles:
        if user_data['password'] == user_profiles[user_data['email']]['password']:
            print("Login successful")
            return user_profiles[user_data["email"]]
        else:
            print('Incorrect password! Please try again')
    else:
        print("Email does not exists.")



# Login by phone
def login_by_phone(user_data):
    user_profiles = load_profiles()
    found = False
    for email in user_profiles:
        if user_profiles[email]['phone'] == user_data['phone']:
            if user_data['password'] == user_profiles[email]["password"]:
                print("Login successful!")
                found = True
                return user_profiles[email]
            else:
                print("Password incorrect! Please try again.")