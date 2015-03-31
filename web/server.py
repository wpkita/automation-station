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


@app.route('/dropbox/auth')
def dropbox_auth():
    dropbox_config = {
        'client_id': 'ax0k4eseumuduy8',
        'response_type': 'token',
        'redirect_uri': 'http://localhost:5000'
    }

    dropbox_auth_uri = 'https://www.dropbox.com/1/oauth2/authorize?client_id={0}&response_type={1}&redirect_uri={2}'\
        .format(dropbox_config['client_id'], dropbox_config['response_type'], dropbox_config['redirect_uri'])

    return flask.redirect(dropbox_auth_uri)


@app.route('/dropbox/token', methods=['POST'])
def dropbox_token():
    token = flask.request.json['access_token']
    return token


def start():
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run(debug=False)
