# Aula 1: Instruct the Women 
Anotações das aulas de mentoria de python backend da @WoMakersCode com a @Instruct.

## Orientação a Objetos
- Representações do mundo real
- Possui dos componentes
    1. Propiedades
    2. Comportamentos (ações, ,mêtodos)

### Classes
- Definidas com Class <NomeDaClasse>
- Podemos ter várias instâncias dentro dela.
- Uma instância pode ser uma concretização da classe.
- Toda classe tem um construtor def `__init__(self)`
- O self indica que a instância dessa classe está sendo considerada.
- O codigo OOP tem dados de entrada o processamento e dados de saída.

#### Exemplo: Modelando um estacionamento
1. Estabelecer os atores: estacionamento, vaga, carro, moto
2. Identificando as propiedades deles:
    - estacionamento: vagas (carro, moto), vagas livres (moto, carro)
    - vagas: livre ou não, tipo, id. Acoes: ocupar, desocupar
    - carro: placa
    - moto: placa

### Heranças