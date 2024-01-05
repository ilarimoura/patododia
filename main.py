from datetime import datetime, date
from pytube import Playlist
from frases import Frases
import json
from gerenciador_twitter import GerenciadorTwitter
from gerenciador_data import GerenciadorDatas
from musica import Musica
from video import Video
from arquivo import Arquivo


config = Arquivo.abrir_json('config.json')
dados_musicas_sorteadas = Arquivo.abrir_json('musicas_sorteadas.json')
musicas_programadas = Arquivo.abrir_json('musicas_programadas.json', encoding="utf-8")

hoje = date.today()
dia_de_hoje_string = hoje.strftime('%Y-%m-%d')

musica_programada_do_dia = GerenciadorDatas.achar_data(dia_de_hoje_string, musicas_programadas)


pl = Playlist(config['youtube']['playlist_url'])

if musica_programada_do_dia:
    videoSorteado = musica_programada_do_dia['url']
    textoTwitter = musica_programada_do_dia['texto']
else:
    videoSorteado = Musica.sorteia_nova_musica(pl,dados_musicas_sorteadas)
    infoVideo = Video.dados_video(videoSorteado)
    textoTwitter = Frases.fraseDoPato(datetime.today().weekday(), infoVideo['song'], infoVideo['artist'])

posicao_musica = GerenciadorDatas.achar_posicao_do_array(hoje.day, hoje.month)
dados_musicas_sorteadas[posicao_musica] = videoSorteado

with open('musicas_sorteadas.json', 'w') as arquivo_musicas_sorteadas_gravar:
    json.dump(dados_musicas_sorteadas, arquivo_musicas_sorteadas_gravar)

Video.baixar_video(videoSorteado)
Video.gerar_video()

twitter = GerenciadorTwitter(config['twitter'])
twitter.postar('pato_pronto.mp4', textoTwitter)
