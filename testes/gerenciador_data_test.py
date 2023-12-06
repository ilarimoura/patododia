from gerenciador_data import GerenciadorDatas


def test_achar_posicao_array_mes_par_dia_1():
    assert GerenciadorDatas.achar_posicao_do_array(1, 8) == 31

def test_achar_posicao_array_mes_par_dia_31():
    assert GerenciadorDatas.achar_posicao_do_array(31, 4) == 61

def test_achar_posicao_array_mes_impar_dia_1():
    assert GerenciadorDatas.achar_posicao_do_array(1, 7) == 0

def test_achar_posicao_array_mes_impar_dia_31():
    assert GerenciadorDatas.achar_posicao_do_array(31, 3) == 30





