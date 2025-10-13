# task_list.py

# Initialize an empty task list
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet. Add one!")
    else:
        print("📋 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"✅ Task added: {task}")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"❌ Task removed: {removed}")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Simple menu loop
while True:
    print("\n--- Task List Menu ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! Stay productive 🚀")
        break
    else:
        print("Invalid choice. Try again.")
