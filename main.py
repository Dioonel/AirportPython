flights = {
    1: {
        "origin": "Buenos Aires",
        "destination": "Madrid",
        "date": "2026-12-15",
        "price": 850,
        "seats": 5
    },
    2: {
        "origin": "Buenos Aires",
        "destination": "New York",
        "date": "2026-12-20",
        "price": 950,
        "seats": 3
    },
    3: {
        "origin": "Cordoba",
        "destination": "Sao Paulo",
        "date": "2026-12-25",
        "price": 400,
        "seats": 8
    },
    4: {
        "origin": "Buenos Aires",
        "destination": "Tokyo",
        "date": "2027-01-10",
        "price": 1500,
        "seats": 2
    }
}

# Registered users
users = {}

# User reservations
reservations = {}

# Currently logged-in user
current_user = None


# Register a new user
def register_user():
    username = input("Enter a username: ")

    if username in users:
        print("Username already exists.")
        return

    password = input("Enter a password: ")

    users[username] = password
    reservations[username] = []

    print("User registered successfully!")


# Login an existing user
def login_user():
    global current_user

    if current_user is not None:
        print("You are already logged in.")
        return

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        current_user = username
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")


# Display available flights
def show_available_flights():
    print("\n--- AVAILABLE FLIGHTS ---")

    for flight_id, flight in flights.items():
        if flight["seats"] > 0:
            print(f"\nFlight ID: {flight_id}")
            print(f"Origin: {flight['origin']}")
            print(f"Destination: {flight['destination']}")
            print(f"Date: {flight['date']}")
            print(f"Price: ${flight['price']}")
            print(f"Available seats: {flight['seats']}")


# Reserve a flight
def reserve_flight():
    show_available_flights()

    try:
        flight_id = int(input("\nEnter the flight ID you want to reserve: "))

        if flight_id not in flights:
            print("Flight not found.")
            return

        flight = flights[flight_id]

        if flight["seats"] <= 0:
            print("No seats available for this flight.")
            return

        reservation = {
            "flight_id": flight_id,
            "origin": flight["origin"],
            "destination": flight["destination"],
            "date": flight["date"],
            "price": flight["price"]
        }

        reservations[current_user].append(reservation)
        flight["seats"] -= 1

        print("Flight reserved successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Display the user's reservations
def view_my_flights():
    user_reservations = reservations[current_user]

    print("\n--- MY FLIGHTS ---")

    if not user_reservations:
        print("You have no reservations.")
        return

    for index, reservation in enumerate(user_reservations, start=1):
        print(f"\nReservation #{index}")
        print(f"Flight ID: {reservation['flight_id']}")
        print(f"Origin: {reservation['origin']}")
        print(f"Destination: {reservation['destination']}")
        print(f"Date: {reservation['date']}")
        print(f"Price: ${reservation['price']}")


# Cancel a reservation
def cancel_flight():
    user_reservations = reservations[current_user]

    if not user_reservations:
        print("You have no reservations to cancel.")
        return

    view_my_flights()

    try:
        reservation_number = int(
            input("\nEnter the reservation number to cancel: ")
        )

        if reservation_number < 1 or reservation_number > len(user_reservations):
            print("Invalid reservation number.")
            return

        reservation = user_reservations.pop(reservation_number - 1)

        flight_id = reservation["flight_id"]

        # Restore the available seat
        flights[flight_id]["seats"] += 1

        print("Reservation cancelled successfully!")

    except ValueError:
        print("Please enter a valid number.")


def main():
    global current_user
    while True:
        print("\n========== FLIGHT RESERVATION SYSTEM ==========")

        print("1. REGISTER USER")
        print("2. LOGIN USER")
        print("3. RESERVE FLIGHT")
        print("4. VIEW MY FLIGHTS")
        print("5. CANCEL FLIGHT")
        print("6. LOGOUT")
        print("0. EXIT")

        if current_user is not None:
            print(f"\nLogged in as: {current_user}")
        else:
            print("\nStatus: Not logged in")

        option = input("\nSelect an option: ")

        if option == "1":
            register_user()

        elif option == "2":
            login_user()

        elif option == "0":
            print("Thank you for using our service!")
            break

        elif option == "6":

            if current_user is not None:
                print("Goodbye,", current_user)
                current_user = None
            else:
                print("You are not logged in.")

        elif option in ["3", "4", "5"]:

            if current_user is None:
                print("You must be logged in to perform this action.")
                continue

            if option == "3":
                reserve_flight()

            elif option == "4":
                view_my_flights()

            elif option == "5":
                cancel_flight()

        else:
            print("Invalid option. Please try again.")


main()
