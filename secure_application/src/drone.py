class Drone:
    def __init__(self, drone_id, model, owner, battery, location):
        self.drone_id = drone_id
        self.model = model
        self.owner = owner
        self.battery = battery
        self.location = location
        self.status = "LANDED"

    def get_status(self):
        print("\n===== DRONE STATUS =====")
        print(f"Drone ID : {self.drone_id}")
        print(f"Model    : {self.model}")
        print(f"Owner    : {self.owner}")
        print(f"Battery  : {self.battery}%")
        print(f"Location : {self.location}")
        print(f"Status   : {self.status}")

    def take_off(self):
        if self.battery <= 10:
            print("Battery too low for takeoff.")
            return

        if self.status == "AIRBORNE":
            print("Drone is already airborne.")
            return

        self.status = "AIRBORNE"
        print(f"Drone {self.drone_id} has taken off.")

    def land(self):
        if self.status == "LANDED":
            print("Drone is already landed.")
            return

        self.status = "LANDED"
        print(f"Drone {self.drone_id} has landed.")

    def update_location(self, new_location):
        self.location = new_location
        print(f"Drone location updated to {new_location}.")