import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as Querys
c = conn.cursor()

#Executa o comando em SQL
c.execute("""INSERT INTO usuarios(nome,email,senha,data_nascimento) VALUES('Joao','joao_e_maria@gmail.com','Maria123','21/05/2001')""") 

c.execute("""INSERT INTO usuarios(nome,email,senha,data_nascimento) VALUES('Maria','maria_e_joao@gmail.com','Joao123','21/05/2001')""") 

c.execute("""INSERT INTO usuarios(nome,email,senha,data_nascimento) VALUES('Ana','aninha@gmail.com','Joao123','21/05/2001')""") 


print("Tabela de usuarios Criada com sucesso !")

#Grava as informações no Banco de Dados
conn.commit()

#Fecha a conexao com o banco de dados
conn.close()