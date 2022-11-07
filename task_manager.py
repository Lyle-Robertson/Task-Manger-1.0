"""Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone"""

# =====importing libraries===========
from datetime import date

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
searchfile = open("user.txt", "r")
content = searchfile.readlines()
found = False

while not found:
    username = input("Enter your username:\t")
    password = input("Enter your password:\t")
    user_pass = username + ", " + password      # username, password combination

    for line in content:    # search for username,password combination
        if user_pass in line:   # if found
            found = True
            searchfile.close()
            break

    if not bool(found):     # if not found
        print("Username, Password or combination of two is incorrect. Try again\n")

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    # admin menu
    if username == "admin":
        menu = input('''\nSelect one of the following Options below:
r\t-\tRegistering a user
a\t-\tAdding a task
va\t-\tView all tasks
vm\t-\tview my task
s\t-\tStatistics
e\t-\tExit
: ''').lower()

    # non-admin menu
    else:
        menu = input('''\nSelect one of the following Options below:
r\t-\tRegistering a user
a\t-\tAdding a task
va\t-\tView all tasks
vm\t-\tview my task
e\t-\tExit
: ''').lower()

    if menu == 'r' and username == 'admin':
        pass
        new_user = input("Enter new username:\t")
        new_password = input("Enter password:\t")

        while new_user == new_user:
            confirm_password = input("Confirm password:\t")

            if confirm_password != new_password:    # password match conditional statement
                print("Password do not match. Try again\n")

            else:
                new_user_pass = "\n" + new_user + ", " + new_password
                ammendfile = open("user.txt", "a")      # adding user and password to file
                ammendfile.write(new_user_pass)
                ammendfile.close()

                print(new_user + " has been registered!\n")
                break

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        task_title = input("Task:\t\t\t\t\t\t")

        task_user = input("Assigned to:\t\t\t\t")

        date_assigned = date.today()
        date_assigned = date_assigned.strftime("%d/%m/%Y")
        print("Date Assigned:\t\t\t\t" + date_assigned)

        due_date = input("Due date (dd-mm-yyyy):\t\t")

        task_complete = "Task complete:\t\t\t\tNo"
        print(task_complete)

        task_description = input("Task description:\t\t\t")

        taskfile = open("tasks.txt", "a")   # writing data to task file
        taskfile.write(f'\nTask:\t\t\t\t\t\t{task_title},Assigned to:\t\t\t\t{task_user},'
                       f'Date Assigned:\t\t\t\t{date_assigned},'
                       f'Due date (dd/mm/yyyy):\t\t{due_date},{task_complete},'
                       f'Task description:\t\t\t{task_description}')
        taskfile.close()

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''

        task_file = open('tasks.txt', 'r')  # displays data in task file
        contents = task_file.readlines()
        for line in contents:
            print(*line.split(",")[0:6], sep="\n")

        task_file.close()

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''

        taskfile = open("tasks.txt", "r")  # displaying specific user tasks
        contents = taskfile.readlines()

        for line in contents:
            if username in line:
                print(*line.split(",")[0:6], sep="\n")

        taskfile.close()

    elif menu == 'r' and username != 'admin':   # allowing only admin to register new users
        print("Only admin is allowed to register new users, Please make another choice")

    elif menu == 's':   # accessible only by admin user
        users = open("user.txt", "r")

        num_users = len(users.readlines())  # determining number of users
        print(f"There are {num_users} users currently registered")
        users.close()

        tasks = open("tasks.txt", "r")  # determining number of tasks
        num_tasks = len(tasks.readlines()) - 1
        print(f"There are {num_tasks} tasks.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
