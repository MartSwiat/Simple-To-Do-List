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


def add_task(tasks, new_task):
    tasks.append({'task': new_task, 'done': False})
    print(f'Task {new_task} added to the List.')


def mark_as_done(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['done'] = True
        print(f"{tasks[task_index - 1]['task']} marked as done")
    else:
        print(f'task with index: {task_index} does not exist. Try again')

show_menu()
tasks_to_do = [{"task": "some task", "done": False}]
# print(type(tasks_to_do))
# show_tasks(tasks_to_do)
# task = input('Please enter task to add: ')
# add_task(tasks_to_do, task)
task_num = int(input('Please enter task number to mark as done: '))
mark_as_done(tasks_to_do, task_num)
