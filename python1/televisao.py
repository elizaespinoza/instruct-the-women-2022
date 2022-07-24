 #!/usr/bin/python
 # # -*- coding: utf-8 -*-

import sys

if sys.version_info[0] < 3:
    raise Exception("This script must run in Python 3.9.10.")

class Televisao:
    """Classe que modela ao objeto Televisao."""

    def __init__(self):
        self.ligada = False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        """Liga a televisao, devolvendo True para o atributo ligada."""
        self.ligada = True
        print("Televisão ligada")

    def desligar(self):
        """Desliga a televisao, devolvendo Fase para o atributo ligada."""
        self.ligada = False
        print("Televisão desligada")

    def mudar_canal_para_cima(self):
        """Muda um canal para cima, respeitando o limite de 1 a 99 canais."""
        if self.ligada:
            if self.canal >= self.canal_min and self.canal <= self.canal_max:
                self.canal += 1
                print("Canal mudado para {}".format(self.canal))
            else:
                print("Canal inválido")
        else:
            print("Televisão desligada")

    def mudar_canal_para_baixo(self):
        """Muda um canal para baixo, respeitando o limite de 1 a 99 canais."""
        if self.ligada:
            if self.canal >= self.canal_min and self.canal <= self.canal_max:
                self.canal -= 1
                print("Canal mudado para {}".format(self.canal))
            else:
                print("Canal inválido")
        else:
            print("Televisão desligada")

    def aumentar_volume(self):
        """Aumenta o volume em 10 decibels, respeitando o limite de 0 a 100 decibels."""
        if self.ligada:
            if self.volume >= self.volume_min and self.volume <= self.volume_max:
                self.volume += 10
                print("Volume aumentado para {}".format(self.volume))
            else:
                print("Volume inválido")
        else:
            print("Televisão desligada")

    def reduzir_volume(self):
        """Diminui o volume em 10 decibels, respeitando o limite de 0 a 100 decibels."""
        if self.ligada:
            if self.volume >= self.volume_min and self.volume <= self.volume_max:
                self.volume -= 10
                print("Volume reduzido para {}".format(self.volume))
            else:
                print("Volume inválido")
        else:
            print("Televisão desligada")

    def __str__(self) -> str:
        return f"Televisão: - ligada {self.ligada} - canal {self.canal} - volume {self.volume}"


"""
Criando instancias da classe Televisao
"""
tv_sala = Televisao()
tv_quarto = Televisao()

tv_sala.ligar()
print(f"tv_sala está ligada? {tv_sala.ligada}")
print(f"tv_quarto está ligada? {tv_quarto.ligada}")

for _ in range(3):
    tv_sala.aumentar_volume()

print(f"tv_sala volume: {v_sala.volume}")
print(f"tv_quarto volume: {tv_quarto.volume}")

"""
Imprimir o conteúdo do objeto
"""
print("tv_sala", tv_sala)
print("tv_quarto", tv_quarto)
