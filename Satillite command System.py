class Satellite:
    def __init__(self):
        self.orientation = "North"
        self.solar_panels = "Inactive"
        self.data_collected = 0

    def rotate(self, direction):
        self.orientation = direction

    def activate_panels(self):
        self.solar_panels = "Active"

    def deactivate_panels(self):
        self.solar_panels = "Inactive"

    def collect_data(self):
        if self.solar_panels == "Active":
            self.data_collected += 10

    def status_report(self):
        print(f"Orientation: {self.orientation}")
        print(f"Solar Panels: {self.solar_panels}")
        print(f"Data Collected: {self.data_collected}")

# Main function
def main():
    # Create a satellite object
    satellite = Satellite()
    # Display the initial state
    print("Initial State:")
    satellite.status_report()
    # Prompt the user for commands
    print("Enter commands to control the satellite. Type 'exit' to end the program.")
    while True:
        command = input("> ")
        if command == "exit":
            break
        elif command.startswith("rotate"):
            direction = command.split()[1]
            satellite.rotate(direction)
        elif command == "activatePanels":
            satellite.activate_panels()
        elif command == "deactivatePanels":
            satellite.deactivate_panels()
        elif command == "collectData":
            satellite.collect_data()
        else:
            print("Invalid command. Please try again.")
        # Display the updated state
        print("Updated State:")
        satellite.status_report()

# Run the main function
if __name__ == "__main__":
    main()
