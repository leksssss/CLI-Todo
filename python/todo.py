import argparse
import sys
import datetime
from termcolor import colored


#added colorcodes to console output for better visuals

def add(args):
    maxval = -1
    #copying existing lines/ creating new file if not exists
    try:
        fout = open('todo.txt','r')    
    except:
        fout = open('todo.txt','a+')
        
    fline = fout.readlines()
    if fline is not None:
        for line in fline:
            l = line.split()[0]
            length = len(l)
            num = int(l[1:length-1])
            #print(num)
            maxval = max(num, maxval)
    fout.close()
    if maxval >= 0:
        x = maxval + 1
    else:
        x = 1
    #inserting the newly added todo on top
    with open("todo.txt", "w") as fout:
        fout.write(f"[{x}] {args.additem}\n")
        fout.writelines(fline)
    
    sys.stdout.write(colored(f"Added todo: \"{args.additem}\"",'green'))


#displaying contents of todo
def show(args):
    try:
        file = open('todo.txt','r')
        data = file.readlines()
        if data:
            content =""
            for d in data:
                content += str(d)
            #print(data)
                
            sys.stdout.write(content)
        else:
            sys.stdout.write(colored("There are no pending todos!",'red'))
        file.close()
    except FileNotFoundError:
        sys.stdout.write(colored("There are no pending todos!",'red'))


#deleting tasks
def delete(args):
    flag = False
    try:
        f = open("todo.txt", 'r')
        lines = f.readlines()
    except FileNotFoundError:
        sys.stdout.write(colored(f"Error: todo #{args.delitem} does not exist. Nothing deleted.",'red'))
        sys.exit(0)
    lists = []
    with open("todo.txt", 'w') as f:
        for line in lines:
            l = line.split()[0]
            length = len(l)
            num = l[1:length-1]
            #print(num)
            if int(num) == args.delitem:   
                flag = True
            else: 
                lists.append(line)   
        count = len(lists)   
                
        for line in lists:
            item = line.split()[1:]
            content = ""
            for i in item:
                content += str(i) + " "
            f.write(f"[{count}] {content.rstrip()}\n") 
            count -= 1

    if (flag):    
        sys.stdout.write(colored(f"Deleted todo #{args.delitem}.",'green'))
    else:
        sys.stdout.write(colored(f"Error: todo #{args.delitem} does not exist. Nothing deleted.",'red'))


#marking completed tasks
def done(args):
    now = datetime.date.today()
    flag = False
    try:
        f = open("todo.txt", 'r')
        lines = f.readlines()
    except FileNotFoundError:
        sys.stdout.write(colored(f"Error: todo #{args.doneitem} does not exist.",'red'))
        sys.exit(0)
    lists = []
    done_file = open('done.txt', 'a')
    with open("todo.txt", 'w') as f:
        for line in lines:
            l = line.split()[0]
            length = len(l)
            num = l[1:length-1]
            #print(num)
            if int(num) == args.doneitem:  
                d = line.split()[1:]
                content = ""
                for i in d:
                    content += str(i) + " "
                done_file.write(f"x {now} {content.rstrip()}\n") 
                flag = True
            else: 
                lists.append(line)    
        count = len(lists)            
        for line in lists:
            item = line.split()[1:]
            content = ""
            for i in item:
                content += str(i) + " "
            f.write(f"[{count}] {content.rstrip()}\n") 
            count -= 1   
             
    if (flag):    
        sys.stdout.write(colored(f"Marked todo #{args.doneitem} as done.",'green'))
    else:
        sys.stdout.write(colored(f"Error: todo #{args.doneitem} does not exist.",'red'))


#reporting pending and completed tasks
def report(args):
    now = datetime.date.today()
    completed = 0
    pending = 0
    try:
        with open('todo.txt', 'r') as f:    
            data = f.readlines()
            for d in data:
                if(d):
                    pending += 1
    except FileNotFoundError:
        pending = 0
    try:
        with open('done.txt', 'r') as f:    
            data = f.readlines()
            for d in data:
                if(d):
                    completed += 1
    except FileNotFoundError:
        completed = 0
    print(colored(f"{now} Pending : {pending} Completed : {completed}",'yellow'))

#display help when called without arguments or with 'help'
def help(args):
    with open('usage.txt', 'r') as fout:
        data = fout.readlines()
        content =""
        for d in data:
            content += str(d)
    sys.stdout.write(colored(content,'blue'))

my_parser = argparse.ArgumentParser(prog="todo", description="Manage todo list")
my_parser.set_defaults(func=help)
subparsers = my_parser.add_subparsers(dest='command')

help_parser = subparsers.add_parser('help', help="Show usage")
help_parser.set_defaults(func=help)

add_parser = subparsers.add_parser('add', help="Add a new todo")
add_parser.add_argument('additem')
add_parser.set_defaults(func=add)

show_parser = subparsers.add_parser('ls', help="Show remaining todos")
show_parser.set_defaults(func=show)

delete_parser = subparsers.add_parser('del', help="Delete a todo")
delete_parser.add_argument('delitem', type=int)
delete_parser.set_defaults(func=delete)

done_parser = subparsers.add_parser('done', help="Complete a todo")
done_parser.add_argument('doneitem', type=int)
done_parser.set_defaults(func=done)

report_parser = subparsers.add_parser('report', help="Statistics")
report_parser.set_defaults(func=report)

if __name__ == "__main__":
    n = len(sys.argv)
    if n == 2 and sys.argv[1] == "add":
        sys.stdout.write(colored("Error: Missing todo string. Nothing added!",'red'))
        sys.exit(0)
    elif n == 2 and sys.argv[1] == "del":
        sys.stdout.write(colored("Error: Missing NUMBER for deleting todo.",'red'))
        sys.exit(0)
    elif n == 2 and sys.argv[1] == "done":
        sys.stdout.write(colored("Error: Missing NUMBER for marking todo as done.",'red'))
        sys.exit(0)

    args = my_parser.parse_args()   
    args.func(args)
    
    
    
    