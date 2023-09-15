import pytest
from ..funcoes import *

@pytest.mark.usuarios
def test_idade_invalida():
    assert cadastra_usuario('Mario',0, '01234567890','Rua Quata', 'email@gmail.com') == False

# def test_idade_valida():
    # assert cadastra_usuario('Mario',10, '01234567890','Rua Quata', 'email@gmail.com') == False

@pytest.mark.usuarios
def test_cpf_invalido():
    assert cadastra_usuario('Mario',10, '69','Rua quata', 'email@gmail.com') == False

@pytest.mark.usuarios
def test_email_string_antes():
    assert cadastra_usuario('Mario',10, '01234567890','Rua Quata', 'email@') == False

@pytest.mark.usuarios
def test_email_string_antes():
    assert cadastra_usuario('Mario',10, '01234567890','Rua Quata', '@gmail.com') == False

