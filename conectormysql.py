import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database= "bd_walisson"
)

meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)

resultado = meucursor.fetchall()
for x in resultado:
    print(x)


nome1  = input("Digite seu nome")
telefone1 = input("Digite ")

sql = "INSERT INTO alunos(nome, telefone) VALUES (%s,%s)"
data = (nome1, telefone1)
meucursor.execute(sql, data)
banco.commit()

meucursor.close()
banco.close()


