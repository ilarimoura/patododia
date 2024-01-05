import json

class Arquivo:

    @staticmethod
    def abrir_json(nome_arquivo, encoding=None):
        with open(nome_arquivo, encoding=encoding) as arquivo:
            return json.load(arquivo)
