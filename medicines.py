# Medicine Reminder & Inventory Manager
# File: medicine.py
# Owner: Hiralal Shah

# Purpose:
# Manage medicine records.

# Responsibilities:
# - Create medicine dictionaries.
# - Update medicine quantity.
# - Delete medicines.
# - view medicines
# - search medicine

file_name = "accounts.txt"

def add_medicine():
    medicine_name = input("Enter medicine name: ")
    medicine_quantity = input("Enter medicine quantity: ")
    medicine_expiry_date = input("Enter the expiry date(DD/MM/YYYY): ")
    
    medicine_time = []
    while True:
        print("Select Time Slots")
        print("1. 06:00 AM - 12:00 PM")
        print("2. 12:00 PM - 06:00 PM")
        print("3. 06:00 PM - 12:00 AM")
        print("4. 12:00 AM - 06:00 AM")
        print('5. Done')
        choice = int(input("Enter choice: "))
        if choice == 1:
            if "06:00 AM - 12:00 PM" not in medicine_time:
                medicine_time.append('06:00 AM - 12:00 PM')
                print("06:00 AM - 12:00 PM Time Slot Selected")
            else:
                print("Time slot already selected")
        elif choice == 2:
            if "12:00 PM - 06:00 PM" not in medicine_time:
                medicine_time.append("12:00 PM - 06:00 PM")
                print("12:00 PM - 06:00 PM Time Slot Selected")
            else:
                print("Time slot already selected")
        elif choice == 3:
            if "06:00 PM - 12:00 AM" not in medicine_time:
                medicine_time.append("06:00 PM - 12:00 AM")
                print("06:00 PM - 12:00 AM Time Slot Selected")
            else:
                print("Time slot already selected")
        elif choice == 4:
            if "12:00 AM - 06:00 AM" not in medicine_time:
                medicine_time.append("12:00 AM - 06:00 AM")
                print("12:00 AM - 06:00 AM Time Slot Selected")
            else:
                print("Time slot already selected")
        elif choice == 5:
            break
        else:
            print('Invalid choice! please try again')

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

    with open(file_name,'w') as profiles:
        for user_profile in updated_records:
            profiles.write(user_profile + "\n")
    print("Medicine added successfully!")


def delete_medicine(current_user):
    medicine_name = input("Enter medicine name: ")
    with open(file_name, 'r') as profiles:
        updated_records = []
        medicine_found = False
        for profile in profiles:
            profile = profile.strip()
            medicine_info = profile.split('|')
            user_profiles = medicine_info[0].split(',')
            current_user_medicines_list = medicine_info[1].split(';')
            if current_user == user_profiles[0]:
                for medicine in current_user_medicines_list:
                    individual_medicine = medicine.split(',')
                    if medicine_name == individual_medicine[0]:
                        medicine_found = True
                        current_user_medicines_list.remove(medicine)
                        updated_medicine_list = ";".join(current_user_medicines_list)
                        if updated_medicine_list:
                            updated_profile = f"{medicine_info[0]}|{updated_medicine_list}"
                        else:
                            updated_profile = medicine_info[0]
                        break
                if medicine_found:
                    updated_records.append(updated_profile)
                else:
                    updated_records.append(profile)
            else:
                updated_records.append(profile)

        with open(file_name,'w') as profiles:
            for profile in updated_records:
                profiles.write(profile + '\n')

        
        if medicine_found:
            print("Medicine deleted successfully!")
        else:
            print("Medicine not found!")


def view_medicine(current_user):
    with open(file_name,'r') as profiles:
        for profile in profiles:
            profile = profile.strip()
            medicine_info = profile.split("|")
            user_profiles = medicine_info[0].split(',')
            
            if current_user == user_profiles[0]:
                current_user_medicines_list = medicine_info[1].split(';')
                for medicine in current_user_medicines_list:
                    individual_medicine = medicine.split(",")
                    print("Medicine Name:", individual_medicine[0])
                    print("Quantity:", individual_medicine[1])
                    print("Expiry Date:", individual_medicine[2])
                    print("Timings:", individual_medicine[3].split('/'))
                    print("Dosage Per Day:", individual_medicine[4])
                    print("-" * 30)


def search_medicine(current_user):
    medicine_name = input('Enter medicine name: ')
    medicine_found = False
    with open(file_name,'r') as profiles:
        for profile in profiles:
            profile = profile.strip()
            medicine_info = profile.split("|")
            user_profiles = medicine_info[0].split(',')
            current_user_medicines_list = medicine_info[1].split(';')
            if current_user == user_profiles[0]:
                for medicine in current_user_medicines_list:
                    individual_medicine = medicine.split(",")
                    if medicine_name == individual_medicine[0]:
                        print('medicine found successfully!')
                        print("Medicine Name:", individual_medicine[0])
                        print("Quantity:", individual_medicine[1])
                        print("Expiry Date:", individual_medicine[2])
                        print("Timings:", individual_medicine[3].split('/'))
                        print("Dosage Per Day:", individual_medicine[4])
                        medicine_found = True
                        break

    if not medicine_found:
        print('Medicine not found!')


def update_medicine(current_user):
    updated_profiles = []                    
    with open(file_name) as profiles:
        for profile in profiles:
            profile = profile.strip()
            user_info = profile.split("|")
            user_proflies = user_info[0].split(",")
            
            if current_user == user_proflies[0]:
                medicine_details = user_info[1].split(";")
                medicine_name = input("Enter medicine name: ")
                medicine_index = 0
                for medicine in medicine_details:
                    single_medicine_details = medicine.split(",")
                    if medicine_name == single_medicine_details[0]:
                        updated_records = single_medicine_details.copy()
                        while True:
                            print('1. Medicine Name')                        
                            print('2. Medicine quantity')
                            print('3. Medicine expiry date')
                            print('4. Medicine dosage and time slots')
                            print("5. Exit")
                            choice = int(input("Enter your choice: "))
                        
                            
                            if choice == 1:
                                updated_medicine_name = input("Enter medicine name: ")
                                updated_records[0] = updated_medicine_name
                                print("Medicine name updated successfully")
                            elif choice == 2:
                                updated_medicine_quantity = input("Enter medicine quantity: ")
                                updated_records[1] = updated_medicine_quantity
                                print("Medicine quantity updated successfully")
                            elif choice == 3:
                                updated_medicine_expiry_date = input("Enter medicine expiry date: ")
                                updated_records[2] = updated_medicine_expiry_date
                                print("Medicine expiry date updated successfully")
                            elif choice == 4:
                                updated_medicine_time = []
                                while True:
                                    print("Select Time Slots")
                                    print("1. 06:00 AM - 12:00 PM")
                                    print("2. 12:00 PM - 06:00 PM")
                                    print("3. 06:00 PM - 12:00 AM")
                                    print("4. 12:00 AM - 06:00 AM")
                                    print('5. Done')
                                    time_choice = int(input("Enter choice: "))
                                    if time_choice == 1:
                                        if "06:00 AM - 12:00 PM" not in updated_medicine_time:
                                            updated_medicine_time.append('06:00 AM - 12:00 PM')
                                            print("06:00 AM - 12:00 PM Time Slot Selected")
                                        else:
                                            print("Time slot already selected")
                                    elif time_choice == 2:
                                        if "12:00 PM - 06:00 PM" not in updated_medicine_time:
                                            updated_medicine_time.append("12:00 PM - 06:00 PM")
                                            print("12:00 PM - 06:00 PM Time Slot Selected")
                                        else:
                                            print("Time slot already selected")
                                    elif time_choice == 3:
                                        if "06:00 PM - 12:00 AM" not in updated_medicine_time:
                                            updated_medicine_time.append("06:00 PM - 12:00 AM")
                                            print("06:00 PM - 12:00 AM Time Slot Selected")
                                        else:
                                            print("Time slot already selected")
                                    elif time_choice == 4:
                                        if "12:00 AM - 06:00 AM" not in updated_medicine_time:
                                            updated_medicine_time.append("12:00 AM - 06:00 AM")
                                            print("12:00 AM - 06:00 AM Time Slot Selected")
                                        else:
                                            print("Time slot already selected")
                                    elif time_choice == 5:
                                        break
                                    else:
                                        print('Invalid choice! please try again')
                                    
                                updated_medicine_dosage_per_day = len(updated_medicine_time)
                                updated_medicine_time = "/".join(updated_medicine_time)
                                updated_records[3] = updated_medicine_time
                                updated_records[4] = str(updated_medicine_dosage_per_day)
                                

                                print("Medicine dosage and time slots updated successfully")
                            elif choice == 5:
                                break
                            else:
                                print("Invalid choice! please enter the choice again")

                        updated_medicine = ",".join(updated_records)
                        medicine_details[medicine_index] = updated_medicine
                    medicine_index += 1
                updated_profile = user_info[0] + '|' + ';'.join(medicine_details)
                updated_profiles.append(updated_profile)
            else:
                updated_profiles.append(profile)

    with open(file_name, "w") as profiles:
        for profile in updated_profiles:
            profiles.write(profile + "\n")