from pytube import YouTube
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.editor import VideoFileClip, AudioFileClip
from musica import Musica


class Video:

    @staticmethod
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

    @staticmethod
    def baixar_video(urlVideo):
        YouTube(urlVideo) \
            .streams \
            .filter(mime_type='audio/mp4', abr='128kbps') \
            .first() \
            .download(filename='audio.mp4', skip_existing=False)

    @staticmethod
    def gerar_video(tempo_inicial_musica_programada=None):
        videoPato = VideoFileClip("video.mp4")
        audioPato = AudioFileClip("audio.mp4")
        tempoInicial = Musica.decide_tempo_inicial(audioPato.duration)

        if tempo_inicial_musica_programada:
            tempoInicial = tempo_inicial_musica_programada

        tempoFinal = tempoInicial + videoPato.duration
        audioPatoCurto = audioPato.subclip(tempoInicial, tempoFinal)
        final_clip = videoPato.set_audio(audioPatoCurto)
        final_clip = audio_fadein(final_clip, 3)
        final_clip = audio_fadeout(final_clip, 3)
        final_clip.write_videofile("pato_pronto.mp4", codec='libx264', audio_codec='aac')