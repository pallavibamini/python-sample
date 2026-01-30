from func import show_drivers, book_ride, register_user, ride_history
while True:
    print("\n--- UBER MINI APP ---")
    print("1. Register User")
    print("2. Show Drivers")
    print("3. Book Ride")
    print("4. Ride History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()

    elif choice == "2":
        show_drivers()

    elif choice == "3":  
        book_ride()

    elif choice == "4":
        ride_history()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")
