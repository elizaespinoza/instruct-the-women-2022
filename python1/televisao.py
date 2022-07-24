class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        self.ligada = True
        print("Televisão ligada")

    def desligar(self):
        self.ligada = False
        print("Televisão desligada")

    def mudar_canal_para_cima(self, canal):
        if self.ligada:
            if canal >= self.canal_min and canal <= self.canal_max:
                self.canal += 1
                print("Canal mudado para {}".format(canal))
            else:
                print("Canal inválido")
        else:
            print("Televisão desligada")

    def mudar_canal_para_baixo(self, canal):
        if self.ligada:
            if canal >= self.canal_min and canal <= self.canal_max:
                self.canal -= 1
                print("Canal mudado para {}".format(canal))
            else:
                print("Canal inválido")
        else:
            print("Televisão desligada")

    def aumentar_volume(self):
        if self.ligada:
            if self.volume >= self.volume_min and self.volume <= self.volume_max:
                self.volume += 10
                print("Volume aumentado para {}".format(self.volume))
            else:
                print("Volume inválido")
        else:
            print("Televisão desligada")

    def reduzir_volume(self):
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


'''
Criando instancias da classe Televisao
'''
tv_sala = Televisao()
tv_quarto = Televisao()

tv_sala.ligar()
print('tv_sala está ligada? {}'.format(tv_sala.ligada))
print('tv_quarto está ligada? {}'.format(tv_quarto.ligada))

for _ in range(3):
    tv_sala.aumentar_volume()

print('tv_sala volume: {}'.format(tv_sala.volume))
print('tv_quarto volume: {}'.format(tv_quarto.volume))

'''
Imprimir o conteúdo do objeto
'''
print('tv_sala',tv_sala)
print('tv_quarto',tv_quarto)
