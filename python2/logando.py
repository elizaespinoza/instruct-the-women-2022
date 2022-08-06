class Logavel:

    def __init__(self):
        self.nome_da_classe = ''

    def logar(self, mensagem):
        print(f'Mensagem da classe {self.nome_da_classe}: {mensagem}')

class Conexao:

    def __init__(self):
        self.servidor = ''

    def conectar(self):
        print(f'Conectado ao banco de dados do servidor {self.servidor}')

class MySqlDatabase(Conexao, Logavel):

    def __init__(self):
        super().__init__()
        self.nome_da_classe = 'MySqlDatabase'
        self.servidor = 'elizaServer'

def framework(item):

    if isinstance(item, Conexao):
        item.conectar()
    if isinstance(item, Logavel):
        mensagem = 'Sabadou'
        item.logar(mensagem)

conexao_mysql = MySqlDatabase()
framework(conexao_mysql)
