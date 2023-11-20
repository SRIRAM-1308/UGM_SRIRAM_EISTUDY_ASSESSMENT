import ast
class Device:
    def __init__(self, id, type, status, temperature=None):
        self.id = id
        self.type = type
        self.status = status
        self.temperature = temperature

class SmartHomeSystem:
    def __init__(self, devices):
        self.devices = {device['id']: Device(**device) for device in devices}
        self.scheduled_tasks = []
        self.automated_triggers = []

    def turn_on(self, id):
        self.devices[id].status = 'on'

    def set_schedule(self, id, time, command):
        self.scheduled_tasks.append({'device': id, 'time': time, 'command': command})

    def add_trigger(self, condition, action):
        self.automated_triggers.append({'condition': condition, 'action': action})

    def status_report(self):
        return "\n".join(f"{device.type.capitalize()} {device.id} is {device.status.capitalize()}."
                          for device in self.devices.values())

    def list_scheduled_tasks(self):
        return self.scheduled_tasks

    def list_automated_triggers(self):
        return self.automated_triggers

class Device:
    def __init__(self, id, type, status, temperature=None):
        self.id = id
        self.type = type
        self.status = status
        self.temperature = temperature

class SmartHomeSystem:
    def __init__(self, devices):
        self.devices = {device['id']: Device(**device) for device in devices}
        self.scheduled_tasks = []
        self.automated_triggers = []

    def turn_on(self, id):
        self.devices[id].status = 'on'

    def set_schedule(self, id, time, command):
        self.scheduled_tasks.append({'device': id, 'time': time, 'command': command})

    def add_trigger(self, condition, action):
        self.automated_triggers.append({'condition': condition, 'action': action})

    def status_report(self):
        return "\n".join(f"{device.type.capitalize()} {device.id} is {device.status.capitalize()}."
                          for device in self.devices.values())

    def list_scheduled_tasks(self):
        return self.scheduled_tasks

    def list_automated_triggers(self):
        return self.automated_triggers

def main():
    # Get user input
    devices_input = input("Enter devices (e.g., [{'id': 1, 'type': 'light', 'status': 'off'}, {'id': 2, 'type': 'thermostat', 'temperature': 70, 'status': 'off'}, {'id': 3, 'type': 'door', 'status': 'locked'}]): ")
    commands_input = input("Enter commands (e.g., ['turnOn(1)', 'setSchedule(2, \"06:00\", \"Turn On\")', 'addTrigger(\"temperature\", \">\", 75, \"turnOff(1)\")']): ")

    # Parse user input
    devices = ast.literal_eval(devices_input)
    commands = ast.literal_eval(commands_input)

    system = SmartHomeSystem(devices)

    for command in commands:
        if command.startswith('turnOn'):
            id = int(command.split('(')[1].split(')')[0])
            system.turn_on(id)
        elif command.startswith('setSchedule'):
            id, time, cmd = command.split('(')[1].split(')')[0].split(', ')
            id = int(id)
            system.set_schedule(id, time, cmd)
        elif command.startswith('addTrigger'):
            condition, action = command.split('(')[1].split(')')[0].split(', ')[0:2]
            system.add_trigger(condition, action)

    print("Status Report:", system.status_report())
    print("Scheduled Tasks:", system.list_scheduled_tasks())
    print("Automated Triggers:", system.list_automated_triggers())

if __name__ == "__main__":
    main()
