'''importar o sqlite3
'''
import sqlite3

'''criacao dp nome do banco de dados
'''
conn = sqlite3.connect("Sistema.db")

'''criacao do cursor, o cursor é uma ponte que vai conectar os codigos que serao executados no sqlite
'''
cursor = conn.cursor()

'''criacao de comandos para o sqlite --> o cursor ira criar uma tabela no banco de dados se nao existir com o nome users ou seja caso exista uma tabela com o nome users nao ira criar, caso nao exista ira cria-la'''
cursor.execute('''
CREATE TABLE IF NOT EXISTS users
(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Username TEXT  NOT NULL,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    ConfPassword TEXT NOT NULL

)''')

print("Conexão ao banco de dados feita com sucesso!")

