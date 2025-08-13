def main():
    print("Welcome to the todo app!")
    answer = getUserInput()
    if answer == 'y':
        print("You selected yes")
    else:
        print("You selected no")

def getUserInput():
    while True:
        prompt = input("Do you want to add a task (y/n)?")
        if prompt.lower() == 'y' or prompt.lower() == 'n':
            return prompt.lower()
        else:
            print("Invalid input, please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()

