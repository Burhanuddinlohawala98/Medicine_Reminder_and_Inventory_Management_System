# Medicine Reminder & Inventory Management system
# File: medicine.py
# Owner: Hiralal Shah

# Purpose:
# Manage medicine records.

# Responsibilities:
# - Create medicine dictionaries.
# - Update medicine quantity.
# - Delete medicines.
# - view medicines
# - search meidicine

from datetime import datetime
file_name = "accounts.txt"

def add_medicine():
    while True:
        medicine_name = input("Enter medicine name: ")
        if medicine_name == "":
            print("Medicine name cannot be empty")
            continue
        has_letter = False
        for letter in medicine_name:
            if letter.isalpha():
                has_letter = True
                break
        if has_letter:
            break
        else:
            print("Medicine name must contain one alphabet.")

    while True:        
        medicine_quantity = input("Enter medicine quantity: ")
        if medicine_quantity.isdigit() and int(medicine_quantity) > 0:
            break
        else:
            print("Please enter valid medicine quantity")

    while True:
        medicine_expiry_date = input("Enter the expiry date(DD/MM/YYYY): ")
        if len(medicine_expiry_date) == 10 and medicine_expiry_date[2] == "/" and medicine_expiry_date[5] == "/":
            day = medicine_expiry_date[0:2]
            month = medicine_expiry_date[3:5]
            year = medicine_expiry_date[6:10]
            if day.isdigit() and month.isdigit() and year.isdigit():
                break
            print("Invalid date format! Please enter in DD/MM/YYYY format (e.g., 25/12/2025).")


    
    medicine_time = []
    while True:
        print("Select Time Slots")
        print("1. 06 AM - 12 PM")
        print("2. 12 PM - 06 PM")
        print("3. 06 PM - 12 AM")
        print("4. 12 AM - 06 AM")
        print('5. Done')
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                if "06:00 AM - 12:00 PM" not in medicine_time:
                    medicine_time.append('06 AM - 12 PM')
                    print("06 AM - 12 PM Time Slot Selected")
                else:
                    print("Time slot already selected")
            elif choice == 2:
                if "12PM - 06 PM" not in medicine_time:
                    medicine_time.append("12 PM - 06 PM")
                    print("12 PM - 06 PM Time Slot Selected")
                else:
                    print("Time slot already selected")
            elif choice == 3:
                if "06 PM - 12 AM" not in medicine_time:
                    medicine_time.append("06 PM - 12 AM")
                    print("06 PM - 12 AM Time Slot Selected")
                else:
                    print("Time slot already selected")
            elif choice == 4:
                if "12 AM - 06 AM" not in medicine_time:
                    medicine_time.append("12 AM - 06 AM")
                    print("12 AM - 06 AM Time Slot Selected")
                else:
                    print("Time slot already selected")
            elif choice == 5:
                break
            else:
                print('Invalid choice! please try again')
        except ValueError:
            print("Invalid choice! Please enter choices in between 1 to 5")

    medicine_dosage_per_day = len(medicine_time)

        
    return {
        "medicine_name": medicine_name,
        "medicine_quantity": medicine_quantity,
        "medicine_expiry_date": medicine_expiry_date,
        "medicine_dosage_per_day": medicine_dosage_per_day,
        "medicine_timings": medicine_time
    }

def save_medicine(current_user, medicine):
    with open(file_name,'r') as profiles:
        updated_records = []
        for profile in profiles:
            user_info = profile.strip().split(',')
            if current_user == user_info[0]:
                medicine_name = medicine["medicine_name"]
                medicine_quantity = medicine["medicine_quantity"]
                medicine_expiry_date = medicine["medicine_expiry_date"]
                medicine_timings = "/".join(medicine["medicine_timings"])
                medicine_dosage_per_day = medicine["medicine_dosage_per_day"]
                medicine_records = f"{medicine_name},{medicine_quantity},{medicine_expiry_date},{medicine_timings},{medicine_dosage_per_day}"
                if  '|' in profile:
                    updated_profile = profile.strip()+ ';' + medicine_records
                else:
                    updated_profile = profile.strip()+ '|' + medicine_records
                updated_records.append(updated_profile)
            else:
                updated_records.append(profile.strip())
    try:
        with open(file_name,'w') as profiles:
            for user_profile in updated_records:
                profiles.write(user_profile + "\n")
        print("Medicine added successfully!")
    except FileNotFoundError:
        print("Records Not Found")



def delete_medicine(current_user):
    try:
        user_found = False
        user_has_medicines = False

        # Step 1: Read file first to check user profile and medicine existence
        with open(file_name, 'r') as profiles:
            for profile in profiles:
                profile = profile.strip()
                if profile == "":
                    continue

                medicine_info = profile.split("|")
                user_profiles = medicine_info[0].split(',')

                if len(user_profiles) > 0 and (current_user == user_profiles[0] or current_user == user_profiles[1]):
                    user_found = True
                    if len(medicine_info) > 1 and medicine_info[1].strip() != "":
                        user_has_medicines = True
                    break

        # Step 2: Early exits BEFORE asking for input
        if not user_found:
            print("User profile not found.")
            return

        if not user_has_medicines:
            print("No medicines found! Please add some medicine first to delete medicine.")
            return

        # Step 3: Prompt for input ONLY if medicines exist
        while True:
            medicine_name = input("Enter medicine name to delete: ").strip()
            if medicine_name == "":
                print("Please enter medicine name, medicine name cannot be empty")
            else:
                break

        updated_records = []
        medicine_found = False

        # Step 4: Re-open file to remove target medicine and save updated structure
        with open(file_name, 'r') as profiles:
            for profile in profiles:
                profile = profile.strip()
                if profile == "":
                    continue

                medicine_info = profile.split('|')
                user_profiles = medicine_info[0].split(',')

                if len(user_profiles) > 0 and (current_user == user_profiles[0] or current_user == user_profiles[1]):
                    current_user_medicines_list = medicine_info[1].split(';') if len(medicine_info) > 1 else []
                    updated_medicines_list = []

                    for medicine in current_user_medicines_list:
                        if medicine.strip() == "":
                            continue

                        individual_medicine = medicine.split(',')

                        # Case-insensitive match check
                        if len(individual_medicine) >= 1 and medicine_name.lower() == individual_medicine[0].lower():
                            medicine_found = True  # Skip adding this medicine to updated list
                        else:
                            updated_medicines_list.append(medicine)

                    if medicine_found:
                        updated_medicine_str = ";".join(updated_medicines_list)
                        if updated_medicine_str != "":
                            updated_profile = f"{medicine_info[0]}|{updated_medicine_str}"
                        else:
                            updated_profile = medicine_info[0]  # Remove '|' if no medicines left
                        updated_records.append(updated_profile)
                    else:
                        updated_records.append(profile)
                else:
                    updated_records.append(profile)

        # Step 5: Write back updated records
        if medicine_found:
            with open(file_name, 'w') as profiles:
                for profile in updated_records:
                    profiles.write(profile + '\n')
            print("Medicine deleted successfully!")
        else:
            print("Medicine not found in your records.")

    except FileNotFoundError:
        print("Records not found")


def view_medicine(current_user):
    try:
        user_found = False
        with open(file_name, 'r') as profiles:
            for profile in profiles:
                profile = profile.strip()
                if profile == "":
                    continue
                
                medicine_info = profile.split("|")
                user_profiles = medicine_info[0].split(',')
            
                if current_user == user_profiles[0]:
                    user_found = True

                    if len(medicine_info) > 1 and medicine_info[1] != "":
                        current_user_medicines_list = medicine_info[1].split(';')
                        for medicine in current_user_medicines_list:
                            individual_medicine = medicine.split(",")
                            if len(individual_medicine) >= 5:
                                print(f"""======== MEDICINE DETAILS========
Medicine Name              : {individual_medicine[0]}
Medicine Quantity          : {individual_medicine[1]}
Medicine Expiry Date       : {individual_medicine[2]}
Medicine Timings           : {individual_medicine[3].split("/")}
Medicine Dosage Per Day    : {individual_medicine[4]}
====================================================""")
                    else:
                        print("No medicine found, Please add some medicine to view medicines.")
                    
                    break  # Stop searching after current_user profile is found and processed
            
            if not user_found:
                print("User profile not found.")

    except FileNotFoundError:
        print("Records Not Found")


def search_medicine(current_user):
    try:
        user_found = False
        user_has_medicines = False
        user_medicines_str = ""

        
        with open(file_name, 'r') as profiles:
            for profile in profiles:
                profile = profile.strip()
                if profile == "":
                    continue

                medicine_info = profile.split("|")
                user_profiles = medicine_info[0].split(',')

                if len(user_profiles) > 0 and (current_user == user_profiles[0] or current_user == user_profiles[1]):
                    user_found = True
                    # Check if medicine section exists and is not empty
                    if len(medicine_info) > 1 and medicine_info[1].strip() != "":
                        user_has_medicines = True
                        user_medicines_str = medicine_info[1]
                    break

        
        if not user_found:
            print("User profile not found.")
            return

        if not user_has_medicines:
            print("No medicine found! Please add some medicine first to search medicine.")
            return

        
        while True:
            medicine_name = input('Enter medicine name: ').strip()
            if medicine_name == "":
                print("Please enter medicine name, medicine name cannot be empty")
            else:
                break

        
        medicine_found = False
        current_user_medicines_list = user_medicines_str.split(';')

        for medicine in current_user_medicines_list:
            if medicine.strip() == "":
                continue

            individual_medicine = medicine.split(",")

            if len(individual_medicine) >= 5 and medicine_name.lower() == individual_medicine[0].lower():
                medicine_found = True
                print(f"""======== MEDICINE DETAILS FOR {current_user} ========
Medicine Name              : {individual_medicine[0]}
Medicine Quantity          : {individual_medicine[1]}
Medicine Expiry Date       : {individual_medicine[2]}
Medicine Timings           : {individual_medicine[3].split("/")}
Medicine Dosage Per Day    : {individual_medicine[4]}
=====================================================""")
                break

        if not medicine_found:
            print('Medicine not found!')

    except FileNotFoundError:
        print("Records not found")


def update_medicine(current_user):
    try:
        user_found = False
        user_has_medicines = False

        # Step 1: Read file first to verify user and check if medicines exist
        with open(file_name, 'r') as profiles:
            for profile in profiles:
                profile = profile.strip()
                if profile == "":
                    continue

                medicine_info = profile.split("|")
                user_profiles = medicine_info[0].split(',')

                if len(user_profiles) > 0 and (current_user == user_profiles[0] or current_user == user_profiles[1]):
                    user_found = True
                    if len(medicine_info) > 1 and medicine_info[1].strip() != "":
                        user_has_medicines = True
                    break

        # Step 2: Early exits BEFORE asking for input
        if not user_found:
            print("User profile not found.")
            return

        if not user_has_medicines:
            print("No medicine found! Please add some medicine first to update medicine.")
            return

        # Step 3: Ask for target medicine name only if medicines exist
        while True:
            medicine_name = input("Enter medicine name to update: ").strip()
            if medicine_name == "":
                print("Please enter medicine name, medicine name cannot be empty")
            else:
                break

        updated_records = []
        medicine_found = False

        # Step 4: Re-open file to process and write updates
        with open(file_name, 'r') as profiles:
            for profile in profiles:
                profile = profile.strip()
                if profile == "":
                    continue

                medicine_info = profile.split("|")
                user_profiles = medicine_info[0].split(',')

                if len(user_profiles) > 0 and (current_user == user_profiles[0] or current_user == user_profiles[1]):
                    current_user_medicines_list = medicine_info[1].split(';')
                    updated_medicines_list = []

                    for medicine in current_user_medicines_list:
                        if medicine.strip() == "":
                            continue

                        individual_medicine = medicine.split(",")

                        if len(individual_medicine) >= 5 and medicine_name.lower() == individual_medicine[0].lower():
                            medicine_found = True
                            print(f"\nFound '{individual_medicine[0]}'. Enter new details below:")

                            # Validations for updated details
                            while True:
                                new_quantity = input("Enter new quantity: ").strip()
                                if new_quantity == "":
                                    print("Quantity cannot be empty.")
                                else:
                                    break

                            while True:
                                new_expiry = input("Enter new expiry date (DD/MM/YYYY): ").strip()
                                if new_expiry == "":
                                    print("Expiry date cannot be empty.")
                                else:
                                    break

                            while True:
                                new_timings = input("Enter new timings (separated by /): ").strip()
                                if new_timings == "":
                                    print("Timings cannot be empty.")
                                else:
                                    break

                            while True:
                                new_dosage = input("Enter new dosage per day: ").strip()
                                if new_dosage == "":
                                    print("Dosage cannot be empty.")
                                else:
                                    break

                            # Preserve the original medicine name, update the rest
                            updated_med_entry = f"{individual_medicine[0]},{new_quantity},{new_expiry},{new_timings},{new_dosage}"
                            updated_medicines_list.append(updated_med_entry)
                        else:
                            updated_medicines_list.append(medicine)

                    # Reconstruct profile record
                    joined_medicines = ";".join(updated_medicines_list)
                    updated_profile = f"{medicine_info[0]}|{joined_medicines}"
                    updated_records.append(updated_profile)
                else:
                    updated_records.append(profile)

        # Step 5: Save changes back to file if medicine was matched
        if medicine_found:
            with open(file_name, 'w') as profiles:
                for profile in updated_records:
                    profiles.write(profile + '\n')
            print("Medicine updated successfully!")
        else:
            print("Medicine not found in your records.")

    except FileNotFoundError:
        print("Record not found")