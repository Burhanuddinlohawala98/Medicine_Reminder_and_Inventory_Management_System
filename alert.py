# Medicine Reminder & Inventory Manager
# File: alerts.py
# Owner: Bibin Rufaz L

# Purpose:
# Generate medicine alerts.

# Responsibilities:
# - check expiry status
# - Find low stock medicines.
# - Timely medicine reminder system

from datetime import datetime

file_name = 'accounts.txt'

def expiry_status(expiry_date):
    try:
        expiry_date_obj = datetime.strptime(expiry_date, "%d/%m/%Y").date()
        today = datetime.today().date()
        remaining_days = (expiry_date_obj - today).days

        if remaining_days == 0:
            return 'This medicine expires today'
        elif remaining_days < 0:
            return 'This medicine is already expired.'
        elif remaining_days <= 30:
            return 'This medicine will be expiring within 30 days'
        elif remaining_days <= 60:
            return 'This medicine will be expiring within 60 days'
        elif remaining_days <= 90:
            return 'This medicine will be expiring within 90 days'
        else:
            return 'This medicine is safe for consumption'
    except ValueError:
        return 'Invalid date format'

def parse_user_medicines(current_user):
    user_medicines = []
    
    try:
        with open(file_name, 'r') as profiles:
            lines = profiles.readlines()
            
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                i += 1
                
                # Skip empty lines
                if not line:
                    continue
                
                try:
                    user_profile = line.split("|")
                    if len(user_profile) < 2:
                        continue

                    user_info = user_profile[0].split(",")
                    username = user_info[0]

                    if current_user == username:
                        medicine_entries = user_profile[1].split(";")
                        
                        for medicine in medicine_entries:
                            fields = medicine.split(",")
                            
                            # Safety check to prevent IndexError
                            if len(fields) >= 4:
                                # Using a dictionary to store structured data
                                med_dict = {
                                    "name": fields[0],
                                    "quantity": int(fields[1]),
                                    "exp_date": fields[2],
                                    "timings": fields[3].split("/")
                                }
                                user_medicines.append(med_dict)
                except IndexError:
                    print("Skipping corrupted or incomplete line in file.")
                    
    except FileNotFoundError:
        print("Error: Accounts file not found.")
    
    return user_medicines

def check_user_expired_medicine(current_user):
    print("EXPIRY ALERT:")
    medicines = parse_user_medicines(current_user)
    
    if not medicines:
        print("Alert: No medicines found for this user.")
        return

    for med in medicines:
        status = expiry_status(med["exp_date"])
        print(f"{med['name']} | Expiry Date: {med['exp_date']} | Expiry Status: {status}")

def low_stock_medicine(current_user, threshold=5):
    print("LOW STOCK ALERT:")
    medicines = parse_user_medicines(current_user)
    
    if not medicines:
        print("Alert: No medicines found for this user.")
        return

    for med in medicines:
        if med["quantity"] <= threshold:
            print(f"ALERT! {med['name']} has low stock! Quantity left: {med['quantity']}")
        else:
            print(f"{med['name']} has enough stock! Quantity left: {med['quantity']}")

def get_current_time_slot():
    current_hour = datetime.now().hour
    
    # Using tuples for time range conditions
    time_slots = [
        ((6, 12), '06:00 AM - 12:00 PM'),
        ((12, 18), '12:00 PM - 06:00 PM'),
        ((18, 24), '06:00 PM - 12:00 AM'),
        ((0, 6), '12:00 AM - 06:00 AM')
    ]
    
    for time_range, slot_label in time_slots:
        start_hour = time_range[0]
        end_hour = time_range[1]
        if start_hour <= current_hour < end_hour:
            return slot_label
            
    return '12:00 AM - 06:00 AM'

def timely_medicine_reminder(current_user):
    print("TIMELY MEDICINE REMINDER:")
    current_slot = get_current_time_slot()
    print(f"Current time slot: {current_slot}")
    
    medicines = parse_user_medicines(current_user)
    
    if not medicines:
        print("Alert: No medicines found for this user.")
        return

    reminder_found = False
    for med in medicines:
        if current_slot in med["timings"]:
            print(f"It is time to take {med['name']}")
            reminder_found = True
            
    if not reminder_found:
        print("No medicine reminders for the current time slot.")

def show_alerts(current_user):
    # Retrieve user's medicines first
    medicines = parse_user_medicines(current_user)

    # If no medicines are found, stop execution immediately without printing anything
    if not medicines:
        return

    print(f"Alerts for User: {current_user}")
    print("----------------------------------------")
    timely_medicine_reminder(current_user)
    print("----------------------------------------")
    check_user_expired_medicine(current_user)
    print("----------------------------------------")
    low_stock_medicine(current_user)
    print("----------------------------------------")