from ITaskService import ITaskService
from TaskRepository import TaskRepository


class TaskService(ITaskService):

    def __init__(self):
        self.task_repository = TaskRepository()

    def add_task(self, task):
        self.task_repository.create(task)

    def get_task(self, task_id):
        return self.task_repository.read(task_id)

    def modify_task(self, modified_task):
        task_id = modified_task.task_id
        self.task_repository.update(task_id, modified_task)

    def remove_task(self, task_id):
        self.task_repository.delete(task_id)

    def list_tasks(self, filter_start_date=None, filter_end_date=None, filter_is_completed=None, filter_tags=None):
        filtered_tasks = self.task_repository.read_all()

        if filter_start_date and filter_end_date:
            filtered_tasks = [task for task in filtered_tasks if filter_start_date <= task.created_at]

        if filter_is_completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed == filter_is_completed]

        if filter_tags:
            filtered_tasks = [task for task in filtered_tasks if any(tag in task.tags for tag in filter_tags)]

        return filtered_tasks

    def get_statistics(self, start_date, end_date):
        pass

    def get_activitylog(self, start_date, end_date):
        pass
