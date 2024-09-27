import mysql.connector

# Conectando ao banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="sua_base_de_dados"
)

# Exemplo de comando CREATE TABLE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE sua_nova_tabela (id INT PRIMARY KEY, nome VARCHAR(255))")

# Exemplo de comando STORED PROCEDURE
mycursor.execute("CREATE PROCEDURE sua_procedure() SELECT * FROM sua_tabela")

# Exemplo de criação de VIEW
mycursor.execute("CREATE VIEW sua_view AS SELECT coluna1, coluna2 FROM sua_tabela")

# Exemplo de comando ALTER TABLE
mycursor.execute("ALTER TABLE sua_tabela ADD COLUMN nova_coluna VARCHAR(255)")

# Exemplo de comando DROP TABLE
mycursor.execute("DROP TABLE sua_tabela")

# Fechando a conexão
mydb.close()
