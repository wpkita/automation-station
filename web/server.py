import webbrowser
from flask import Flask
from engine.tasks.hello_world import *

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/helloworld')
def hello():
    HelloWorld().process()

    return 'Ran successfully!'


def start():
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run()
