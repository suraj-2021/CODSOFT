
import os

# Function to display the To-Do List
def display_todo_list():
    with open("todo.txt", "r") as f:
        tasks = f.read()
        if tasks:
            print("To-Do List:")
            print(tasks)
        else:
            print("Your to-do list is empty.")

# Function to add a task
def add_task(task):
    with open("todo.txt", "a") as f:
        f.write(task + "\n")
    print("Task added successfully.")

# Function to remove a task
def remove_task(task_index):
    with open("todo.txt", "r") as f:
        tasks = f.readlines()
    
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number.")
        return
    
    removed_task = tasks.pop(task_index - 1)
    
    with open("todo.txt", "w") as f:
        f.writelines(tasks)
    
    print(f"Task '{removed_task.strip()}' removed successfully.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_todo_list()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        display_todo_list()
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

