from gerenciador_data import GerenciadorDatas


def test_achar_posicao_array_mes_par_dia_1():
    assert GerenciadorDatas.achar_posicao_do_array(1, 8) == 31

def test_achar_posicao_array_mes_par_dia_31():
    assert GerenciadorDatas.achar_posicao_do_array(31, 4) == 61

def test_achar_posicao_array_mes_impar_dia_1():
    assert GerenciadorDatas.achar_posicao_do_array(1, 7) == 0

def test_achar_posicao_array_mes_impar_dia_31():
    assert GerenciadorDatas.achar_posicao_do_array(31, 3) == 30


def test_achar_data_nao_encontrou():
    assert GerenciadorDatas.achar_data('2023-12-25', [{'data': '2023-12-16', 'url': 'bleh', 'texto':'blah'}]) == None

def test_achar_data_encontrou():
    assert GerenciadorDatas.achar_data('2023-12-25',[{'data':'2023-12-25', 'url': 'bleh', 'texto': 'blah'},
                                                     {'data':'2023-1-1'}]) == {'data':'2023-12-25', 'url': 'bleh', 'texto': 'blah'}







