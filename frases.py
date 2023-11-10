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
            nomeDoDia = 'segunda'
        elif dia == 1:
            nomeDoDia = 'terça'
        elif dia == 2:
            nomeDoDia = 'quarta'
        elif dia == 3:
            nomeDoDia = 'quinta'
        elif dia == 4:
            nomeDoDia = 'sexta'
        elif dia == 5:
            nomeDoDia = 'sábado'
        elif dia == 6:
            nomeDoDia = 'domingo'
        return 'Hoje é ' + nomeDoDia + '!'

    @staticmethod
    def fraseDoPato(dia_da_semana, musica, artista):
        return Frases.__diaDaSemana(dia_da_semana) + ' ' + Frases.__fraseDoDia(musica, artista)
