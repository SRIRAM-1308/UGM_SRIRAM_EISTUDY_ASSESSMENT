import time

class Rocket:
    def __init__(self):
        self.stage = "Pre-Launch"
        self.fuel = 100
        self.altitude = 0
        self.speed = 0

    def start_checks(self):
        return "All systems are 'Go' for launch."

    def launch(self):
        self.stage = "Stage 1"
        self.fuel -= 10
        self.altitude += 10
        self.speed += 1000
        return f"Stage: {self.stage}, Fuel: {self.fuel}%, Altitude: {self.altitude} km, Speed: {self.speed} km/h"

    def fast_forward(self, X):
        for _ in range(X):
            self.fuel -= 10
            self.altitude += 10
            self.speed += 1000
        return f"Stage: {self.stage}, Fuel: {self.fuel}%, Altitude: {self.altitude} km, Speed: {self.speed} km/h"

def main():
    rocket = Rocket()
    while True:
        command = input("Enter command (start_checks, launch, fast_forward X, exit): ")
        if command == "start_checks":
            print(rocket.start_checks())
        elif command == "launch":
            print(rocket.launch())
        elif command.startswith("fast_forward"):
            X = int(command.split()[1])
            print(rocket.fast_forward(X))
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
