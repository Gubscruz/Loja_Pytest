from flask import Flask, request
from db_utils import Sql

app = Flask('Loja')
db = Sql()

def cadastra_usuario(nome, idade, cpf, endereco, email):
    if 0<int(idade)<120:
        return False
    
    if len(cpf) != 11:
        return False
    
    pos = email.find('@')
    if email[:pos] == '' or email[pos+1:] == '':
        return False
    
    data = (nome, idade, cpf, endereco, email)
    
    return db.insert('Usuarios', ('nome','idade','cpf','endereco','email'), '?,?,?,?,?', data), 'Yes'