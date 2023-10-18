import tweepy
from datetime import datetime
from moviepy.editor import VideoFileClip, AudioFileClip
from pytube import YouTube, Playlist
import random
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from correct_metadata import CorrectMetadata
from frases import Frases
import json


arquivo = open('config.json')
dados1 = json.load(arquivo)


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



pl = Playlist('https://www.youtube.com/playlist?list=PLmGO3ZOd8ezKutaz9luKJhx0_vnHUR1Aj')
videoSorteado = random.choice(pl)
baixar_video(videoSorteado)

gerar_video()

auth = tweepy.OAuth1UserHandler(dados1['twitter']['consumer_key'],
                                dados1['twitter']['consumer_secret'],
                                dados1['twitter']['access_token'],
                                dados1['twitter']['access_token_secret'])

api = tweepy.API(auth)
patoDoDia = api.media_upload('pato_pronto.mp4')
print(patoDoDia)

client = tweepy.Client(
    consumer_key=dados1['twitter']['consumer_key'],
    consumer_secret=dados1['twitter']['consumer_secret'],
    access_token=dados1['twitter']['access_token'],
    access_token_secret=dados1['twitter']['access_token_secret'],


)
arquivo.close()

testeVideo = YouTube(videoSorteado)
dados = CorrectMetadata(testeVideo.metadata)

frases = Frases()
textoTwitter = frases.fraseDoPato(datetime.today().weekday(), dados.song, dados.artist)

create1 = client.create_tweet(media_ids=[patoDoDia.media_id], text=textoTwitter)
print(create1)