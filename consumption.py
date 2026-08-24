# Medicine Reminder & Inventory Manager
# File: consumption.py
# Owner: Abdul Razzak Shaikh

# Purpose:
# Ask user about dosage taken and tell him remaining dosage
# Update medicine quantity

# Responsibilities:
# - Log medicine consumption.

file_name = "accounts.txt"


def get_dosage(medicine_name, quantity, daily_dosage):
    while True:
        try:
            taken = int(input("Enter dosage taken for " + medicine_name + ": "))

            if taken < 0:
                print("Please enter a valid dosage.")
            elif taken > quantity:
                print("You do not have enough medicine quantity.")
            elif taken > daily_dosage:
                print("You cannot take more dosage than prescribed.")
            else:
                return taken

        except ValueError:
            print("Please enter a number.")


def log_consumption(current_user):
    updated_records = []
    user_found = False

    with open(file_name, "r") as profiles:

        for profile in profiles:
            profile = profile.strip()
            user_profile = profile.split("|")
            user_info = user_profile[0].split(",")

            if current_user != user_info[0]:
                updated_records.append(profile)
                continue

            user_found = True

            if len(user_profile) < 2 or user_profile[1].strip() == "":
                print("No medicines are currently available. Please add a medicine first.")
                updated_records.append(profile)
                return

            medicines = user_profile[1].split(";")
            valid_medicines = []

            # Check medicines
            for medicine in medicines:
                data = medicine.split(",")

                if len(data) < 5:
                    continue

                try:
                    quantity = int(data[1])
                    dosage = int(data[-1])

                    if quantity >= 0 and dosage > 0:
                        valid_medicines.append(medicine)
                    else:
                        print("Invalid medicine data for", data[0])

                except ValueError:
                    print("Invalid medicine data for", data[0])

            if len(valid_medicines) == 0:
                print("No valid medicines found.")
                updated_records.append(profile)
                continue

            # Show medicines
            print("\nAvailable medicines:")

            for i in range(len(valid_medicines)):
                name = valid_medicines[i].split(",")[0]
                print(i + 1, ".", name)

            # Select medicine
            while True:
                try:
                    choice = int(input("Enter medicine number: "))

                    if 1 <= choice <= len(valid_medicines):
                        break

                    print("Invalid medicine number.")

                except ValueError:
                    print("Please enter a number.")

            selected = valid_medicines[choice - 1].split(",")
            medicine_name = selected[0]
            quantity = int(selected[1])
            daily_dosage = int(selected[-1])

            print("\nMedicine:", medicine_name)
            print("Available quantity:", quantity)
            print("Dosage per day:", daily_dosage)

            # Enter dosage
            taken = get_dosage(medicine_name, quantity, daily_dosage)

            # Update quantity
            new_quantity = quantity - taken
            selected[1] = str(new_quantity)

            remaining_dosage = daily_dosage - taken

            print("\n--- Summary ---")
            print("Remaining dosage for today:", remaining_dosage)
            print("New total quantity:", new_quantity)

            # Replace medicine
            new_medicines = []

            for medicine in medicines:
                data = medicine.split(",")

                if len(data) >= 5 and data[0] == medicine_name:
                    new_medicines.append(",".join(selected))
                else:
                    new_medicines.append(medicine)

            new_profile = user_profile[0] + "|" + ";".join(new_medicines)
            updated_records.append(new_profile)

        if not user_found:
            print("User not found.")
            return

    with open(file_name, "w") as profiles:
        for record in updated_records:
            profiles.write(record + "\n")

        print("Consumption logged successfully")