import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as Querys
c = conn.cursor()

# Carrega as informações do usuario
p_nome = input("nome:")
p_email = input("email:")
P_senha = input("Senha:")
p_data_de_nascimento = input("Data de Nascimento (dd/mm/yyyy):")

#Executa o comando em SQL
c.execute("""INSERT INTO usuarios(nome, email, senha, data_nascimento)
    VALUES(?,?,?,?)""",
    (p_nome, p_email, P_senha, p_data_de_nascimento)
    )

print("Adicionado novo usuarios na tabela 'usuarios'")

#Grava as informações no Banco de Dados
conn.commit()

#Fecha a conexao com o banco de dados
conn.close()