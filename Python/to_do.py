class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list!")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print(f"- {task}")
        else:
            print("No tasks found!")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter task description: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
