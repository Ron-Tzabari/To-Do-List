FILEPATH = 'todos.txt'

def readFile():
    with open(FILEPATH) as file:
        file.read()

def get_tasks():
    tasks = []
    with open(FILEPATH, 'r') as file:
        new_tasks = []
        tasks = file.readlines()
        for task in tasks:
            task = task.strip('\n')
            new_tasks.append(task)
    return new_tasks

def write_tasks(tasks):
    with open(FILEPATH, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

