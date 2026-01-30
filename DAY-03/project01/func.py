# ------------------ DATA ------------------

users = []

drivers = {
    1: {"name": "sls", "loc": 5},
    2: {"name": "xyz", "loc": 12},
    3: {"name": "qwert", "loc": 20},
    4: {"name": "aswd", "loc": 2}
}

available_drivers = {1, 2, 3, 4}
rides = []

RATE_PER_KM = 10

def register_user():
    name = input("Enter user name: ")
    users.append(name)
    print("User registered successfully!")

def show_drivers():
    print("\nAvailable Drivers:")
    for d in available_drivers:
        print(f"ID:{d} Name:{drivers[d]['name']} Location:{drivers[d]['loc']} km")

def get_user_location():
    return int(input("Enter your current location (km): "))


def get_destination():
    return int(input("Enter destination location (km): "))



def calculate_distance(loc1, loc2):
    return abs(loc2 - loc1)


def calculate_fare(distance):
    return distance * RATE_PER_KM

def book_ride():
    user = input("Enter your name: ")

    if user not in users:
        print("User not registered!")
        return

    if not available_drivers:
        print("No drivers available!")
        return

    show_drivers()
    driver_id = int(input("Enter driver ID: "))

    if driver_id not in available_drivers:
        print("Driver not available!")
        return

    user_loc = get_user_location()
    dest_loc = get_destination()
    driver_loc = drivers[driver_id]["loc"]

    pickup_distance = calculate_distance(driver_loc, user_loc)
    trip_distance = calculate_distance(user_loc, dest_loc)
    fare = calculate_fare(trip_distance)

    ride = {
        "user": user,
        "driver": drivers[driver_id]["name"],
        "trip_distance": trip_distance,
        "fare": fare
    }

    rides.append(ride)
    available_drivers.remove(driver_id)

    print("\nRide Booked Successfully!")
    print(f"Driver: {drivers[driver_id]['name']}")
    print(f"Trip Distance: {trip_distance} km")
    print(f"Fare: ₹{fare}")

# ------------------

def ride_history():
    print("\nRide History:")
    for r in rides:
        print(f"{r['user']} -> {r['driver']} | {r['trip_distance']} km | ₹{r['fare']}")

# ------------------