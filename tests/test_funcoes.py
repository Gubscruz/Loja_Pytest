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

@pytest.mark.usuarios
def test_cadastro_idade_str():
    assert cadastra_usuario('Mario','5','01234567890','Rua Quata','email@gmail.com') == False


# acha usuario
@pytest.mark.usuarios
def test_id_out_of_range():
    assert encontra_usuario(100) == False

@pytest.mark.usuarios
def test_id_negativo():
    assert encontra_usuario(-3) == False

@pytest.mark.usuarios
def test_encontra_id():
    assert encontra_usuario(2) == 200


# lista todos usuarios
@pytest.mark.usuarios
def test_lista_todos_usuarios():
    assert lista_usuarios() == 200


# atualiza usuarios
@pytest.mark.usuarios
def test_atualiza_dados_usuario():
    assert atualiza_usuario('Mario',10,'01234567890','Rua Quata','email@gmail.com',2) == 201

@pytest.mark.usuarios
def test_atualiza_idade_invalida():
    assert atualiza_usuario('Mario',-1,'01234567890','Rua Quata','email@gmail.com',2) == False

@pytest.mark.usuarios
def test_atualiza_cpf_invalido():
    assert atualiza_usuario('Mario',10,'69','Rua Quata','email@gmail.com',2) == False

@pytest.mark.usuarios
def test_atualiza_email_string_antes():
    assert atualiza_usuario('Mario',10,'01234567890','Rua Quata','email@',2) == False

@pytest.mark.usuarios
def test_atualiza_email_string_depois():
    assert atualiza_usuario('Mario',10,'01234567890','Rua Quata','@gmail.com',2) == False

@pytest.mark.usuarios
def test_atualiza_cadastro_valido():
    assert atualiza_usuario('Mario',10,'01234567890','Rua Quata','email@gmail.com',2) == 201

@pytest.mark.usuarios
def test_deleta_usuario():
    assert deleta_usuario(1) == 200



@pytest.mark.produtos
def test_preco_negativo():
    assert cadastra_produto('Apple M1','Processador com arquitetura ARM-64x','Eletrônicos',-10,8) == False

@pytest.mark.produtos
def test_estoque_negativo():
    assert cadastra_produto('Apple M1','Processador com arquitetura ARM-64x','Eletrônicos',4200,-10) == False

@pytest.mark.produtos
def test_categoria_inexistente():
    assert cadastra_produto('Apple M1','Processador com arquitetura ARM-64x','Macaco',4200,8) == False

@pytest.mark.produtos
def test_lista_produtos():
    assert cadastra_produto('Apple M1','Processador com arquitetura ARM-64x','Eletrônicos',4200,8) == 200

@pytest.mark.produtos
def test_encontra_produto():
    assert encontra_produto(1) == 200

@pytest.mark.produtos
def test_encontra_produto_id_negativo():
    assert encontra_produto(-1) == False

@pytest.mark.produtos
def test_encontra_produto_id_out_of_range():
    assert encontra_produto(100) == False

@pytest.mark.produtos
def test_atualiza_produto():
    assert atualiza_produto('Apple M1','Processador com arquitetura ARM-64x','Eletrônicos',4200,8,1) == 200

@pytest.mark.produtos
def test_atualiza_produto_preco_negativo():
    assert atualiza_produto('Apple M1','Processador com arquitetura ARM-64x','Eletrônicos',-4200,8,1) == False

@pytest.mark.produtos
def test_atualiza_produto_estoque_negativo():
    assert atualiza_produto('Apple M1','Processador com arquitetura ARM-64x','Eletrônicos',4200,-8,1) == False

@pytest.mark.produtos
def test_atualiza_produto_categoria_inexistente():
    assert atualiza_produto('Apple M1','Processador com arquitetura ARM-64x','Macaco',4200,8,1) == False

@pytest.mark.produtos
def test_atualiza_produto_id_negativo():
    assert atualiza_produto('Apple M1','Processador com arquitetura ARM-64x','Eletrônicos',4200,8,-1) == False

@pytest.mark.produtos
def test_delete_produto():
    assert deleta_produto(1) == 200

@pytest.mark.produtos
def test_delete_produto_id_negativo():
    assert deleta_produto(-1) == False