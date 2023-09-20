import tweepy
from datetime import datetime
from moviepy.editor import VideoFileClip, AudioFileClip

def gerar_video():
    videoPato = VideoFileClip("video.mp4")
    audioPato = AudioFileClip("audio.mp3")
    audioPatoCurto = audioPato.set_duration(videoPato.duration)
    final_clip = videoPato.set_audio(audioPatoCurto)
    final_clip.write_videofile("pato_pronto.mp4",codec='libx264', audio_codec='aac')

def diaDaSemana(dia):
    nomeDoDia =''
    if dia == 0:
        nomeDoDia = 'segunda'
    elif dia == 1:
        nomeDoDia ='terça'
    elif dia == 2:
        nomeDoDia ='quarta'
    elif dia == 3:
        nomeDoDia ='quinta'
    elif dia == 4:
        nomeDoDia ='sexta'
    elif dia == 5:
        nomeDoDia ='sábado'
    elif dia == 6:
        nomeDoDia ='domingo'
    return 'Hoje é ' + nomeDoDia

gerar_video()

auth = tweepy.OAuth1UserHandler('kToF73rieDIO3tECcFk3jDdFh','snOnIhgU61UkleRlTGa85L84rPet4qcbB4IOJFDfXcpLXfAdOA', '1700698252700532736-2omHU8dS0orm3yi9wHfaI3T5By66FT', 'ecCouCcgmCJCniNY9uDiITDVriHax4qQEphvZzz63cH3L')

api = tweepy.API(auth)
patoDoDia = api.media_upload('pato_pronto.mp4')
print(patoDoDia)

client = tweepy.Client(
    consumer_key="kToF73rieDIO3tECcFk3jDdFh",
    consumer_secret="snOnIhgU61UkleRlTGa85L84rPet4qcbB4IOJFDfXcpLXfAdOA",
    access_token="1700698252700532736-2omHU8dS0orm3yi9wHfaI3T5By66FT",
    access_token_secret="ecCouCcgmCJCniNY9uDiITDVriHax4qQEphvZzz63cH3L"
)

create1 = client.create_tweet(media_ids=[patoDoDia.media_id], text=diaDaSemana(datetime.today().weekday()))
print(create1)








