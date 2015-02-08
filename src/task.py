import json
import pystache
import re


class Task():
    def __init__(self):
        self.file_root_name = camel_case_to_underscore(self.__class__.__name__)

        with open('models/{0}.json'.format(self.file_root_name)) as config_file:
            # Map JSON properties to this object
            self.__dict__.update(json.load(config_file))

    def process(self):
        renderer = pystache.Renderer(search_dirs='templates')

        with open('bin/{0}.txt'.format(self.file_root_name), 'w') as output_file:
            output_file.write(renderer.render(self))


def camel_case_to_underscore(text):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

