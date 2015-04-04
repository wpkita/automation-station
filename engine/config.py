import json
from os.path import isfile
from shutil import copyfile

DEFAULT_CONFIG_PATH = 'engine/default_config.json'
CONFIG_PATH = 'tasks/config.json'


# Create a default config file in the tasks directory if one doesn't exist already
def init_config():
    if not isfile(CONFIG_PATH):
        copyfile(DEFAULT_CONFIG_PATH, CONFIG_PATH)


# Load the config file's contents into a dictionary
def load_config():
    with open(CONFIG_PATH) as config_file:
        config = json.load(config_file)
    return config


def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        f.writelines(json.dumps(config, sort_keys=True, indent=2, separators=(',', ': ')))


def get_value(key):
    config = load_config()

    return config[key]


def set_value(key, value):
    config = load_config()

    config[key] = value

    save_config(config)

init_config()

