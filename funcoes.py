import sqlite3 as sql

conn = sql.connect('./db/e_magic_shop_v2.db')
cursor = conn.cursor()


def cadastra_usuario(nome, idade, cpf, endereco, email):
    if 0>idade or 120<idade:
        return False
    
    if len(cpf) != 11:
        return False
    
    pos = email.find('@')
    if email[:pos] == '' or email[pos+1:] == '':
        return False
    
    else:
        data = (nome, idade, cpf, endereco, email)
        cursor.execute(('INSERT INTO Usuarios (nome,idade,cpf,endereco,email) VALUES (?,?,?,?,?)'), data)
        return 201