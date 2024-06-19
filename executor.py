from pytube import Playlist
from arquivo import Arquivo
from datetime import datetime, date
from gerenciador_data import GerenciadorDatas
from postagem import Postagem
from musica import Musica
from video import Video
from frases import Frases
import json

class Executor:
    def __init__(self):
        self.config = Arquivo.abrir_json('config.json')
        self.musicas_sorteadas = Arquivo.abrir_json('musicas_sorteadas.json')
        self.musicas_programadas = Arquivo.abrir_json('musicas_programadas.json', encoding="utf-8")
        self.hoje = date.today()
        self.dia_de_hoje_string = self.hoje.strftime('%Y-%m-%d')
        self.playlist = Playlist(self.config['youtube']['playlist_url'])

    def run(self):
        postagem = self.cria_postagem()
        self.grava_musica(postagem.url)

    def cria_postagem(self):
        musica_programada_do_dia = GerenciadorDatas.achar_data(self.dia_de_hoje_string, self.musicas_programadas)
        tempo_inicial = None
        if musica_programada_do_dia:
            url = musica_programada_do_dia['url']
            texto = musica_programada_do_dia['texto']
            tempo_inicial = musica_programada_do_dia.get('tempo_inicial', None)
        else:
            url = Musica.sorteia_nova_musica(self.playlist, self.musicas_sorteadas)
            info_video = Video.dados_video(url)
            texto = Frases.fraseDoPato(datetime.today().weekday(), info_video['song'], info_video['artist'])

        return Postagem(url, texto, tempo_inicial)

    def grava_musica(self, url):
        posicao_musica = GerenciadorDatas.achar_posicao_do_array(self.hoje.day, self.hoje.month)
        self.musicas_sorteadas[posicao_musica] = url

        with open('musicas_sorteadas.json', 'w') as arquivo_musicas_sorteadas_gravar:
            json.dump(self.musicas_sorteadas, arquivo_musicas_sorteadas_gravar)

    def postar(self url):
        print("Downloading " + videoSorteado + "...")

        Video.baixar_video(url)

        print("Generating video...")

        Video.gerar_video(tempo_inicial)

        print("Video generated...")
        pausa_postagem = random.choice([0, 60, 120, 180, 240, 300])

        print("Waiting for: " + str(pausa_postagem) + " seconds...")
        time.sleep(pausa_postagem)

        print("Wake up...")

        twitter = GerenciadorTwitter(config['twitter'])

        print("Twitter configs loaded...")

        twitter.postar('pato_pronto.mp4', textoTwitter)

        print("Finished")

