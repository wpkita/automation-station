from flask import Flask
import engine


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return app.send_static_file('index.html')


def start():
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run()
