to_do_list = []

while True:
    task = input("Enter a task (or 'done' to stop): ")
    if task.lower() == 'done':
        break
    else:
        to_do_list.append(task)

print("\nYour tasks are:")
for task in to_do_list:
    print(f"- {task}")