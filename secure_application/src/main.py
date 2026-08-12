from drone import Drone
from authentication import login
from pathlib import Path


drones = {}

LOG_FILE = Path(__file__).resolve().parent.parent / "outputs" / "drone_logs.txt"


def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")


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

    write_log(f"Drone registered: {drone_id}")

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
            f"\nMission: {drone.mission_status}"
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
        write_log(f"Drone {drone.drone_id}: takeoff")


def land_drone():
    drone = find_drone()

    if drone:
        drone.land()
        write_log(f"Drone {drone.drone_id}: landing")


def update_location():
    drone = find_drone()

    if drone:
        new_location = input("Enter new location: ").strip()

        drone.update_location(new_location)

        write_log(
            f"Drone {drone.drone_id}: "
            f"location updated to {new_location}"
        )


def upload_waypoints():
    drone = find_drone()

    if not drone:
        return

    print("\n===== WAYPOINT UPLOAD =====")

    try:
        count = int(input("How many waypoints? "))
    except ValueError:
        print("Number of waypoints must be an integer.")
        return

    if count <= 0:
        print("At least one waypoint is required.")
        return

    waypoints = []

    for number in range(1, count + 1):
        print(f"\nWaypoint {number}")

        try:
            latitude = float(input("Latitude: "))
            longitude = float(input("Longitude: "))
        except ValueError:
            print("Latitude and longitude must be numbers.")
            return

        waypoints.append(
            {
                "latitude": latitude,
                "longitude": longitude
            }
        )

    drone.upload_waypoints(waypoints)

    write_log(
        f"Drone {drone.drone_id}: "
        f"{count} waypoint(s) uploaded"
    )


def execute_mission():
    drone = find_drone()

    if not drone:
        return

    drone.execute_mission()

    write_log(
        f"Drone {drone.drone_id}: "
        f"mission execution requested"
    )


def display_telemetry():
    drone = find_drone()

    if drone:
        drone.display_telemetry()

        write_log(
            f"Drone {drone.drone_id}: "
            f"telemetry displayed"
        )


def execute_command():
    print("\n===== DRONE COMMAND =====")

    drone = find_drone()

    if not drone:
        return

    command = input(
        "Enter command (takeoff/land/status): "
    ).strip().lower()

    # INTENTIONALLY VULNERABLE FOR ASSIGNMENT 3:
    # User-controlled input is passed to eval().
    #
    # The local command names are mapped to functions so that
    # normal commands such as "status", "takeoff", and "land"
    # work during the demonstration.
    command_functions = {
        "status": drone.get_status,
        "takeoff": drone.take_off,
        "land": drone.land,
        "telemetry": drone.display_telemetry
    }

    try:
        eval(
            "command_functions[command]()",
            {
                "command_functions": command_functions,
                "command": command
            }
        )

        write_log(
            f"Drone {drone.drone_id}: "
            f"command executed - {command}"
        )

    except Exception as error:
        print(f"Command execution failed: {error}")


def main_menu():
    while True:
        print("\n")
        print("=" * 45)
        print("       DRONE MISSION CONTROL SYSTEM")
        print("=" * 45)

        print("1. Register Drone")
        print("2. View All Drones")
        print("3. Check Drone Status")
        print("4. Update Drone Location")
        print("5. Take Off")
        print("6. Land")
        print("7. Execute Drone Command")
        print("8. Upload Waypoints")
        print("9. Execute Mission")
        print("10. Display Telemetry")
        print("11. View Log File")
        print("12. Logout")

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
            upload_waypoints()

        elif choice == "9":
            execute_mission()

        elif choice == "10":
            display_telemetry()

        elif choice == "11":
            view_log_file()

        elif choice == "12":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


def view_log_file():
    print("\n===== DRONE LOGS =====")

    if not LOG_FILE.exists():
        print("No logs available.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        logs = file.read()

    if logs:
        print(logs)
    else:
        print("No logs available.")


def main():
    if login():
        main_menu()


if __name__ == "__main__":
    main()