import random


class Musica:
    @staticmethod
    def sorteia_nova_musica(lista_musicas,lista_sorteada):

        sorteio2 = random.choice(lista_musicas)
        print(sorteio2)
        while sorteio2 in lista_sorteada:
            sorteio2 = random.choice(lista_musicas)
        return sorteio2

    @staticmethod
    def decide_tempo_inicial(duracao):
        meio = int(duracao / 2)
        return meio

