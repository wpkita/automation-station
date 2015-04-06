from engine import auth, runner
import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True


# Decorator to be used in the future for authorizing web requests
def authorized(f):
    def wrapper(*args, **kwargs):
        if auth.is_authorized():
            return f(*args, **kwargs)
        else:
            return flask.redirect(auth.get_auth_uri())
    return wrapper


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/tasks')
def tasks():
    return flask.jsonify(tasks=runner.get_tasks())


@app.route('/task/<task_name>', methods=['GET', 'POST'])
def task(task_name=None):
    if task_name:
        if flask.request.method == 'POST':
            task, did_succeed = runner.add_task(task_name)

            if not did_succeed:
                flask.abort(409)
        else:
            task = runner.get_task(task_name)

        return flask.jsonify(task)

    flask.abort(400)


@app.route('/run/<task_name>', methods=['PUT'])
def run_task(task_name=None):
    if task_name:
        task = runner.get_task(task_name)

        if task is not None:
            runner.run_task(task_name)

            return flask.jsonify(task)

        flask.abort(404)

    flask.abort(400)


@app.route('/authorize')
def authorize():
    if not auth.is_authorized():
        return flask.redirect(auth.get_auth_uri())

    return flask.redirect('/')


@app.route('/token', methods=['POST'])
def token():
    token = flask.request.json['access_token']

    auth.set_auth_token(token)

    return token


def start():
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run(debug=False)
