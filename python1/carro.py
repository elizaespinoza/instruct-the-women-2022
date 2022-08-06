#!/usr/bin/python
# # -*- coding: utf-8 -*-

import sys

if sys.version_info[0] < 3:
    raise Exception("This script must run in Python 3.9.10.")

"""
Challenge 1
- Crie uma classe que modele o objeto Carro
- Um carro deve ter os seguintes atributos: ligado, cor, modelo, velocidade
- Um carros deve ter os seguintes comportamentos: ligar/desligar, acelerar/frear
- Crie uma intância da classe carro
- Faça o carro andar utilizando os metodos da classe
- Faça o carro parar utilizando os metodos da classe
"""


class Carro:
    """Classe que modela ao objeto Carro."""

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
            print(f"Carro acelerando para {self.velocidade} km/h")
        else:
            print("Carro desligado")

    def desacelerar(self):
        if self.ligado:
            self.velocidade -= 10
            print(f"Carro desacelerando para {self.velocidade} km/h")
        else:
            print("Carro desligado")

    def __str__(self) -> str:
        return f"Carro: - ligado {self.ligado} - cor {self.cor} - modelo {self.modelo} - velocidade {self.velocidade} km/h"


"""
Criando instancias da classe Carro
"""
carro_eliza = Carro()

carro_eliza.ligar()
carro_eliza.acelerar()
print(f"carro_eliza andando: {carro_eliza}")

carro_eliza.desacelerar()
carro_eliza.desligar()
print(f"carro_eliza parou: {carro_eliza}")
