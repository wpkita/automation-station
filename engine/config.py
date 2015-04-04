import json
from os.path import isfile
from shutil import copyfile

DEFAULT_CONFIG_PATH = 'engine/default_config.json'
CONFIG_PATH = 'tasks/config.json'


def init_config():
    # Create a default config file in the tasks directory if one doesn't exist already
    if not isfile(CONFIG_PATH):
        copyfile(DEFAULT_CONFIG_PATH, CONFIG_PATH)


def get_value(key):
    return config[key]


def set_value(key, value):
    config[key] = value

    with open(CONFIG_PATH, 'w') as f:
        f.writelines(json.dumps(config, sort_keys=True, indent=2, separators=(',', ': ')))

# Create a config file if one does not exist already
init_config()

# Load the config file's contents
with open(CONFIG_PATH) as config_file:
    config = json.load(config_file)
