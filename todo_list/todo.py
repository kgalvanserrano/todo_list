# read lines -> put them in a list
# show numbered tasks -> ask the user which number to delete
# use list deletion (pop/del)
# rewrite the file with the updated list

# open the stupid tasks file
f = open("todo_list/tasks.txt", "r+")

# main
# run app
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
            f.close()
            break
        else:
            print("Invalid choice, please try again.")

# adds a task
def addTask():
    taskDescription = input("Enter the task description: ")
    f.write(taskDescription + '\n')
    print("Task added!")
    
# deletes a task
def delTask():
    tasks = f.readlines()
    f.seek(0)

# view the tasks
def viewTasks():
    f.seek(0)  # move to the beginning of the file
    print(f.read())  # read and print the list

# clear the tasks
def clearTasks():
    f.seek(0)  # move to the beginning of the file
    f.truncate(0)


if __name__ == "__main__":
    main()