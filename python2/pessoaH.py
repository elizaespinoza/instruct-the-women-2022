class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._tipo = 'Pessoa'

    def falar_oi(self):
        print('Oi, meu nome é {}'.format(self._nome))

    def falar_tipo(self):
        print('Meu tipo é {}'.format(self._tipo))

pessoa = Pessoa('Maria')
pessoa.falar_oi()
pessoa.falar_tipo()

class Estudante(Pessoa):
    '''Estudante é uma pessoa'''
    def __init__(self, nome, curso):
        #chama o construtor na classe base
        super().__init__(nome)
        self._curso = curso

    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo o curso {self._curso}') #A propriedade self._nome é herdada da classe base

    def falar_tipo(self):
        self._tipo = 'Estudante'
        return super().falar_tipo()

estudante = Estudante('Yasmin', 'Introdução ao Python')

# o método "falar_oi" é herdado
estudante.falar_oi()

# o método "falar_tipo" e modifcado na classe derivada
estudante.falar_tipo()

estudante.falar_curso
