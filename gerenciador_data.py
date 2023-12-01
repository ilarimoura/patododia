class GerenciadorDatas:
    @staticmethod
    def achar_posicao_do_array(dia:int, mes:int):
        if mes % 2 == 0:
            return dia - 1 + 31
        else:
            return dia - 1

    @staticmethod
    def achar_data(data_procurada, array_musicas_especiais):
        for data_especial in array_musicas_especiais:
            if data_procurada == data_especial['data']:
                return data_especial

