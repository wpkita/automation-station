import json
from os.path import isfile
from shutil import copyfile

DEFAULT_CLOUD_CONFIG_PATH = 'engine/default_cloud_config.json'
CLOUD_CONFIG_FILE_NAME = 'cloud_config.json'
cloud_config_path = ''

DEFAULT_LOCAL_CONFIG_PATH = 'engine/default_local_config.json'
LOCAL_CONFIG_PATH = 'tasks/local_config.json'


# Create a default config file in the tasks directory if one doesn't exist already
def init_local_config():
    if not isfile(LOCAL_CONFIG_PATH):
        copyfile(DEFAULT_LOCAL_CONFIG_PATH, LOCAL_CONFIG_PATH)


def init_cloud_config():
    if not isfile(get_cloud_config_path()):
        copyfile(DEFAULT_CLOUD_CONFIG_PATH, get_cloud_config_path())


def get_task_directory():
    config = load_config(LOCAL_CONFIG_PATH)

    return config['taskDirectory']


def get_cloud_config_path():
    return '{0}/{1}'.format(get_task_directory(), CLOUD_CONFIG_FILE_NAME)


# Load the config file's contents into a dictionary
def load_config(path):
    with open(path) as config_file:
        config = json.load(config_file)
    return config


def save_config(path, config):
    with open(path, 'w') as f:
        f.writelines(json.dumps(config, sort_keys=True, indent=2, separators=(',', ': ')))


def get_value(key):
    config = load_config(get_cloud_config_path())

    return config[key]


def set_value(key, value):
    config = load_config(get_cloud_config_path())

    config[key] = value

    save_config(get_cloud_config_path(), config)

