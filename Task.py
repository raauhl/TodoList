from _datetime import datetime


class Task:
    def __init__(self, task_id, description, deadline, tags=None):

        self.task_id = task_id

        self.description = description

        self.deadline = deadline

        self.tags = tags if tags else []

        self.completed = False

        self.created_at = datetime.now()

    def show_details(self):
        print(f"Task ID: {self.task_id}")
        print(f"Description: {self.description}")
        print(f"Deadline: {self.deadline}")
        print(f"Tags: {', '.join(self.tags)}")
        print(f"Completed: {'Yes' if self.completed else 'No'}")
        print(f"Created At: {self.created_at}")
        print()
