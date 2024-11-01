# Procedural

def procedural(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x['time'])
    total_wait_time = 0
    current_time = 0
    task_order = []

    for task in sorted_tasks:
        current_time += task['time']
        total_wait_time += current_time
        task_order.append(task['id'])
    return task_order, total_wait_time


tasks = [
    {'id': 1, 'time': 4, 'reward': 20},
    {'id': 2, 'time': 2, 'reward': 10},
    {'id': 3, 'time': 3, 'reward': 15},
    {'id': 4, 'time': 1, 'reward': 5}
]

task_order, total_wait_time = procedural(tasks)
print("Optimal task order (Procedural):", task_order)
print("Total wait time (Procedural):", total_wait_time)


# Functional

def functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x['time'])
    task_order = list(map(lambda x: x['id'], sorted_tasks))

    cumulative_time = 0
    total_wait_time = sum(
        (cumulative_time := cumulative_time + task['time']) for task in sorted_tasks
    )
    return task_order, total_wait_time


task_order, total_wait_time = functional(tasks)
print("Optimal task order (Functional):", task_order)
print("Total wait time (Functional):", total_wait_time)
