import pytest
from ..code import *

@pytest.mark.validacao
def test_idade_invalida():
    assert validacao_usuario(idade, cpf, email)