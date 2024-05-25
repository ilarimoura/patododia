import random
from datetime import datetime, date
from pytube import Playlist
from frases import Frases
import json
from gerenciador_twitter import GerenciadorTwitter
from gerenciador_data import GerenciadorDatas
from musica import Musica
from video import Video
from arquivo import Arquivo
import time

config = Arquivo.abrir_json('config.json')
dados_musicas_sorteadas = Arquivo.abrir_json('musicas_sorteadas.json')
musicas_programadas = Arquivo.abrir_json('musicas_programadas.json', encoding="utf-8")

hoje = date.today()
dia_de_hoje_string = hoje.strftime('%Y-%m-%d')

musica_programada_do_dia = GerenciadorDatas.achar_data(dia_de_hoje_string, musicas_programadas)

pl = Playlist(config['youtube']['playlist_url'])

tempo_inicial = None
if musica_programada_do_dia:
    videoSorteado = musica_programada_do_dia['url']
    textoTwitter = musica_programada_do_dia['texto']
    tempo_inicial = musica_programada_do_dia.get('tempo_inicial', None)

else:
    videoSorteado = Musica.sorteia_nova_musica(pl,dados_musicas_sorteadas)
    infoVideo = Video.dados_video(videoSorteado)
    textoTwitter = Frases.fraseDoPato(datetime.today().weekday(), infoVideo['song'], infoVideo['artist'])

posicao_musica = GerenciadorDatas.achar_posicao_do_array(hoje.day, hoje.month)
dados_musicas_sorteadas[posicao_musica] = videoSorteado

with open('musicas_sorteadas.json', 'w') as arquivo_musicas_sorteadas_gravar:
    json.dump(dados_musicas_sorteadas, arquivo_musicas_sorteadas_gravar)

print("Downloading " + videoSorteado + "...")

Video.baixar_video(videoSorteado)

print("Generating video...")

Video.gerar_video(tempo_inicial)

print("Video generated...")
pausa_postagem = random.choice([0,60,120,180,240,300])

print("Waiting for: " + str(pausa_postagem) + " seconds...")
time.sleep(pausa_postagem)

print("Wake up...")

twitter = GerenciadorTwitter(config['twitter'])

print("Twitter configs loaded...")

twitter.postar('pato_pronto.mp4', textoTwitter)

print("Finished")