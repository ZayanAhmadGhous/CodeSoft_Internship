tasks = [] 

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def update_task(task_index, new_task):
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index")
    else:
        tasks[task_index] = new_task
        print("Task updated successfully!")

def delete_task(task_index):
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index")
    else:
        deleted_task = tasks.pop(task_index)
        print("Task deleted successfully:", deleted_task)

def display_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# Main program loop
while True:
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Display Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task_index = int(input("Enter task index: ")) - 1
        new_task = input("Enter new task: ")
        update_task(task_index, new_task)
    elif choice == "3":
        task_index = int(input("Enter task index: ")) - 1
        delete_task(task_index)
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")