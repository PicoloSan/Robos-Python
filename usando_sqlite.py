import sqlite3
from openpyxl import load_workbook

# Carregar o arquivo do Excel
wb = load_workbook('seu_arquivo.xlsx')
sheet = wb.active
column_values = [cell.value for cell in sheet['D']]

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('seu_banco_de_dados.db')
cursor = conn.cursor()

# Criando a tabela no banco de dados (se necessário)
cursor.execute('''CREATE TABLE IF NOT EXISTS sua_tabela (
                    id INTEGER PRIMARY KEY,
                    valor TEXT
                )''')

# Iniciar uma transação
cursor.execute('BEGIN TRANSACTION')

try:
    # Iterar sobre as células da coluna e atualizar o banco de dados
    for value in column_values:
        try:
            valor = cell.value
            cursor.execute('INSERT INTO sua_tabela (valor) VALUES (?)', (valor,))
        except Exception as e:
            # Captura o erro, mas continua para a próxima célula
            print(f"Erro ao inserir {cell.coordinate}: {e}")
            continue

    # Commit para salvar as alterações se não houver erros
    conn.commit()
    print("Dados inseridos com sucesso.")
except Exception as e:
    # Rollback em caso de erro
    conn.rollback()
    print(f"Erro ao inserir dados: {e}")
finally:
    # Fechar a conexão
    conn.close()