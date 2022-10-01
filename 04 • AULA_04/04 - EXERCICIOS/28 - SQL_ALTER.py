import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as Querys
c = conn.cursor()

#Executa o comando em SQL
c.execute("""ALTER TABLE usuarios ADD data_nascimento VARCHAR(10)""")

#Mostra mensagem para o usuario
print("Adicionado nova coluna 'data_nascimento' dentro da tabela 'usuarios'")

#Grava as informações no Banco de Dados
conn.commit()

#Fecha a conexao com o banco de dados
conn.close()