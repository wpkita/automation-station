import json
import subprocess

CONFIG_PATH = 'tasks/config.json'

with open(CONFIG_PATH) as config_file:
    config = json.load(config_file)


def get_task_names():
    return [t['name'] for t in config['tasks']]


def run_task(task_name):
    print('\n\n')
    print(task_name)
    print(config)
    task_path, = (t['path'] for t in config['tasks'] if t['name'] == task_name)
    print(task_path)
    print('\n\n')
    subprocess.call('./tasks/{0}'.format(task_path))
