import flask
import sqlite3
from flask import Flask, g

app = Flask(__name__)

@app.route("/")
def hello_world():
    cursor = get_db().cursor()
    resposta = cursor.execute("select * from musicas_programadas")
    return flask.render_template('index.html', musicas_programadas = resposta.fetchall())

@app.post("/add_music")
def add_music():
    print(flask.request.form.get('url'))
    print(flask.request.form.get('data'))
    return flask.redirect(flask.url_for('hello_world'))

@app.teardown_appcontext
def close_conection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

DATABASE = 'database.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db