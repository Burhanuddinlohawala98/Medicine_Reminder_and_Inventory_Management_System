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
# - search meidicine

file_name = "accounts.txt"

def add_medicine():
    medicine_name = input("Enter medicine name: ")
    medicine_quantity = input("Enter medicine quantity: ")
    medicine_expiry_date = input("Enter the expiry date: ")
    number_of_times = int(input("How many times per day?: "))
    medicine_time = []
    for time in range(number_of_times):
        enter_time = input("Enter time: ")
        medicine_time.append(enter_time)
    return {
        "medicine_name": medicine_name,
        "medicine_quantity": medicine_quantity,
        "medicine_expiry_date": medicine_expiry_date,
        "medicine_dosage_per_day": number_of_times,
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
                    
