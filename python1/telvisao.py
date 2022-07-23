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
                print("Volume aumentado para {}".format(volume))
            else:
                print("Volume inválido")
        else:
            print("Televisão desligada")
    
    def reduzir_volume(self):
        if self.ligada:
            if self.volume >= self.volume_min and self.volume <= self.volume_max:
                self.volume -= 10
                print("Volume reduzido para {}".format(volume))
            else:
                print("Volume inválido")
        else:
            print("Televisão desligada")

    def __str__(self) --> str:
        return f"Televisão: - ligada {self.ligada} - canal {self.canal} - volume {self.volume}"
