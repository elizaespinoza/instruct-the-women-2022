class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = "branco"
        self.modelo = "Fusca"
        self.velocidade = 0
    
    def ligar(self):
        self.ligado = True
        print("Carro ligado")
    
    def desligar(self):
        self.ligado = False
        print("Carro desligado")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print("Carro acelerando para {}".format(self.velocidade))
        else:
            print("Carro desligado")
    
    def desacelerar(self):
        if self.ligado:
            self.velocidade -= 10
            print("Carro desacelerando para {}".format(self.velocidade))
        else:
            print("Carro desligado")

    def __str__(self) -> str:
        return f"Carro: - ligado {self.ligado} - cor {self.cor} - modelo {self.modelo} - velocidade {self.velocidade}"
    
'''
Criando instancias da classe Carro
'''

carro_eliza = Carro()

carro_eliza.ligar()
carro_eliza.acelerar()
print('carro_eliza andando: {}'.format(carro_eliza))

carro_eliza.desacelerar()
carro_eliza.desligar()
print('carro_eliza parou: {}'.format(carro_eliza))
    
    