
to_do_list = []
file_name = "tasks.txt"


def load_tasks():
    try:
        with open(file_name, "r") as file:
            for line in file:
                to_do_list.append(line.strip())
    except FileNotFoundError:
        # If the file doesn't exist, we create an empty list
        pass

# Function to save tasks to the file
def save_tasks():
    with open(file_name, "w") as file:
        for task in to_do_list:
            file.write(task + "\n")


def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")


def view_tasks():
    if not to_do_list:
        print("Your To-Do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")


def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        to_do_list.append(task)
        save_tasks()
        print(f"Task '{task}' added to the list.")
    else:
        print("Task cannot be empty.")


def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(to_do_list):
            removed_task = to_do_list.pop(task_number - 1)
            save_tasks()
            print(f"Task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    load_tasks()  
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting the To-Do List. Have a productive day!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

#start 
main()
