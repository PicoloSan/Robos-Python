import mysql.connector

# Conectando ao banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="sua_base_de_dados"
)

# Exemplo de consulta SELECT
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sua_tabela")
result_select = mycursor.fetchall()
for row in result_select:
  print(row)

# Exemplo de consulta UPDATE
sql_update = "UPDATE sua_tabela SET coluna = %s WHERE id = %s"
val_update = ("novo_valor", id)
mycursor.execute(sql_update, val_update)
mydb.commit()
print(mycursor.rowcount, "registro(s) afetado(s) pela atualização")

# Exemplo de consulta INSERT
sql_insert = "INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s)"
val_insert = ("valor1", "valor2")
mycursor.execute(sql_insert, val_insert)
mydb.commit()
print("Novo registro inserido. ID:", mycursor.lastrowid)

# Exemplo de consulta DELETE
sql_delete = "DELETE FROM sua_tabela WHERE id = %s"
val_delete = (id,)
mycursor.execute(sql_delete, val_delete)
mydb.commit()
print(mycursor.rowcount, "registro(s) removido(s)")

# Fechando a conexão
mydb.close()
