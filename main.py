from datetime import datetime
from moviepy.editor import VideoFileClip, AudioFileClip
from pytube import YouTube, Playlist
import random
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from frases import Frases
import json
from gerenciador_twitter import GerenciadorTwitter


def sorteia_nova_musica(lista_musicas,lista_sorteada):

    sorteio2 = random.choice(lista_musicas)
    print(sorteio2)
    while sorteio2 in lista_sorteada:
        sorteio2 = random.choice(lista_musicas)
    return sorteio2

def dados_video(url):
    youTube = YouTube(url)
    musica = youTube.metadata['song']
    artista = youTube.metadata['artist']
    numeroDeTentativas = 0

    while (musica is None or artista is None) and numeroDeTentativas < 5:
        youTube = YouTube(url)
        musica = youTube.metadata['song']
        artista = youTube.metadata['artist']
        numeroDeTentativas = numeroDeTentativas + 1

    return youTube.metadata

arquivo = open('config.json')
dados1 = json.load(arquivo)
arquivo_musicas_sorteadas = open('musicas_sorteadas.json')
dados_musicas_sorteadas = json.load(arquivo_musicas_sorteadas)
arquivo_musicas_sorteadas.close()

def decide_tempo_inicial(duracao):
    meio = int(duracao / 2)
    return meio

def baixar_video(urlVideo):
    YouTube(urlVideo) \
        .streams \
        .filter(mime_type='audio/mp4', abr='128kbps') \
        .first() \
        .download(filename='audio.mp4', skip_existing=False)

def gerar_video():
    videoPato = VideoFileClip("video.mp4")
    audioPato = AudioFileClip("audio.mp4")
    tempoInicial = decide_tempo_inicial(audioPato.duration)
    tempoFinal = tempoInicial + videoPato.duration
    audioPatoCurto = audioPato.subclip(tempoInicial,tempoFinal)
    final_clip = videoPato.set_audio(audioPatoCurto)
    final_clip = audio_fadein(final_clip, 3)
    final_clip = audio_fadeout(final_clip, 3)
    final_clip.write_videofile("pato_pronto.mp4",codec='libx264', audio_codec='aac')

arquivo_musicas_sorteadas_gravar = open('musicas_sorteadas.json', 'w')

pl = Playlist(dados1['youtube']['playlist_url'])
videoSorteado = sorteia_nova_musica(pl,dados_musicas_sorteadas)
dados_musicas_sorteadas[datetime.today().day - 1] = videoSorteado

json.dump(dados_musicas_sorteadas,arquivo_musicas_sorteadas_gravar)
arquivo_musicas_sorteadas_gravar.close()
baixar_video(videoSorteado)

gerar_video()


arquivo.close()


infoVideo = dados_video(videoSorteado)



textoTwitter = Frases.fraseDoPato(datetime.today().weekday(), infoVideo['song'], infoVideo['artist'])

GerenciadorTwitter.postar('pato_pronto.mp4',
                          textoTwitter,
                          dados1['twitter']['consumer_key'],
                          dados1['twitter']['consumer_secret'],
                          dados1['twitter']['access_token'],
                          dados1['twitter']['access_token_secret']
                        )