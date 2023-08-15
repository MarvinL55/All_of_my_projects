import time

task = {}
current_task = None
start_time = None

while True:
    # Print the current task and elapsed time
    if current_task:
        elapsed_time = time.time() -start_time
        print(f"Current task: {current_task} - Elapsed time: {elapsed_time:.2f} seconds")

    # Prompt the user to select an action
    action = input("\nSelect an action: \n1. Start a new task\n2. Stop the current task\n3. View task history\n4. Quit\n")

    # Start a new task
    if action == "1":
        if current_task:
            print("Please stop the current task before starting a new one")
        else:
            task_name = input("Enter the name of the new task: ")
            task[task_name] = task.get(task_name, 0)
            current_task = task_name
            start_time = time.time()

    # Stop the current task
    elif action == "2":
        if not current_task:
            print("there is no task currently in progress.")
        else:
            elapsed_time = time.time() - start_time
            task[current_task] += elapsed_time
            current_task = None
            start_time = None

    elif action == "3":
        if not task:
            print("There is no task history")
        else:
            print("Task history")
            for task, time_spent in task.items():
                print(f"{task}: {time_spent:.2f} seconds")

    # Quit program
    elif action == "4":
        break

    #  Invalid action
    else:
        print("Invalid action. Please try again.")