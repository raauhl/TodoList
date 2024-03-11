from Task import Task
from TaskService import TaskService
from datetime import datetime

taskService = TaskService()

task1 = Task(1, "Complete Python project", datetime(2024, 4, 1), ["python", "study"])
task2 = Task(2, "Study for exams", datetime(2024, 3, 15), ["study", "exams"])
task3 = Task(3, "Write documentation", datetime(2024, 3, 20), ["documentation", "writing"])
task4 = Task(4, "Exercise", datetime(2024, 3, 13), ["health", "exercise", "books"])
task5 = Task(5, "Read a book", datetime(2024, 3, 18), ["reading", "books"])

print("CREATE TASKS.")
taskService.add_task(task1)
taskService.add_task(task2)
taskService.add_task(task3)
taskService.add_task(task4)
taskService.add_task(task5)

print("GET ALL TASKS")
tasks = taskService.list_tasks()
for t in tasks:
    t.show_details()

print("GET TASKS BY ID")
task1 = taskService.get_task(1)
task1.show_details()
task2 = taskService.get_task(3)
task2.show_details()

print("MODIFY TASKS.")
taskService.add_task(Task(6, "Task is even", datetime(2024, 3, 18), ["reading", "books"]))
task7 = taskService.get_task(6)
task7.show_details()

task7.description = "Task desc changed"
task7.completed = True
taskService.modify_task(task7)
task7 = taskService.get_task(6)
task7.show_details()


print("LIST TASK FILTER.")
tasks = taskService.list_tasks(filter_is_completed=True)
for t in tasks:
    t.show_details()

"""
tasks = taskService.list_tasks(filter_start_date=datetime.strptime("2024-03-15", "%Y-%m-%d"), filter_end_date=datetime.strptime("2024-03-20", "%Y-%m-%d"))
for t in tasks:
    t.show_details()
"""

tasks = taskService.list_tasks(filter_tags=["books"])
for t in tasks:
    t.show_details()











