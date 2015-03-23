from flask import Flask, render_template
from engine import runner


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    tasks = runner.get_task_names()

    return render_template('index.html', tasks=tasks)


def start():
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run()
