import json
import pystache


class HelloWorld():
    def __init__(self):
        with open('models/hello_world.json') as config_file:
            self.config = json.load(config_file)
            self.message = self.config['message']

    def process(self):
        renderer = pystache.Renderer(search_dirs='templates')

        with open('bin/hello_world.txt', 'w') as output_file:
            output_file.write(renderer.render(self))
