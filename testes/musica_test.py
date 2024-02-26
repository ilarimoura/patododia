from musica import Musica


def test_decide_tempo_inicial():
    assert Musica.decide_tempo_inicial(100) == 50

