from datetime import datetime, date
from pytube import Playlist
from frases import Frases
import json
from gerenciador_twitter import GerenciadorTwitter
from gerenciador_data import GerenciadorDatas
from musica import Musica
from video import Video



arquivo = open('config.json')
dados1 = json.load(arquivo)
arquivo_musicas_sorteadas = open('musicas_sorteadas.json')
dados_musicas_sorteadas = json.load(arquivo_musicas_sorteadas)
arquivo_musicas_sorteadas.close()

hoje = date.today()
dia_de_hoje_string = hoje.strftime('%Y-%m-%d')
musicas_programadas_arquivo = open('musicas_programadas.json', encoding="utf-8")
musicas_programadas = json.load(musicas_programadas_arquivo)
musica_programada_do_dia = GerenciadorDatas.achar_data(dia_de_hoje_string, musicas_programadas)
musicas_programadas_arquivo.close()


arquivo_musicas_sorteadas_gravar = open('musicas_sorteadas.json', 'w')

pl = Playlist(dados1['youtube']['playlist_url'])

if musica_programada_do_dia:
    videoSorteado = musica_programada_do_dia['url']
else:
    videoSorteado = Musica.sorteia_nova_musica(pl,dados_musicas_sorteadas)

posicao_musica = GerenciadorDatas.achar_posicao_do_array(hoje.day, hoje.month)
dados_musicas_sorteadas[posicao_musica] = videoSorteado



json.dump(dados_musicas_sorteadas,arquivo_musicas_sorteadas_gravar)
arquivo_musicas_sorteadas_gravar.close()
Video.baixar_video(videoSorteado)

Video.gerar_video()


arquivo.close()


infoVideo = Video.dados_video(videoSorteado)


if musica_programada_do_dia:
    textoTwitter = musica_programada_do_dia['texto']
else:
    textoTwitter = Frases.fraseDoPato(datetime.today().weekday(), infoVideo['song'], infoVideo['artist'])


GerenciadorTwitter.postar('pato_pronto.mp4',
                          textoTwitter,
                          dados1['twitter']['consumer_key'],
                          dados1['twitter']['consumer_secret'],
                          dados1['twitter']['access_token'],
                          dados1['twitter']['access_token_secret']
                        )