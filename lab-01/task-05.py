# Procedural

def schedule_tasks(tasks):
    tasks.sort(key=lambda x: x[1])
    max_reward = 0
    last_end_time = 0
    selected_tasks = []

    for start, end, reward in tasks:
        if start >= last_end_time:
            selected_tasks.append((start, end, reward))
            max_reward += reward
            last_end_time = end

    return max_reward, selected_tasks


tasks = [(1, 3, 10), (2, 5, 20), (3, 6, 15), (4, 7, 30)]
max_reward, schedule = schedule_tasks(tasks)
print("Maximum reward (Procedural):", max_reward)
print("Selected tasks (Procedural):", schedule)


# Functional

def functional_schedule(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    selected_tasks = []
    max_reward = 0
    last_end_time = 0

    for task in sorted_tasks:
        start, end, reward = task
        if start >= last_end_time:
            selected_tasks.append(task)
            max_reward += reward
            last_end_time = end

    return max_reward, selected_tasks


max_reward, schedule = functional_schedule(tasks)
print("Maximum reward (Functional):", max_reward)
print("Selected tasks (Functional):", schedule)
