import json

CONFIG_PATH = 'tasks/config.json'


def get_task_names():
    with open(CONFIG_PATH) as config_file:
        config = json.load(config_file)

    return [t['name'] for t in config['tasks']]
