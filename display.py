# Medicine Reminder & Inventory Manager
# File: display.py
# Owner: Burhanuddin Lohawala

# Purpose:
# Display medicine information on the screen.

# Responsibilities:
# 1. Call login function
# 2. Create menu
# 3. Menu items 
# - View medicines
# - Add medicines
# - Remove or delete medicine
# - Log consumption 
# - Update medicine - later 
# - Exit menu
# - Exit program

import user_profiles
import medicines
import consumption
import alert
def display_menu(current_user):
    while True:
        print('===MENU===')
        print("1. View medicines")
        print("2. Add medicine")
        print("3. Delete medicine")
        print("4. Search medicine")
        print("5. Update medicine")
        print("6. consumption log")
        print("7. Exit menu")
        print("8. Exit")
        choice = int(input("Enter choice between 1 to 8: ").strip())
        if choice == 1:
            print('VIEW MEDICINE')
            medicines.view_medicine(current_user)
        elif choice == 2:
            print('ADD MEDICINE')
            user_medicine = medicines.add_medicine()
            medicines.save_medicine(current_user, user_medicine)
        elif choice == 3:
            print('DELETE MEDICINE')
            medicines.delete_medicine(current_user)
        elif choice == 4:
            print('SEARCH MEDICINE')
            medicines.search_medicine(current_user)
        elif choice == 5:
            print("UPDATE MEDICINE")
            medicines.update_medicine(current_user)
        elif choice == 6:
            print('MEDICINE CONSUMPTION DETAILS')
            consumption.log_consumption(current_user)
        elif choice == 7:
            print('LOGGING OUT....')
            return 'logout'
        elif choice == 8:
            return "exit"

def start():
    while True:
        current_user = user_profile.user_profile_menu()
        if current_user:
            alert.show_alerts(current_user)
            result = display_menu(current_user)
            if result == "logout":
                print("RETURNING TO THE LOGIN")
                continue
            if result == 'exit':    
                break
        else:
            print("GOODBYE")
            break



