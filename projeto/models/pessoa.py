from projeto.models.enums.sexo import Sexo

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = self._verificar_nome(nome)
        self.idade = self._verificar_idade(idade)
        self.sexo = sexo

   # def _verificar_idade(self,valor):
     # if valor >= 130:
        # raise ValueError("Idade não pode ultrapassar o limite")
        
        # if valor < 0:
        #    raise ValueError("A idade não pode ser negativa.")
                
    # self.idade = valor
    # return self.idade

    def _verificar_nome(self,valor):
        """Método para verificação de nome"""
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio_invalido(valor)

        self.nome = valor
        return self.nome

    def _verificar_idade(self,valor):
        """Método auxiliar para verificação de idade"""
        self._verificar_idade_tipo_invalido(valor)
        self._verificar_idade_negativa(valor)
        self._verificar_idade_acima_130(valor)

        self.idade = valor
        return self.idade

    def _verificar_idade_tipo_invalido(self,valor):
        """Método auxiliar para verificação de tipo para idade"""
        if not isinstance(valor, int):
            raise TypeError("A idade deve ser um número inteiro")

    def _verificar_idade_negativa(self,valor):
        """Método auxiliar para verificação de idade negativa"""
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        
    def _verificar_idade_acima_130(self,valor):
        """Método auxiliar para verificação da idade limite"""
        if valor >= 130:
            raise ValueError("Idade não pode ultrapassar o limite")
        
    def _verificar_nome_tipo_invalido(self,valor):
        """Método auxiliar para verificação de tipo para nome"""
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto")
        
    def _verificar_nome_vazio_invalido(self,valor):
        """Método auxiliar para verificação de nome inexistente"""
        # strip() Verifica se o nome está vazio ou contém apenas espaços.
        if not valor.strip():
            raise TypeError("O nome não pode estar vazio")