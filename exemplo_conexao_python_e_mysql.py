import mysql.connector

# Conectar ao banco de dados
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="teste"
    )
    print("Conexão bem-sucedida!")
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
