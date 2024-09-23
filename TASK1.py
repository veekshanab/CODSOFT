# Simple To-Do List Application (Command-Line)

tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task (mark as completed)")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    title = input("Enter task title: ")
    task = {"title": title, "status": "pending"}
    tasks.append(task)
    print(f"Task '{title}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = task["status"]
            print(f"{i + 1}. {task['title']} [{status}]")

def update_task():
    view_tasks()
    task_num = int(input("Enter task number to update (mark as completed): ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["status"] = "completed"
        print(f"Task '{tasks[task_num]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['title']}' deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List app. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
