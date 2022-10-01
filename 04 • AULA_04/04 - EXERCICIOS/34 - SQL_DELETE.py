import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as Querys
c = conn.cursor()

# Carrega as informações do usuario
id_usuario = 1
p_nome = "Luiza"
p_email = "luiza@gmail.com"
P_senha = "luiza123"
p_data_de_nascimento = "02/02/2002"

#Executa o comando em SQL
c.execute("""DELETE FROM

print(f"Usuario Deletado: {id_usuario}")

#Grava as informações no Banco de Dados
conn.commit()

#Fecha a conexao com o banco de dados
conn.close()