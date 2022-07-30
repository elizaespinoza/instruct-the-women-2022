# Getter = retornar o valor
# Setter = definir ou atualizar

class Quadrado:

    def __init__(self, medida):
        self.altura = medida
        self.largura = medida

    # pegar o valor da largura (o comportamento)
    @property
    def altura(self):
        print('Getter de altura')
        return self.__medida

    @altura.setter
    def altura(self, valor):
        print('Setter de altura')

        if valor < 0:
            raise ValueError()
        self.__medida = valor

    @property
    def largura(self):
        print('Getter da largura')
        return self.__medida

    @largura.setter
    def largura(self, valor):
        print('Setter de largura')
        if valor < 0:
            raise ValueError()
        self.__medida = valor

    def area(self):
        return self.largura * self.altura


quadrado = Quadrado(2)
print(quadrado.area())
quadrado.altura = 3
print(quadrado.area())
quadrado.largura = 2
print(quadrado.area())
