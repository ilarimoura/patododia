from frases import Frases
from unittest import mock

def test_frase_do_pato_segunda_musica_artista_conhecido():
    assert Frases.fraseDoPato(0, 'Song 2','Blur') == 'Hoje é segunda! Dia de ouvir Blur - Song 2!'


def test_frase_do_pato_terca_musica_artista_conhecido():
    assert Frases.fraseDoPato(1, 'songbird', 'oasis') == 'Hoje é terça! Dia de ouvir oasis - songbird!'


def test_frase_do_pato_quarta_musica_artista_conhecido():
    assert Frases.fraseDoPato(2, 'brutal', 'olivia rodrigo') == 'Hoje é quarta! Dia de ouvir olivia rodrigo - brutal!'


def test_frases_do_pato_quinta_musica_artista_conhecido():
    assert Frases.fraseDoPato(3, 'song 2', 'blur') == 'Hoje é quinta! Dia de ouvir blur - song 2!'


def test_frases_do_pato_sexta_musica_artista_conhecido():
    assert Frases.fraseDoPato(4, 'depois', 'pato fu') == 'Hoje é sexta! Dia de ouvir pato fu - depois!'


def test_frases_do_pato_sabado_musica_artista_conhecido():
    assert Frases.fraseDoPato(5, 'depois', 'pato fu') == 'Hoje é sábado! Dia de ouvir pato fu - depois!'


def test_frases_do_pato_domingo_musica_artista_conhecido():
    assert Frases.fraseDoPato(6, 'depois', 'pato fu') == 'Hoje é domingo! Dia de ouvir pato fu - depois!'

@mock.patch('random.randint')
def test_frases_do_pato_segunda_musica_desconhecida_bora_dancar(randint_mock):
    randint_mock.return_value = 1
    assert Frases.fraseDoPato(0, None, 'pato fu') == 'Hoje é segunda! Bora dançar!'


@mock.patch('random.randint')
def test_frases_do_pato_quarta_musica_desconhecida_aumenta_som(randint_mock):
    randint_mock.return_value = 2
    assert Frases.fraseDoPato(2, None, 'blur') == 'Hoje é quarta! Aumenta o som!'


@mock.patch('random.randint')
def test_frases_do_pato_quinta_artista_desconhecida_aumenta_som(randint_mock):
    randint_mock.return_value = 2
    assert Frases.fraseDoPato(3, 'song 2', None) == 'Hoje é quinta! Aumenta o som!'


@mock.patch('random.randint')
def test_frases_do_pato_sexta_artista_desconhecida_bora_dancar(randint_mock):
    randint_mock.return_value = 1
    assert Frases.fraseDoPato(4, 'song 2', None) == 'Hoje é sexta! Bora dançar!'
