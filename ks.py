from tasks.hello_world import *
from flask import Flask
import webbrowser

app = Flask(__name__)


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/helloworld')
def hello():
    HelloWorld().process()

    return 'Ran successfully!'

if __name__ == '__main__':
    webbrowser.open_new_tab('http://localhost:5000')
    app.run()
