new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

#1. Переносим из списка new_tasks задачу task_005 в список completed_tasks
completed_tasks.append(new_tasks.pop(4))

#2. Удаляем из списка new_tasks задачу task_007
new_tasks.remove('task_007')
print(new_tasks)

#3. Выводим на экран последнюю задачу из списка new_tasks
print(new_tasks[-1])