from auth import login
from customer import add_customer
from room import show_available_rooms
from booking import create_booking
from invoice import checkout
from report import daily_income

role = login()
if not role:
    exit()

while True:
    print("""
    1. Add Customer
    2. View Rooms
    3. Create Booking
    4. Checkout
    5. Daily Income
    0. Exit
    """)

    choice = input("Choose: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        show_available_rooms()
    elif choice == "3":
        create_booking()
    elif choice == "4":
        checkout(int(input("Booking ID: ")))
    elif choice == "5":
        daily_income()
    elif choice == "0":
        break
