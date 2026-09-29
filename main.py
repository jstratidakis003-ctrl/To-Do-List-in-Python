import json
import datetime

tdl = []
ctl = []
now = datetime.datetime.now()
"""

"""
def load(file ='tdl.json'):
    """ 
        Loads the file tdl and retuns the list as data with the tasks that have been saved 
    """ 

    with open(file, 'r') as tdl:
        try:
            data  = json.load(tdl)
        except(ValueError):
            print("File is empty load fail")

        return data

def help_():
    """ 
        Gives the user a list of the avalable choices 
    """ 
    print("Press c and the relevant function for the compleated tasks ")
    
    print("\nEnter 1 to enter a task")
    print("Enter p to print all the tasks or cp for the compleated task list")
    print("Enter r to remove a task or cr for the compleated task list")
    print("Enter c  to clear tasks or cc for the compleated task list")
    print("Enter q to exit")
    print("Enter d to compleat a task")
    print("Enter pt to print a single task or cpt for the compleated task list")
    print("Enter e to edit a task")
    print("Enter b to print back up")
    print("Enter bs to save new back up")
    print("Back up happens evry time you enter the program")
    



def save(tmpd,file ='tdl.json' ):
    """
        Saves the current task list to the JSON file.
        
        This keeps any changes made to the tasks, such as adding,
        removing, or clearing tasks, after the program closes.
    """
    with open(file, 'w') as tdl:
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

def clear_task(file = 'tdl.json'):
    """
     # Creates an empty list to replace the existing task list.
        # Saves the empty list to the JSON file, removing all saved tasks.
    """
    
    data = []
    save(data,file)

def print_tdl(file = 'tdl.json'):
    """
        # Loads the saved tasks from the JSON file.
        # Loops through each task and displays it with a number.
        # The number helps the user identify a specific task
        # when removing or completing it.
    """
    if file == 'tdl.json':
        print("To DO List: ")
    elif file == 'ctl_tdl.json':
        print("Compleated Tasks ")
    elif file == 'back_up.json':
        print('Back Up To Do List')
    a = 0
    for i in load(file):
        print(f"\nNumber: {a}: ")
        for c in i.items():
            print(f" {c}")
        a +=1



def remove_tasl(i = -1,file = 'tdl.json'):
    """ 
        Loads the saved task list.
        Displays all tasks with their corresponding numbers.
        Asks the user to enter the number of the task to remove.
        Converts the user's input into an integer to access the task.
        Removes the selected task and saves the updated list.
        If the input is invalid, displays an error message.
        Allows the user to enter 'q' to cancel the operation.
    """ 
    tdl = load(file)
    
    if i == -1:
        print_tdl(file)
        i  = check_num("you wont to deleate ")
        if exit_check(i):
            return
        print(f"\nDeleted task {tdl[int(i)]}")
    tdl.pop(int(i))
    save(tdl,file)

def exit_check(n):
    if n == 'q':
        return True
    else:
        return False




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
    ctl = load('ctl_tdl.json')
    d = check_num("that has been compleated ")
    if exit_check(d):
        return
    tdl[d]["Done"] = True 
    tdl[d]["Finised time time"] = f"{datetime.date.today()} {now.hour}:{now.minute} "
    save(tdl)
    print("\nCompleated Task: ")
    ctl.append(print_task(d))
    save(ctl,'ctl_tdl.json')
    remove_tasl(d)
    
    
def back_up():
    tdl = load()
    save(tdl,'back_up.json')

def print_task(num,file= 'tdl.json'):
    tdl = load(file)
    print("\n", tdl[num])
    return tdl[num]


def edit():
    print_tdl()
    tdl =load()
    
    c = check_num()
    if exit_check(c):
        return
    tdl[c]["Task"] = input("\nEnter edited task: ")
    save(tdl)
        
def check_num(a=""):
    tdl = load()
    while True:
        try:
            t_num = input(f"\nEnter task number {a}or q to exit: ")
            num = int(t_num)
            if num >=0 and num <= len(tdl):
                return num
            else:
                print(f"\nEnter a number in range of [0-{len(tdl)}] ") 
        except(ValueError):
            if t_num == 'q':
                print("\nAction canceld exiting")
                return t_num
            print(f"\nEnter a number in range of [0-{len(tdl)}]")


def main_():

    tdl = load()
    ctl = load('ctl_tdl.json')
    back_up()

    print("In the list there are two modes mode TDL(To Do List) and CTL(Commpleated Task List) Depending on the mode you can edit the relevant tasks press help for more ")
    
    print("Enter number 1 to add a task")


    runing =True
    while runing:
        
        ac = input("\nEnter q to exit h for help: ")
        print(ac)
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
        elif ac == 'pt':
            print_task(check_num())
        elif ac == 'e':
            edit()
        elif ac == "cp":
            print_tdl(file='ctl_tdl.json')
        elif ac == 'cc':
            clear_task(file='ctl_tdl.json')
            print("Task cleared")
        elif ac == "cr":
            remove_tasl(file='ctl_tdl.json')
        elif ac == 'cpt':
            print_task(check_num(),file='ctl_tdl.json')
        elif ac == 'b':
            print_tdl(file = 'back_up.json' )
        elif ac == 'bs':
            back_up()
            print("TDL Back up")


main_()
