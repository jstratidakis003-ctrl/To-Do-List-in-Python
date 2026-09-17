import json
import datetime

tdl = []
now = datetime.datetime.now()
"""

"""
def load():
    """ 
        Loads the file tdl and retuns the list as data with the tasks that have been saved 
    """ 

    with open('tdl.json', 'r') as tdl:
        try:
            data  = json.load(tdl)
        except(ValueError):
            print("File is empty load fail")

        return data

def help_():
    """ 
        Gives the user a list of the avalable choices 
    """ 

    print("Enter 1 to enter a task")
    print("Enter p to print all the tasks")
    print("Enter r to remove a task")
    print("Enter c to clear tasks")
    print("Enter q to exit")
    print("Enter d to compleat a task")



def save(tmpd):
    """
        Saves the current task list to the JSON file.
        
        This keeps any changes made to the tasks, such as adding,
        removing, or clearing tasks, after the program closes.
    """
    with open('tdl.json', 'w') as tdl:
        json.dump(tmpd, tdl, indent=4)

def add_task():
    """
        # Loads the existing tasks from the JSON file.
        # Asks the user to enter a new task.
        # Creates a dictionary containing the task's information,
        # including its description, start time, and completion status.
        # Adds the new task to the list and saves the updated list.
    """

    tdl = load()
    task = input("\nEnter task: ")
    
    tmpd = {
        "Task": task,
        "Start time": f"{datetime.date.today()} {now.hour}:{now.minute} " ,
        "Done": False 
    }
    
    tdl.append(tmpd)
    save(tdl)

def clear_task():
    """
     # Creates an empty list to replace the existing task list.
        # Saves the empty list to the JSON file, removing all saved tasks.
    """
    
    data = []
    save(data)

def print_tdl():
    """
        # Loads the saved tasks from the JSON file.
        # Loops through each task and displays it with a number.
        # The number helps the user identify a specific task
        # when removing or completing it.
    """
    a = 0
    for i in load():
        print(f"\nNumber: {a} {i}")
        a +=1


def remove_tasl():
    """ 
        Loads the saved task list.
        Displays all tasks with their corresponding numbers.
        Asks the user to enter the number of the task to remove.
        Converts the user's input into an integer to access the task.
        Removes the selected task and saves the updated list.
        If the input is invalid, displays an error message.
        Allows the user to enter 'q' to cancel the operation.
    """ 
    tdl = load()
    print_tdl()
    while True:
        try:
            i  = input("\nEnter task number you wont to deleate or q to cancel: ")
            print(f"\nDeleted task {tdl[int(i)]}")
            tdl.pop(int(i))
            save(tdl)
            break
        except(ValueError , IndexError):
            if i == 'q':
                print("\nCanceled ")
                break
            print(f"\nEnter a number from 0-{len(tdl)}")
    
def done():
    """
        # Displays the saved tasks so the user can choose which task to complete.
        # Loads the task list and asks the user to enter a task number.
        # Marks the selected task as completed by changing "Done" to True.
        # Records the completion time and saves the updated task list.
        # Handles invalid input and allows the user to cancel with 'q'.
    """
    print_tdl()
    tdl = load()
    while True:
        try: 
            num = input("\nEnter compleated task number: ")
            i = int(num)
            tdl[i]["Done"] = True 
            tdl[i]["Finised time time"] = f"{datetime.date.today()} {now.hour}:{now.minute} "
            save(tdl)
            break
        except(ValueError, IndexError):
            if num == 'q':
                print("\nCanceled ")
                break
            print(f"\nEnter a number from 0-{len(tdl)}")


def main_():
    
    
    print("Enter number 1 to add a task")


    runing =True
    while runing:
        ac = input("\nEnter q to exit h for help: ")
        if ac == 'q':
            return 0
        elif ac == '1':
            add_task()
        elif ac == "p":
            print_tdl()
        elif ac == 'c':
            clear_task()
            print("Task cleared")
        elif ac == "r":
            remove_tasl()
        elif ac == 'h':
            help_()
        elif ac == 'd':
            done()


main_()
