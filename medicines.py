# Medicine Reminder & Inventory Manager
# File: medicine.py
# Owner: Hiralal Shah

# Purpose:
# Manage medicine records.

# Responsibilities:
# - Create medicine dictionaries.
# - Update medicine quantity.
# - Delete medicines.
# - Check expiry status.
# - Calculate days until expiry.

def add_medicine():
    medicine_name = input("Enter medicine name: ")
    medicine_quantity = input("Enter medicine quantity: ")
    medicine_expiry_date = input("Enter the expiry date: ")
    return {
        "medicine_name": medicine_name,
        "medicine_quantity": medicine_quantity,
        "medicine_expiry_date": medicine_expiry_date

    }