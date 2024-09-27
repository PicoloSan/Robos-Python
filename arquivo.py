import json

# Carregar o JSON a partir do arquivo
with open("arquivo.json", "r") as file:
    dados = json.load(file)

# Acessar a tag e o valor de um nó específico
print("Tag de Edit1: '%s'" %(dados["Edit1"]["tag"]))
print("Valor de Edit1: '%s'" %(dados["Edit1"]["valor"]))

# Outro exemplo
print("Tag de Edit2: '%s'" %(dados["Edit2"]["tag"]))
print("Valor de Edit2: '%s'" %(dados["Edit2"]["valor"]))

print("Tag de Fechar: '%s'" %(dados["Fechar"]["tag"]))
print("Valor de Fechar: '%s'" %(dados["Fechar"]["valor"]))

print("Tag de Botao1: '%s'" %(dados["Botao1"]["tag"]))
print("Valor de Botao1: '%s'" %(dados["Botao1"]["valor"]))

