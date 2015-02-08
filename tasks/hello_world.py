import json
import pystache


class HelloWorld():
    def __init__(self):
        with open('models/hello_world.json') as config_file:
            # Map JSON properties to this object
            self.__dict__.update(json.load(config_file))

    def process(self):
        renderer = pystache.Renderer(search_dirs='templates')

        with open('bin/hello_world.txt', 'w') as output_file:
            output_file.write(renderer.render(self))
