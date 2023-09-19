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