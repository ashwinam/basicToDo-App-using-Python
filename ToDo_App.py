def workInProgress(): # Put from new entries to In progress table
    push_entries = int(input('Enter the number to transfer into In progress: '))
    print()
    value = toDo.pop(push_entries)
    inProgress.append(value)

def completedTasks(): # Put from In progress table to Completed Table
    push_entries = int(input('Enter the number to transfer into Completed Task: '))
    print()
    value = inProgress.pop(push_entries)
    completedTask.append(value)
    

def newlyAddedViews(): # Table Of new ToDo's
    for key, values in toDo.items():
        print(f'{key}'.rjust(48),f' | {values}')

def inProgressView(): # Table of In progress ToDo's
    for value in range(len(inProgress)):
        print(f'{value}'.rjust(48),f' | {inProgress[value]}')

def completedTaskView(): # Table of Complete Task ToDo's ToDo's
    for value in range(len(completedTask)):
        print(f'{value}'.rjust(48),f' | {completedTask[value]}')

def bare_template(viewName): # Boiler plate for Heading's
    print(viewName.center(100))
    print('**************'.center(100))
    print('Sr.No | ToDo'.center(100))
    print('--------------'.center(100))


def toDoView(): # ToDo View(show's all Table and interaction between tables)
    while (True):
        try:
            # # Table Of new ToDo's
            bare_template(viewName='To Do List')
            newlyAddedViews()
            print()
            # Table of In progress ToDo's
            bare_template(viewName='In Progress')
            if inProgress:
                inProgressView()
            else:
                print('No data...'.center(100))
            print()
            # Table of Complete Task ToDo's ToDo's
            bare_template(viewName='Completed Task')
            if completedTask:
                completedTaskView()
            else:
                print('No data...'.center(100))
            print()
            # Options for Transfer Data from one table to another
            print('Choose below options 1 to 3'.center(60))
            print('1.Put task in Progress, 2.Put task In Completed, 3.quit the option')
            userChoice = int(input('Enter the Task: '))
            if userChoice == 1:
                print('In Progress'.center(60))
                workInProgress()
            if userChoice == 2:
                print("Complete Task List".center(60))
                if len(inProgress) != 0:
                    completedTasks()
                else:
                    print('Theres No Entry In In progress...')
            if userChoice == 3:
                print('Exit...')
                break
        except:
            print('Give the proper input')

def show(): # call the ToDo view function
    if len(toDo) != 0:
        toDoView()
    else:
        print('theres No To Do In DataBase, Press 1 for make one.')

def add(): # Adding the new Entry in ToDo's
    user_input = input('Enter the Task: ')
    for keyName in range(1,10):
        if keyName not in toDo.keys():
            toDo[keyName] = user_input
            return toDo


def update(): #make changes in New ToDo's
    bare_template('To Do List')
    newlyAddedViews()
    print('Use the key number for Update')
    keyUpdate = int(input("Enter the Number from above todo's that you want to update: "))
    if keyUpdate in toDo.keys():
        toDo[keyUpdate] = input('Enter the Task: ')
        print(f'{keyUpdate} has been updated.')
    else:
        print('Its Not Available in Todos , use the sr.no from above')

def delete(): # delete from ToDo's
    bare_template('To Do List')
    newlyAddedViews()
    print('Use the Number from Sr.No for Delete')
    deleteKeyNum = int(input("Enter the Number from above todo's that you want to delete: "))
    if deleteKeyNum in toDo.keys():
        del toDo[deleteKeyNum]
        print('selected Task Deleted from Database')
    else:
        print('Use the number from sr.no')

if __name__=="__main__": # main project Execution Start from Here
    toDo = {}
    inProgress = []
    completedTask = []
    print('''
    Welcome to the Apna Kam Manage KarneWala!
        Choose Your Option from 1 to 5...

            1. Add the To Do
            2. Show the To Do
            3. Edit The To Do
            4. Delete The To Do
            5. Exit the App
    ''')
    while (1):
        print()
        try:
            user_choice = int(input('Enter Your Choice: '))
            print()
            if user_choice == 1:
                add()
            if user_choice == 2:
                show()
            if user_choice == 3:
                update()
            if user_choice == 4:
                delete()
            if user_choice == 5:
                print('Exit...')
                break
        except:
            print('Give the correct Choice, Between 1 to 5.')
        
        print()
        print('Choose from 1 to 5.'.center(100))
        print('1. Add the To Do, 2. Show the To Do, 3. Edit The To Do, 4. Delete The To Do, 5. Exit the App')