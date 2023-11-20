class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} - {status}, Due: {self.due_date}"

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append(Task(description, due_date))

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()

    def view_tasks(self, filter="all"):
        if filter == "all":
            return "\n".join(str(task) for task in self.tasks)
        elif filter == "completed":
            return "\n".join(str(task) for task in self.tasks if task.completed)
        elif filter == "pending":
            return "\n".join(str(task) for task in self.tasks if not task.completed)

def main():
    manager = ToDoListManager()

    while True:
        command = input("Enter command (Add Task, Mark Completed, View Tasks): ")
        if command == "Add Task":
            task_input = input("Enter task description and due date (e.g., Buy groceries, 2023-09-20): ")
            description, due_date = task_input.split(', ')
            manager.add_task(description, due_date)
        elif command == "Mark Completed":
            description = input("Enter task description: ")
            manager.mark_completed(description)
        elif command == "View Tasks":
            filter = input("Enter filter (Show all, Show completed, Show pending): ")
            if filter == "Show all":
                print(manager.view_tasks("all"))
            elif filter == "Show completed":
                print(manager.view_tasks("completed"))
            elif filter == "Show pending":
                print(manager.view_tasks("pending"))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
