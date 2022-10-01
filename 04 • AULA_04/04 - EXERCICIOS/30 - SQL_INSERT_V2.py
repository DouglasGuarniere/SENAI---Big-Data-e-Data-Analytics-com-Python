import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as Querys
c = conn.cursor()

# Lista com os dados dos novos usuarios
lista = {
    ('Felipe','felipe123@gmail.com','123felipe','10/04/2000'),
    ('Ariane','ariane7costa@gmail.com','123ariane','31/10/1975'),
    ('Levi','levi@gmail.com','levi123','24/06/1988'),
    ('Mariana','marimariana@hotmail.com','eusoulinda123','21/05/2001')
}

#Executa o comando em SQL
c.executemany("""INSERT INTO usuarios(nome,email,senha,data_nascimento) VALUES('?,?,?,?')""",lista) 


print("Adicionado novos usuarios na tabela 'usuarios'")

#Grava as informações no Banco de Dados
conn.commit()

#Fecha a conexao com o banco de dados
conn.close()