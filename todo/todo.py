import sys

def show_help():
    print("\nSimple ToDo App")
    print("Usage: ")
    print(" add <task> - Add a new task")
    print(" list - List all tasks")
    print(" done <task_number> - Mark a task as done")
    print(" help - Show this help message\n")

def add_task(task):
    with open("todo.txt","a")as file:
        file.write(task + "\n")
    print(f"Added task: {task}")

def list_tasks():
    try:
        with open("todo.txt","r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks,1):
                    print_task(i,task.strip())
    except FileNotFoundError:
        print("No tasks found.")

def mark_done(task_number):
    try:
        with open("todo.txt","r") as file:
            tasks = file.readlines()
            if 0 < task_number <= len(tasks):
                tasks.pop(task_number - 1)
                with open("todo.txt","w") as file:
                    file.writelines(tasks)
                print(f"Marked task {task_number} as done.")
            else:
                print("Invalid task number.")
    except FileNotFoundError:
        print("No task found.")

def print_task(task_number,task):
    task_info = f"Task {task_number}: {task}"
    border = '+' + '-' * (len(task_info) +2) + '+'
    print(border)
    print(f"| {task_info} |")
    print(border)

if __name__=="__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1]
        if command == "add":
            add_task("".join(sys.argv[2:]))
        elif command == "list":
            list_tasks()
        elif command == "done":
            if len(sys.argv) == 3 and sys.argv[2].isdigit():
                mark_done(int(sys.argv[2]))
            else:
                print("Invalid task number.")
        else:
            show_help()



