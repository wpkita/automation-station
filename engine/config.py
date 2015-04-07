import json
from os.path import isfile
from shutil import copyfile


class Config:
    def __init__(self, default_config_path, config_path):
        self.config_path = config_path
        self.recreate_config_file(default_config_path)
        self.config = self.load_config()

    def recreate_config_file(self, default_config_path):
        if not isfile(self.config_path):
            copyfile(default_config_path, self.config_path)

    # Load the config file's contents into a dictionary
    def load_config(self):
        with open(self.config_path) as config_file:
            config = json.load(config_file)
        return config

    def save_config(self):
        with open(self.config_path, 'w') as f:
            f.writelines(json.dumps(self.config, sort_keys=True, indent=2, separators=(',', ': ')))

    def get_value(self, key):
        return self.config[key]

    def set_value(self, key, value):
        self.config[key] = value

        self.save_config()


class CloudConfig(Config):
    def __init__(self, config_directory):
        default_config_path = 'engine/default_cloud_config.json'
        config_file_name = 'cloud_config.json'
        config_path = '{0}/{1}'.format(config_directory, config_file_name)

        Config.__init__(self, default_config_path, config_path)


class LocalConfig(Config):
    def __init__(self):
        default_config_path = 'engine/default_local_config.json'
        config_path = 'tasks/local_config.json'

        Config.__init__(self, default_config_path, config_path)

    def get_task_directory(self):
        return self.config['taskDirectory']



















