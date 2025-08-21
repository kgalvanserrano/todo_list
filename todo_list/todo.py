def main():
    print("" \
    "Welcome to Kevin's Todo List App\n" \
    "What would you like to do today?\n" \
    "1. Add a task\n" \
    "2. View tasks\n" \
    "3. Clear tasks\n" \
    "4. Delete a task\n" \
    "5. Exit\n")
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            addTask()
        elif choice == '2':
            viewTasks()
        elif choice == '3':
            clearTasks()
        elif choice == '4':
            delTask()
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# adds a task
def addTask():
    f = open("todo_list/tasks.txt", "a")
    taskDescription = input("Enter the task description: ")
    f.write(taskDescription + '\n')
    print("Task added!")

# deletes a task
def delTask():
    f = open("todo_list/tasks.txt", "r")
    tasks = f.readlines() # read file into a list
    for i, task in enumerate(tasks, start=1): # show numbered tasks
        print(f"{i}. {task.strip()}")
    delete = int(input("Enter the number of the task to delete: "))
    try:
        if 1 <= delete <= len(tasks):
            tasks.pop(delete - 1) # we have to subtract by 1 since we're starting the enumeration with 1
            f = open("todo_list/tasks.txt", "w")
            f.writelines(tasks)
            f.close()
    except:
        print("Invalid task number.")

# view the tasks
def viewTasks():
    f = open("todo_list/tasks.txt", "r")
    f.seek(0)  # move to the beginning of the file
    for i, task in enumerate(f, start=1):
        print(f"{i}. {task.strip()}")  # read and print the list

# clear the tasks
def clearTasks():
    f = open("todo_list/tasks.txt", "w")


if __name__ == "__main__":
    main()
