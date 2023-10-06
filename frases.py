class Frases:
    def __fraseDoDia(self, musica, artista):
        if not musica or not artista:
            return 'Bora dançar!'
        else:
            return 'Dia de ouvir ' + artista + ' - ' + musica + '!'

    def __diaDaSemana(self, dia):
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

    def fraseDoPato(self, dia_da_semana, musica, artista):
        return self.__diaDaSemana(dia_da_semana) + ' ' + self.__fraseDoDia(musica, artista)

#frase = Frases()
#print(frase.fraseDoPato(1, 'everlong', 'foo fighters'))