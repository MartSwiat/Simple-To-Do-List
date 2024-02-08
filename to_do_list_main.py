def show_menu():
    print('\nTO-DO-LIST-Menu: ')
    menu = ('Tasks', 'Add Task', 'Mark Task as Done', 'Remove Task', 'Exit')
    for i, option in enumerate(menu, start=1):
        print(f'{i}. {option}')


# tasks as a list of directories with keys 'task' and 'done'
def show_tasks(tasks):
    if not tasks:
        print('No tasks in the list!')
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - {'DONE' if task['done'] else 'NOT DONE'}")


tasks = [{"task": "some task", "done": False}]
print(type(tasks))
show_tasks(tasks)
