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

def test_pessoa_idade_negativa():
    with pytest.raises(ValueError, match="A idade não pode ser negativa."):
        Pessoa("Maiara", -33, Sexo.FEMININO)

def test_pessoa_idade_maior_que_130():
    with pytest.raises(ValueError, match="Idade não pode ultrapassar o limite"):
        Pessoa("Maiara", 130, Sexo.FEMININO)

def test_pessoa_idade_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A idade deve ser um número inteiro"):
        Pessoa("Maiara", "33", Sexo.FEMININO)

def test_pessoa_nome_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texto"):
        Pessoa(222, 333, Sexo.FEMININO)

def test_pessoa_nome_vazio_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não pode estar vazio"):
        Pessoa("", 333, Sexo.FEMININO)