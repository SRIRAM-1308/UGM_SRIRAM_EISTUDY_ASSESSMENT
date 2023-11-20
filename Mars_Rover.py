class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No Obstacles detected."

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

class Terrain:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def is_valid_move(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        if (x, y) in self.obstacles:
            return False
        return True

class Simulation:
    def __init__(self, rover, terrain):
        self.rover = rover
        self.terrain = terrain

    def execute(self, commands):
        for command in commands:
            if command == 'F':
                next_x = self.rover.x
                next_y = self.rover.y
                if self.rover.direction == 'N':
                    next_y += 1
                elif self.rover.direction == 'S':
                    next_y -= 1
                elif self.rover.direction == 'E':
                    next_x += 1
                elif self.rover.direction == 'W':
                    next_x -= 1
                if self.terrain.is_valid_move(next_x, next_y):
                    self.rover.move_forward()
            elif command == 'L':
                self.rover.turn_left()
            elif command == 'R':
                self.rover.turn_right()

# Create a rover at position (0, 0) facing North
rover = Rover(0, 0, 'N')

# Create a terrain of size 10x10 with no obstacles
terrain = Terrain(10, 10, [])

# Create a simulation with the rover and the terrain
simulation = Simulation(rover, terrain)

# Execute a series of commands
simulation.execute('FFRFF')

def main():
    # Get user input
    grid_size = input("Enter grid size  ")
    starting_position = input("Enter starting position  ")
    commands = input("Enter commands  ")
    obstacles = input("Enter obstacles  ")

    # Parse user input
    width, height = map(int, grid_size.split('x'))
    x, y, direction = starting_position.split(',')
    x = int(x)
    y = int(y)
    commands = commands.split(',')
    obstacles = [tuple(map(int, obstacle.split(','))) for obstacle in obstacles.split(';')]

    # Create a rover at the starting position
    rover = Rover(x, y, direction)

    # Create a terrain of the specified size with the specified obstacles
    terrain = Terrain(width, height, obstacles)

    # Create a simulation with the rover and the terrain
    simulation = Simulation(rover, terrain)

    # Execute the commands
    simulation.execute(commands)

    print(f"Final Position: ({rover.x}, {rover.y}, {rover.direction})")
    print("Status Report:", rover.status_report())


if __name__ == "__main__":
    main()
