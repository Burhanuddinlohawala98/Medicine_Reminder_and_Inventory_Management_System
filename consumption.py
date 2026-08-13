# Medicine Reminder & Inventory Manager
# File: consumption.py
# Owner: Abdul Razzak Shaikh

# Purpose:
# Manage medicine consumption history.

# Responsibilities:
# - Log medicine consumption.
# - View consumption history.
# - Retrieve recent consumption entries.
# - Calculate remaining daily doses.

file_name = "accounts.txt"


def log_consumption(current_user):
    with open(file_name, 'r') as profiles:

        for profile in profiles:
            profile = profile.strip()
            user_profile = profile.split("|")
            user_info = user_profile[0].split(",")
            if current_user == user_profile[0]:

                medicine_info = user_profile[1]
                medicines = medicine_info.split(';')

                for medicine in medicines:
                    individual_medicine = medicine.split(',')

                    medicine_name = individual_medicine[0]
                    medicine_dosage = int(individual_medicine[-1])

                    dosage_taken = int(
                        input(f"Enter dosage taken for {medicine_name}: ")
                    )

                    if dosage_taken < 0:
                        print("Invalid dosage! Please enter a valid dosage.")

                    elif dosage_taken < medicine_dosage:
                        remaining_dosage = medicine_dosage - dosage_taken
                        print(
                            f"Remaining dosage for {medicine_name}: "
                            f"{remaining_dosage}"
                        )

                    elif dosage_taken == medicine_dosage:
                        print(f"All dosage for {medicine_name} is completed.")

                    else:
                        print("You cannot take more dosage than prescribed.")

                return

        print("User not found.")