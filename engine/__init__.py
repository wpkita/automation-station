from os.path import isfile
from shutil import copyfile

DEFAULT_CONFIG_PATH = 'engine/default_config.json'
CONFIG_PATH = 'tasks/config.json'

# Create a default config file in the tasks directory if one doesn't exist already
if not isfile(CONFIG_PATH):
    copyfile(DEFAULT_CONFIG_PATH, CONFIG_PATH)
