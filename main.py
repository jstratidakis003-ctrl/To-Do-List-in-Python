import json
import datetime


"""
Program description:
A Python To-Do List application that lets users create and manage multiple task lists stored in JSON files. Users can add, edit, remove, complete, schedule, and view tasks. 
Completed tasks are moved to a separate completed-task list, and the program also supports backups and creating/selecting different task files.
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

def save(tmpd,file ='tdl.json' ):
    """
        Saves the current task list to the JSON file.
        
        This keeps any changes made to the tasks, such as adding,
        removing, or clearing tasks, after the program closes.
    """
    with open(file, 'w') as tdl:
        json.dump(tmpd, tdl, indent=4)

def new_list(file):
    files = load('FileStor.json')
    save([],file)
    files.append(file)
    save(files, 'FileStor.json')

def select_file(fnumber):
    files = load('FileStor.json')
    if exit_check(fnumber):
        return
    fnumber = is_number(fnumber,files)
    if 0 <= fnumber < (len(files)):
        return files[fnumber]
    else:
        while 0 > fnumber or fnumber>= (len(files)):
            fnumber = is_number(input(f"Enter a valid number from[0-{len(files)-1}]: "),files)
        return files[fnumber]


def add_task(file = 'tdl.json'):

    """
        # Loads the existing tasks from the JSON file.
        # Asks the user to enter a new task.
        # Creates a dictionary containing the task's information,
        # including its description, start time, and completion status.
        # Adds the new task to the list and saves the updated list.
    """

    now = datetime.datetime.now()
    tdl = load(file)
    task = input("\nEnter task: ")
    if input("Do you wont to schedule a task (y/n): ") == 'y':
        scheduled = input("\nEnter The time you wave the task(YY-MM-DD): ")
        b = True
        while b == True:
            try:
                scheduled = datetime.datetime.strptime(scheduled, "%Y-%m-%d").date()
                print("Valid date:", scheduled)
                b = False
            except ValueError:
                print("\nThat's not a valid date.")
                scheduled = input("\nEnter The time you wave the task(dd/mm/yy): ")
    else:
        scheduled = 'None'
    tmpd = {
        "Scheduled task for" : f"{scheduled}",
        "Task": task,
        "Start time": f"{datetime.date.today()} {now.hour}:{now.minute} " ,
        "Done": False 
    }
    
    tdl.append(tmpd)
    save(tdl)

def edit(c):
    tdl =load()
    if exit_check(c):
        return
    tdl[c]["Task"] = input("\nEnter edited task: ")
    save(tdl)

def remove_task(i = -1,file = 'tdl.json'):
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

def done(d):
    """
        # Displays the saved tasks so the user can choose which task to complete.
        # Loads the task list and asks the user to enter a task number.
        # Marks the selected task as completed by changing "Done" to True.
        # Records the completion time and saves the updated task list.
        # Handles invalid input and allows the user to cancel with 'q'.
    """
    now = datetime.datetime.now()
    tdl = load()
    ctl = load('ctl_tdl.json')
    if exit_check(d):
        return
    tdl[d]["Done"] = True 
    tdl[d]["Finised time"] = f"{datetime.date.today()} {now.hour}:{now.minute} "
    save(tdl)
    print("\nCompleated Task: ")
    task = print_task(d)
    ctl.append(task)
    save(ctl,'ctl_tdl.json')
    remove_task(d)

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

def print_task(num,file= 'tdl.json'):
    tdl = load(file)
    print("\n", tdl[num])
    return tdl[num]

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

def back_up():
    tdl = load()
    save(tdl,'back_up.json')

def exit_check(n):
    if n == 'q':
        return True
    else:
        return False

def check_num(a=""):
    tdl = load()
    while True:
        try:
            t_num = input(f"\nEnter task number {a}or q to exit: ")
            num = int(t_num)
            if num >=0 and num < len(tdl):
                return num
            else:
                print(f"\nEnter a number in range of [0-{len(tdl) -1}] ") 
        except(ValueError):
            if t_num == 'q':
                print("\nAction canceld exiting")
                return t_num
            print(f"\nEnter a number in range of [0-{len(tdl) -1}]")

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
    print("Enter nf to create a new File list")
    print("Enter sf to sellect the file you wont to edit and use\n")

def is_number(n,lim):
    while True:
        try:
            n = int(n)
            return n
        except(ValueError):
            n = input(f"{n} is not a number please enter a number from[0-{len(lim)-1}]: ")
    

def ui():
    
    runing =True
    curent_file = 'tdl.json'
    while runing:
        print(f"Curent file is {curent_file}")
        ac = input("\nEnter q to exit h for help: ")
        print(ac)
        if ac == 'q':
            return True
        elif ac == '1':
            add_task(file = curent_file)
        elif ac == "p":
            print_tdl(curent_file)
        elif ac == 'c':
            clear_task()
            print("Task cleared")
        elif ac == "r":
            remove_task()
        elif ac == 'h':
            help_()
        elif ac == 'd':
            print_tdl()
            done(check_num("that has been compleated "))
        elif ac == 'pt':
            print_task(check_num())
        elif ac == 'e':
            print_tdl()
            edit(check_num)
        elif ac == "cp":
            print_tdl(file='ctl_tdl.json')
        elif ac == 'cc':
            clear_task(file='ctl_tdl.json')
            print("Task cleared")
        elif ac == "cr":
            remove_task(file='ctl_tdl.json')
        elif ac == 'cpt':
            print_task(check_num(),file='ctl_tdl.json')
        elif ac == 'b':
            print_tdl(file = 'back_up.json' )
        elif ac == 'bs':
            back_up()
            print("TDL Back up")
        elif ac == 'nf':
            newFileName = f"{input("Enter new file name: ")}.json"
            new_list(newFileName)
        elif ac == 'sf':
            files = load('FileStor.json')
            print(files)
            FileNumber = input(f"Enter a number from [0-{len(files) -1}]")
            curent_file = select_file(FileNumber)
            
            
            

        



def main_():
    tdl = load()
    ctl = load('ctl_tdl.json')
    files = load('FileStor.json')
    back_up()

    print("In the list there are two modes mode TDL(To Do List) and CTL(Commpleated Task List) Depending on the mode you can edit the relevant tasks press help for more ")
    
    print("Enter number 1 to add a task")

    print(datetime.datetime.date)
    
    while ui() != True:
        return 0



main_()
