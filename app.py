import flask
import sqlite3
from flask import Flask, g
from video import Video
from gerenciador_twitter import GerenciadorTwitter
from arquivo import Arquivo

app = Flask(__name__)

@app.route("/")
def hello_world():
    cursor = get_db().cursor()
    resposta = cursor.execute("select * from musicas_programadas")
    return flask.render_template('index.html', musicas_programadas = resposta.fetchall())

@app.post("/add_music")
def add_music():
    cursor = get_db().cursor()
    url = flask.request.form.get('url')
    data = flask.request.form.get('data')
    texto = flask.request.form.get('texto')
    cursor.execute('insert into musicas_programadas(url, data, texto) values(?,?,?)', (url, data, texto))
    get_db().commit()
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

@app.get('/agora')
def get_agora():
    return flask.render_template('form_agora.html')

@app.post('/agora')
def post_agora():
    url = flask.request.form.get('url')
    texto = flask.request.form.get('texto')
    tempo_inicial = int(flask.request.form.get('tempo_inicial'))
    senha = flask.request.form.get("senha")

    config = Arquivo.abrir_json('config.json')

    if senha != config['chave_seguranca']:
        return "Senha incorreta", 400

    Video.baixar_video(url)
    Video.gerar_video(tempo_inicial)
    twitter = GerenciadorTwitter(config['twitter'])
    twitter.postar('pato_pronto.mp4', texto)

    return "postei", 200


if __name__ == '__main__':
    config = Arquivo.abrir_json('config.json')
    app.run(host="0.0.0.0", port=config['server_port'])