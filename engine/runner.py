from engine import config
import subprocess


def get_tasks():
    return [task for task in config.get_value('tasks')]


def get_task(task_name):
    task = next((task for task in config.get_value('tasks') if task['name'] == task_name), None)

    return task


def add_task(task_name):
    new_task = {
        'name': task_name,
        'path': task_name
    }

    tasks = config.get_value('tasks')

    # Make sure the task doesn't already exist
    task = get_task(task_name)
    if task is None:
        # Update config with new task
        tasks.append(new_task)
        config.set_value('tasks', tasks)

    return task


def run_task(task_name):
    task = get_task(task_name)

    if task:
        subprocess.call('{0}/{1}'.format(config.get_value('taskDirectory'), task['path']))

        return True

    return False
