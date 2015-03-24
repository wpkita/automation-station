from flask import Flask, render_template, request
from engine import runner

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
@app.route('/task/<task_name>')
def home(task_name=None):
    if task_name:
        runner.run_task(task_name)

    tasks = runner.get_task_names()

    return render_template('index.html', tasks=tasks)


def start():
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run()
