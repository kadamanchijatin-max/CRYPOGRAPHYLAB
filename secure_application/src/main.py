from drone import Drone
from authentication import login


drones = {}


def register_drone():
    print("\n===== REGISTER DRONE =====")

    drone_id = input("Enter Drone ID: ").strip()
    model = input("Enter Drone Model: ").strip()
    owner = input("Enter Owner Name: ").strip()

    try:
        battery = int(input("Enter Battery Percentage: "))
    except ValueError:
        print("Battery must be a number.")
        return

    location = input("Enter Current Location: ").strip()

    if drone_id in drones:
        print("Drone ID already exists.")
        return

    if battery < 0 or battery > 100:
        print("Battery must be between 0 and 100.")
        return

    drone = Drone(
        drone_id,
        model,
        owner,
        battery,
        location
    )

    drones[drone_id] = drone

    print("\nDrone registered successfully!")


def view_drones():
    print("\n===== REGISTERED DRONES =====")

    if not drones:
        print("No drones registered.")
        return

    for drone in drones.values():
        print(
            f"\nID: {drone.drone_id}"
            f"\nModel: {drone.model}"
            f"\nOwner: {drone.owner}"
            f"\nBattery: {drone.battery}%"
            f"\nLocation: {drone.location}"
            f"\nStatus: {drone.status}"
        )


def find_drone():
    drone_id = input("Enter Drone ID: ").strip()

    if drone_id not in drones:
        print("Drone not found.")
        return None

    return drones[drone_id]


def check_status():
    drone = find_drone()

    if drone:
        drone.get_status()


def take_off_drone():
    drone = find_drone()

    if drone:
        drone.take_off()


def land_drone():
    drone = find_drone()

    if drone:
        drone.land()


def update_location():
    drone = find_drone()

    if drone:
        new_location = input("Enter new location: ").strip()
        drone.update_location(new_location)


def execute_command():
    print("\n===== DRONE COMMAND =====")

    drone = find_drone()

    if not drone:
        return

    command = input(
        "Enter command (takeoff/land/status): "
    ).strip()

    # INTENTIONALLY VULNERABLE:
    # User-controlled input is passed to eval().
    # This vulnerability will be analyzed and fixed in Assignment 4.
    try:
        eval(command)
    except Exception as error:
        print(f"Command execution failed: {error}")


def main_menu():
    while True:
        print("\n")
        print("=" * 40)
        print("     DRONE MANAGEMENT SYSTEM")
        print("=" * 40)

        print("1. Register Drone")
        print("2. View All Drones")
        print("3. Check Drone Status")
        print("4. Update Drone Location")
        print("5. Take Off")
        print("6. Land")
        print("7. Execute Drone Command")
        print("8. Logout")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            register_drone()

        elif choice == "2":
            view_drones()

        elif choice == "3":
            check_status()

        elif choice == "4":
            update_location()

        elif choice == "5":
            take_off_drone()

        elif choice == "6":
            land_drone()

        elif choice == "7":
            execute_command()

        elif choice == "8":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


def main():
    if login():
        main_menu()


if __name__ == "__main__":
    main()