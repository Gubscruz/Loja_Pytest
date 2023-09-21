import sqlite3 as sql
import _json

conn = sql.connect('./db/e_magic_shop_v2.db')
cursor = conn.cursor()


def cadastra_usuario(nome, idade, cpf, endereco, email):

    if not isinstance(idade, int):
        return False

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
        

def encontra_usuario(id):
    cursor.execute('SELECT * FROM Usuarios')
    usuarios = cursor.fetchall()
    if id<0:
        return False
    try:
        user = usuarios[id-1]
    except:
        return False
    return user


def lista_usuarios():
    cursor.execute('SELECT * FROM Usuarios')
    usuarios = cursor.fetchall()
    return usuarios


def atualiza_usuario(nome,idade,cpf,endereco,email,id):
    cursor.execute('SELECT * FROM Usuarios WHERE id=?', (id,))
    data = (nome, idade, cpf, endereco, email, id)
    if 0>idade or 120<idade:
        return False
    
    if len(cpf) != 11:
        return False
    
    pos = email.find('@')
    if email[:pos] == '' or email[pos+1:] == '':
        return False

    elif cursor.fetchone() == None:
        return False
    cursor.execute('UPDATE Usuarios SET nome=?, idade=?, cpf=?, endereco=?, email=? WHERE id=?', data)
    return 201

