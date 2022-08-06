# O Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# # Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.
# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.
# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".
# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".

class Cliente:

    def __init__(self, nome, telefone, renda_mensal, sexo):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal
        self.sexo = sexo
#        self.cheque_especial = False
#        self.limite = 0
#        self.limite_cheque_especial = 0

class Conta(Cliente):

    def __init__(self, nome, telefone, renda_mensal,sexo):
        super().__init__(nome, telefone, renda_mensal,sexo)
        #self.titular = nome
        self.saldo = 0
        self.operacoes = []
        self.renda_mensal = renda_mensal
        self.cheque_especial = False
        self.limite = 0
        self.limite_cheque_especial = 0

    # lista de operações de saques e depósitos
    def extrato(self):
        print("Extrato")
        for operacao in self.operacoes:
            print(operacao[0],":",operacao[1])
        print("Saldo:",self.saldo)
        print("Limite:",self.limite if self.cheque_especial else self.limite_cheque_especial)

    def depositar(self,valor):
        self.saldo += valor
        self.operacoes.append(["Deposito",valor])

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque",valor])
        else:
            print("Saldo insuficiente")

    def transferir(self,valor,conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.operacoes.append(["Transferencia",valor])
            conta_destino.operacoes.append(["Transferencia",valor])
        else:
            print("Saldo insuficiente")

    def verificar_limite(self):
        print("Limite:",self.limite if self.cheque_especial else self.limite_cheque_especial)

    def definir_limite_por_sexo(self,valor):
        self.limite = valor if self.sexo == "M" else 0
        self.limite = self.limite_cheque_especial if self.cheque_especial else self.limite

    def __str__(self) -> str:
        return super().__str__() + "\nSaldo: " + str(self.saldo) + "\nLimite: " + str(self.limite if self.cheque_especial else self.limite_cheque_especial)

bianca = Conta("Bianca", "9999-9999", 1000, "F")
