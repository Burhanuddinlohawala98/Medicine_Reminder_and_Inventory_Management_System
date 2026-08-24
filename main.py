# Medicine Reminder & Inventory Manager

# Purpose:
# This is the main controller of the application.
# It connects all project modules and controls the program flow.

# Responsibilities:
# - Display the welcome screen.
# - Call function from display module.
# - Save data before exiting the program.

# Modules Used:
# - display.py


import display

if __name__ == "__main__":
    display.start()