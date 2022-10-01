import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as Querys
c = conn.cursor()

#Executa o comando em SQL
c.execute("""SELET * FROM usuarios )


for


print("Adicionado novo usuarios na tabela 'usuarios'")

#Grava as informações no Banco de Dados
conn.commit()

#Fecha a conexao com o banco de dados
conn.close()