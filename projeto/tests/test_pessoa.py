import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def pessoa_valida():
    # Instanciando classe Pessoa
    pessoa = Pessoa("Maiara", 33, Sexo.FEMININO)
    return pessoa

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Maiara"

def test_pessoa_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Manolo"
    assert pessoa_valida.nome == "Manolo"

def test_pessoa_idade_valido(pessoa_valida):
    assert pessoa_valida.idade == 33

def test_pessoa_idade_negativa(pessoa_valida):
    pessoa_valida.set_idade(-1)
    assert pessoa_valida.idade == 0