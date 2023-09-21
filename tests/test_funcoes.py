import pytest
from ..funcoes import *


# cadasto de usuarios
@pytest.mark.usuarios
def test_idade_invalida():
    assert cadastra_usuario('Mario',-1,'01234567890','Rua Quata','email@gmail.com') == False

@pytest.mark.usuarios
def test_cpf_invalido():
    assert cadastra_usuario('Mario',10,'69','Rua Quata','email@gmail.com') == False

@pytest.mark.usuarios
def test_email_string_antes():
    assert cadastra_usuario('Mario',10,'01234567890','Rua Quata','email@') == False

@pytest.mark.usuarios
def test_email_string_depois():
    assert cadastra_usuario('Mario',10,'01234567890','Rua Quata','@gmail.com') == False

@pytest.mark.usuarios
def test_cadastro_valido():
    assert cadastra_usuario('Mario',10,'01234567890','Rua Quata','email@gmail.com') == 201

# acha usuario
@pytest.mark.usuarios
def test_id_out_of_range():
    assert encontra_usuario(100) == False

@pytest.mark.usuarios
def test_id_negativo():
    assert encontra_usuario(-3) == False

@pytest.mark.usuarios
def test_encontra_id():
    assert encontra_usuario(2) == (2, 'Bob', 35, '23456789012', 'Rua dos Construtores, 5', 'bob@builder.com')


# lista todos usuarios
@pytest.mark.usuarios
def test_lista_todos_usuarios():
    assert lista_usuarios() == [(1, 'Alice', 28, '12345678901', 'Rua das Maravilhas, 10', 'alice@wonderland.com'), (2, 'Bob', 35, '23456789012', 'Rua dos Construtores, 5', 'bob@builder.com'), (3, 'Charlie', 40, '34567890123', 'Praça dos Chocolate, 7', 'charlie@chocolate.com'), (4, 'Diana', 29, '45678901234', 'Avenida das Caçadoras, 15', 'diana@amazon.com'), (5, 'Eduardo', 50, '56789012345', 'Beco dos Economistas, 20', 'ed@economy.com'), (6, 'Mario', 10, '01234567890', 'Rua Quata', 'email@gmail.com')]



# atualiza usuarios
@pytest.mark.usuarios
def test_atualiza_dados_usuario():
    assert atualiza_usuario('Mario',10,'01234567890','Rua Quata','email@gmail.com',2) == True
