#Define a global list to hold tasks
tasks = []

def add_task(task_name):
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Task '{task_name}' added.")

def remove_task(task_name):
    global tasks
    tasks = [task for task in tasks if task['name'] != task_name]
    print(f"Task '{task_name}' removed.")

def list_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    for i, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"{i + 1}. {task['name']} - {status}")

def mark_task_completed(task_name):
    for task in tasks:
        if task['name'] == task_name:
            task['completed'] = True
            print(f"Task '{task_name}' marked as completed.")
            return
    print(f"Task '{task_name}' not found.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Mark Task Completed")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == '2':
            task_name = input("Enter task name to remove: ")
            remove_task(task_name)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            task_name = input("Enter task name to mark as completed: ")
            mark_task_completed(task_name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
