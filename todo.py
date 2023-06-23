import os

import time


savePath = '/home/apoorva/Documents/GitHub/py-speedrun/'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


todos = []


with open (savePath+'/todo.txt') as data:
    tasks = data.readlines()
    
    for task in tasks:
        if(task.endswith("\n")):
           task= task.replace("\n","")    
        todos.append(task) 


def printTodos():
    os.system("clear");
    print(bcolors.OKGREEN+"Your Todos are:"+bcolors.ENDC)
    count =1
    for todo in todos:
        print(str(count)+"."+bcolors.OKCYAN + bcolors.UNDERLINE+todo+bcolors.ENDC)
        count+=1
    time.sleep(2)
    os.system("clear")

while True:
    operation = int(input("1.Add Task\n2.Remove Task\n3.Display Tasks\n4.Save and Exit\n"))
    if operation==1:
        os.system("clear")
       
        
        task = input("enter the task to be added:")
        todos.append(task);
        
        printTodos();
    elif operation==2:
        os.system("clear")
        printTodos()
        taskIndex = int(input("enter the number of the task to delete:\n"));
        if taskIndex<=len(todos):
            todos.remove(todos[taskIndex-1])
            printTodos()
        else:
            os.system("clear")
            print(bcolors.WARNING+"Entered task does not exist!"+bcolors.ENDC)
            time.sleep(2);
            os.system("clear")
    elif operation==3:
        os.system("clear")
        printTodos()
    else:
        with open(savePath+'/todo.txt','w') as data:
            for todo in todos:
                
                data.write(todo+'\n')
        
        exit();
        