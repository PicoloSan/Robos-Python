import json

# função lê arquivo json
"""
o arquivo json pode ser caracterizado como um arquivo de pares chave/valor
chave1 = valor 1
chave2 = valor 2
chave3 = valor 3
chave4 = valor 4
"""
def read_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
        return dados


dados = read_json('exemplo.json')

variavel1 = dados['chave1']
variavel2 = dados['chave2']
variavel3 = dados['chave3']
variavel4 = dados['chave4']

print(variavel1, variavel2, variavel3, variavel4)
variavel_enter = input('Aperte Enter para Encerrar:')

