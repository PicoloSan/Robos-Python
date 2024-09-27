import mysql.connector

# Conectando ao banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="sua_base_de_dados"
)

# Definindo a stored procedure com dois parâmetros
mycursor = mydb.cursor()
mycursor.execute(
    """
    CREATE PROCEDURE sua_procedure(IN param1 INT, IN param2 VARCHAR(255))
    BEGIN
        SELECT * FROM sua_tabela WHERE coluna1 = param1 AND coluna2 = param2;
    END
    """
)

# Executando a stored procedure com valores para os parâmetros
params = (valor_param1, valor_param2)
mycursor.callproc("sua_procedure", params)
result_procedure = mycursor.stored_results()

# Exibindo os registros do resultado
for result in result_procedure:
    for row in result.fetchall():
        print(row)

# Fechando a conexão
mydb.close()
