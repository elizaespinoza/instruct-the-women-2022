'''
Hola mundo
- Printando nome e idade
'''
nome = input('Digite seu nome: ')
print('Benvinda, {}!'.format(nome))
idade = input('Digite sua idade: ')
print('Você tem {} anos.'.format(idade))

'''
Printando na tela
- É possível printar vários valores em uma única linha
'''
x = 3.0
y = 2
print('Divisão: x = {}'.format(x/y))

'''
# Pilha
- O último a entrar é o primeiro a sair
'''
pilha = [1, 1, 2, 3, 5, 13] #13 é o último a entrar
pilha.pop() #é o primeiro a sair

'''
# Fila
- O primeiro a entrar é o primeiro a sair
'''
fila = [1, 1, 2, 3, 5]
fila.pop(0) #primeiro a sair

'''
## Tupla
- Inmutável
'''
coordenadaA = (4, 6)
coordenadaB = (5, 7)
print('distancia entre A e B: {}'.format(abs(coordenadaA[0]-coordenadaB[0])+abs(coordenadaA[1]-coordenadaB[1])))

'''
# Listas
- Mutáveis
'''
cachorros = ['Fido', 'Rex', 'Bobby']
print(cachorros[:2])
print(cachorros[1:])
print(cachorros[::-1])

nome_removido = cachorros.pop(2)
print(cachorros)
print(nome_removido)
