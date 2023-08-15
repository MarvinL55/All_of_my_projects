import datetime

# This is where the tasks are made
class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = "Pending"

    def mark_as_complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\n Due date: {self.due_date}\n Priority:{self.priority}\n Status{self.status}"

class TaskManager:
    def __init__(self, file_path):
        self.tasks = []
        self.file_path = file_path

    def create_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYY-MM-DD): ")
        priority = input("Enter task priority: ")
        task = Task(title, description, priority, due_date)
        self.tasks.append(task)
        print("Task created")

    def display_task(self):
        for task in self.tasks:
            print(task)

    def save_task_to_file(self):
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(str(task) + "\n")

    def load_task_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    task_data = line.strip().split("\n")
                    title = task_data[0].split(": ")[1]
                    description = task_data[1].split(": ")[1]
                    due_date = task_data[2].split(": ")[1]
                    priority = task_data[3].split(": ")[1]
                    status = task_data[4].split(": ")[1]
                    task = Task(title, description, due_date, priority)
                    task.status = status
                    self.task.append(task)
        except FileNotFoundError:
            print("No saved task found")

    def mark_task_As_completed(self):
        task_index = int(input("Enter the index of the task to mark as complete: "))
        if task_index >= 0 and task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.mark_as_complete()
            print("Task marked as completed!")
        else:
            print("Invalid task index")

def main():
    file_path = "tasks.txt"

    task_manager = TaskManager(file_path)
    task_manager.load_task_from_file()

    while True:
        print("\n--- Personal Task Manager ---")
        print("1. Create Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task_manager.create_task()
            task_manager.save_task_to_file()
        elif choice == "2":
            task_manager.mark_task_As_completed()
            task_manager.save_task_to_file()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()