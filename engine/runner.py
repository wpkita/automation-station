from engine import config
import subprocess


def get_tasks():
    return [task for task in config.get_value('tasks')]


def get_task(task_name):
    task = next((task for task in config.get_value('tasks') if task['name'] == task_name), None)

    return task


def run_task(task_name):
    task = get_task(task_name)

    if task:
        subprocess.call('./tasks/{0}'.format(task['path']))

        return True

    return False
