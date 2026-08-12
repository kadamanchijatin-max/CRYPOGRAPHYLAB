class Drone:
    def __init__(self, drone_id, model, owner, battery, location):
        self.drone_id = drone_id
        self.model = model
        self.owner = owner
        self.battery = battery
        self.location = location
        self.status = "LANDED"

        # Mission and telemetry data
        self.waypoints = []
        self.mission_status = "NO MISSION"
        self.altitude = 0
        self.speed = 0

    def get_status(self):
        print("\n===== DRONE STATUS =====")
        print(f"Drone ID       : {self.drone_id}")
        print(f"Model          : {self.model}")
        print(f"Owner          : {self.owner}")
        print(f"Battery        : {self.battery}%")
        print(f"Location       : {self.location}")
        print(f"Status         : {self.status}")
        print(f"Mission Status : {self.mission_status}")

    def take_off(self):
        if self.battery <= 10:
            print("Battery too low for takeoff.")
            return

        if self.status == "AIRBORNE":
            print("Drone is already airborne.")
            return

        self.status = "AIRBORNE"
        self.altitude = 10
        self.speed = 5

        print(f"Drone {self.drone_id} has taken off.")

    def land(self):
        if self.status == "LANDED":
            print("Drone is already landed.")
            return

        self.status = "LANDED"
        self.altitude = 0
        self.speed = 0

        print(f"Drone {self.drone_id} has landed.")

    def update_location(self, new_location):
        self.location = new_location
        print(f"Drone location updated to {new_location}.")

    def upload_waypoints(self, waypoints):
        self.waypoints = waypoints
        self.mission_status = "WAYPOINTS UPLOADED"

        print(
            f"{len(waypoints)} waypoint(s) uploaded "
            f"to drone {self.drone_id}."
        )

    def execute_mission(self):
        if not self.waypoints:
            print("No waypoints uploaded.")
            return

        if self.status != "AIRBORNE":
            print("Drone must be airborne to execute the mission.")
            return

        self.mission_status = "MISSION RUNNING"

        print("\n===== MISSION EXECUTION =====")

        for number, waypoint in enumerate(self.waypoints, start=1):
            print(
                f"Waypoint {number}: "
                f"Latitude={waypoint['latitude']}, "
                f"Longitude={waypoint['longitude']}"
            )

        self.mission_status = "MISSION COMPLETED"

        print("\nMission completed successfully.")

    def display_telemetry(self):
        print("\n===== DRONE TELEMETRY =====")
        print(f"Drone ID       : {self.drone_id}")
        print(f"Battery        : {self.battery}%")
        print(f"Location       : {self.location}")
        print(f"Status         : {self.status}")
        print(f"Altitude       : {self.altitude} m")
        print(f"Speed          : {self.speed} m/s")
        print(f"Mission Status : {self.mission_status}")
        print(f"Waypoints      : {len(self.waypoints)}")