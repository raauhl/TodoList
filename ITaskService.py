from abc import ABC, abstractmethod


class ITaskService(ABC):
    @abstractmethod
    def add_task(self, task):
        pass

    @abstractmethod
    def get_task(self, task_id):
        pass

    @abstractmethod
    def modify_task(self, task):
        pass

    @abstractmethod
    def remove_task(self, task_id):
        pass

    @abstractmethod
    def list_tasks(self, start_date, end_date, is_completed, tags):
        pass

    @abstractmethod
    def get_statistics(self, start_date, end_date):
        pass

    @abstractmethod
    def get_activitylog(self, start_date, end_date):
        pass
