import flask
from engine import runner

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/tasks')
def tasks():
    return flask.jsonify(tasks=runner.get_tasks())


@app.route('/task/<task_name>')
def run_task(task_name=None):
    if task_name:
        task = runner.get_task(task_name)

        if task is not None:
            if flask.request.method == 'POST':
                runner.run_task(task_name)

            return flask.jsonify(task)

        flask.abort(404)

    flask.abort(400)


def start():
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run(debug=False)
