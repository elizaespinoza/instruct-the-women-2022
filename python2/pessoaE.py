############ Aula 2 ###############

# encapsulando nome e identidade
class Pessoa:

    def __init__(self, nome, profissao, identidade):
        self._nome = nome
        self.profissao = profissao
        self.__identidade = identidade

    def __str__(self) -> str:
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'

# Cria objeto pessoa1
pessoa1 = Pessoa('Ana', 'Programadora', '123456')

# muda a profissao
pessoa1.profissao = 'Médica'

# Privado: nao consegue mudar a identidade
pessoa1.__identidade = '26737547'

# Protegido: consegue mudar, se coloca underline muda
pessoa1._nome = 'Isa'

print(pessoa1)
