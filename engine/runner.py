import json
import subprocess

CONFIG_PATH = 'tasks/config.json'

with open(CONFIG_PATH) as config_file:
    config = json.load(config_file)


def get_tasks():
    return [task for task in config['tasks']]


def get_task(task_name):
    task = next((task for task in config['tasks'] if task['name'] == task_name), None)

    return task


def run_task(task_name):
    task = get_task(task_name)

    if task:
        subprocess.call('./tasks/{0}'.format(task['path']))

        return True

    return False
