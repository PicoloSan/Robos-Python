import sqlite3
import pandas as pd

# Tentar se conectar ao banco de dados SQLite
try:
    conn = sqlite3.connect('banco_dados_exemplo.db')
    # Consulta SQL para selecionar todos os dados da tabela
    query = "SELECT * FROM exemplo"
    # Usar o pandas para ler os dados do banco de dados SQLite
    df = pd.read_sql_query(query, conn)
    # Fechar a conexão com o banco de dados
    conn.close()

    # Tentar escrever os dados em um arquivo Excel
    try:
        df.to_excel('dados_excel.xlsx', index=False)
        print("Os dados foram exportados para dados_excel.xlsx com sucesso.")
    except Exception as e:
        print(f"Erro ao exportar para o Excel: {e}")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")