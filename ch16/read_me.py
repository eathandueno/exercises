# There is no starting point for the exercise for this chapter.
class Task:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, type):
        self.tasks.append(Task(name, type))

    def delete_task(self, name):
        self.tasks = [task for task in self.tasks if task.name != name]

    def order_tasks(self):
        self.tasks.sort(key=lambda task: task.name)


task_list = TaskList()
task_list.add_task('Task 1', 'Type 1')
task_list.add_task('Task 2', 'Type 2')
task_list.order_tasks()
task_list.delete_task('Task 1')
print(task_list.tasks)