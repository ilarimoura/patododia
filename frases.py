import random

class Frases:
    @staticmethod
    def __fraseDoDia(musica, artista):
        if not musica or not artista:
            if random.randint(1, 2) == 1:
                return 'Bora dançar!'
            else:
                return 'Aumenta o som!'

        else:
            return 'Dia de ouvir ' + artista + ' - ' + musica + '!'

    @staticmethod
    def __diaDaSemana(dia):
        nomeDoDia = ''
        if dia == 0:
            nomeDoDia = 'Segunda'
        elif dia == 1:
            nomeDoDia = 'Terça'
        elif dia == 2:
            nomeDoDia = 'Quarta'
        elif dia == 3:
            nomeDoDia = 'Quinta'
        elif dia == 4:
            nomeDoDia = 'Sexta'
        elif dia == 5:
            nomeDoDia = 'Sábado'
        elif dia == 6:
            nomeDoDia = 'Domingo'
        return 'Hoje é ' + nomeDoDia + '!'

    @staticmethod
    def fraseDoPato(dia_da_semana, musica, artista):
        return Frases.__diaDaSemana(dia_da_semana) + ' ' + Frases.__fraseDoDia(musica, artista)
