# global task list
tasks = []

def main():
    print("Welcome to the todo app!")
    answer = getUserInput()
    if answer == 'y':
        addTask()
    else:
        print("You selected no")
        print(tasks)

def getUserInput():
    while True:
        prompt = input("Do you want to add a task (y/n)?")
        if prompt.lower() == 'y' or prompt.lower() == 'n':
            return prompt.lower()
        else:
            print("Invalid input, please enter 'y' or 'n'.")

def addTask():
    taskDescription = input("Enter the task description: ")
    tasks.append(taskDescription)
    print("Task added!")

if __name__ == "__main__":
    main()

