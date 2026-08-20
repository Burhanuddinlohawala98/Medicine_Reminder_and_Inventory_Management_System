# Medicine Reminder & Inventory Manager
# File: consumption.py
# Owner: Abdul Razzak Shaikh

# Purpose:
# Ask user anout dosage taken and tell him remaining dosag
# Update medicine quantity

# Responsibilities:
# - Log medicine consumption.


file_name = "accounts.txt"

def log_consumption(current_user):
    updated_records = []
    user_found = False
    with open(file_name, 'r') as profiles:

        for profile in profiles:
            profile = profile.strip()
            user_profile = profile.split("|")
            user_info = user_profile[0].split(",")
            if current_user == user_info[0]:
                user_found = True
                medicine_info = user_profile[1]
                medicines = medicine_info.split(';')

                consumed_medicine = []
                for medicine in medicines:
                    individual_medicine = medicine.split(',')

                    medicine_name = individual_medicine[0]
                    medicine_quantity = int(individual_medicine[1])
                    medicine_dosage = int(individual_medicine[-1])

                    dosage_taken = int(
                        input(f"Enter dosage taken for {medicine_name}: ")
                    )

                    if dosage_taken < 0:
                        print("Invalid dosage! Please enter a valid dosage.")

                    elif dosage_taken < medicine_dosage:
                        remaining_dosage = medicine_dosage - dosage_taken
                        new_medicine_quantity = medicine_quantity - dosage_taken
                        individual_medicine[1] = str(new_medicine_quantity)
                        print(
                            f"Remaining dosage for {medicine_name}: "
                            f"{remaining_dosage}"
                        )

                    elif dosage_taken == medicine_dosage:
                        new_medicine_quantity = medicine_quantity - dosage_taken
                        individual_medicine[1] = str(new_medicine_quantity)
                        print(f"All dosage for {medicine_name} is completed.")

                    else:
                        print("You cannot take more dosage than prescribed.")

                    consumed_medicine.append(",".join(individual_medicine))
                updated_medicine_info = ";".join(consumed_medicine)
                updated_user_profile = f"{user_profile[0]}|{updated_medicine_info}\n"
                updated_records.append(updated_user_profile)

            else:
                updated_records.append(profile + "\n")

                
    if not user_found:
        print("User not found.")
        return

    with open(file_name, 'w') as profiles:
        profiles.writelines(updated_records)
    print("Consumption logged successfully")