import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template('index.html')

@app.post("/add_music")
def add_music():
    print(flask.request.form.get('url'))
    print(flask.request.form.get('data'))
    return flask.redirect(flask.url_for('hello_world'))

