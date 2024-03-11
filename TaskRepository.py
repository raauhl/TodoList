from IRepository import IRepository


class TaskRepository(IRepository):
    def __init__(self):
        self.tasks_dict = {}

    def create(self, task):
        if task.task_id in self.tasks_dict:
            print("Task with ID {task.taskId} already exists.")
            return
        self.tasks_dict[task.task_id] = task

    def read(self, task_id):
        if task_id not in self.tasks_dict:
            print("Task with ID {task_id} not found.")
            return
        task = self.tasks_dict[task_id]
        return task

    def read_all(self):
        return self.tasks_dict.values()

    def update(self, task_id, task):
        if task_id not in self.tasks_dict:
            print("Task with ID {task_id} not found.")
            return
        self.tasks_dict[task_id] = task

    def delete(self, task_id):
        if task_id not in self.tasks_dict:
            print("Task with ID {task_id} not found.")
            return
        del self.tasks_dict[task_id]