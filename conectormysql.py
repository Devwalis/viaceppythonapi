import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database= "bd_walisson"
)
print(banco)
