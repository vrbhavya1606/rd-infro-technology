class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - [{status}]")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
        else:
            print("Invalid task number.")

    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
        else:
            print("Invalid task number.")

    def show_menu(self):
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
                print("Task added successfully.")
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_tasks()
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                self.update_task(task_number, new_task)
                print("Task updated successfully.")
            elif choice == "4":
                self.view_tasks()
                task_number = int(input("Enter the task number to delete: "))
                self.delete_task(task_number)
                print("Task deleted successfully.")
            elif choice == "5":
                self.view_tasks()
                task_number = int(input("Enter the task number to mark as completed: "))
                self.mark_completed(task_number)
                print("Task marked as completed.")
            elif choice == "6":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if _name_ == "_main_":
    to_do_list = ToDoList()
    to_do_list.run()
