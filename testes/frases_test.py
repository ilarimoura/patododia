from frases import Frases
from unittest import mock

def test_frase_do_pato_segunda_musica_artista_conhecido():
    assert Frases.fraseDoPato(0, 'Song 2','Blur') == 'Hoje é Segunda! Dia de ouvir Blur - Song 2'


def test_frase_do_pato_terca_musica_artista_conhecido():
    assert Frases.fraseDoPato(1, 'songbird', 'oasis') == 'Hoje é Terça! Dia de ouvir oasis - songbird'


def test_frase_do_pato_quarta_musica_artista_conhecido():
    assert Frases.fraseDoPato(2, 'brutal', 'olivia rodrigo') == 'Hoje é Quarta! Dia de ouvir olivia rodrigo - brutal'


def test_frases_do_pato_quinta_musica_artista_conhecido():
    assert Frases.fraseDoPato(3, 'song 2', 'blur') == 'Hoje é Quinta! Dia de ouvir blur - song 2'


def test_frases_do_pato_sexta_musica_artista_conhecido():
    assert Frases.fraseDoPato(4, 'depois', 'pato fu') == 'Hoje é Sexta! Dia de ouvir pato fu - depois'


def test_frases_do_pato_sabado_musica_artista_conhecido():
    assert Frases.fraseDoPato(5, 'depois', 'pato fu') == 'Hoje é Sábado! Dia de ouvir pato fu - depois'


def test_frases_do_pato_domingo_musica_artista_conhecido():
    assert Frases.fraseDoPato(6, 'depois', 'pato fu') == 'Hoje é Domingo! Dia de ouvir pato fu - depois'

@mock.patch('random.randint')
def test_frases_do_pato_segunda_musica_desconhecida_bora_dancar(randint_mock):
    randint_mock.return_value = 1
    assert Frases.fraseDoPato(0, None, 'pato fu') == 'Hoje é Segunda! Bora dançar!'


@mock.patch('random.randint')
def test_frases_do_pato_quarta_musica_desconhecida_aumenta_som(randint_mock):
    randint_mock.return_value = 2
    assert Frases.fraseDoPato(2, None, 'blur') == 'Hoje é Quarta! Aumenta o som!'


@mock.patch('random.randint')
def test_frases_do_pato_quinta_artista_desconhecida_aumenta_som(randint_mock):
    randint_mock.return_value = 2
    assert Frases.fraseDoPato(3, 'song 2', None) == 'Hoje é Quinta! Aumenta o som!'


@mock.patch('random.randint')
def test_frases_do_pato_sexta_artista_desconhecida_bora_dancar(randint_mock):
    randint_mock.return_value = 1
    assert Frases.fraseDoPato(4, 'song 2', None) == 'Hoje é Sexta! Bora dançar!'
