# Mentoria Instruct the Women 2022

Anotações das aulas da mentoria de python backend da [WoMakersCode](https://womakerscode.org/instruct) com a [Instruct](https://github.com/instruct-br).

## 🧙 Indice

- [Mentoria Instruct the Women 2022](#mentoria-instruct-the-women-2022)
  - [🧙 Indice](#-indice)
  - [A1 - Introdução a OOP](#a1---introdução-a-oop)
    - [1. VS Code](#1-vs-code)
    - [2. OOP](#2-oop)
    - [3. Próximos passos](#3-próximos-passos)
      - [1. Objetos](#1-objetos)
      - [2. Classes](#2-classes)
    - [3. 🎯 Challenge #1](#3--challenge-1)
  - [📃 Licença](#-licença)
  - [🙇‍♀️ Obrigada](#️-obrigada)

## A1 - Introdução a OOP

Anotações das aulas da mentoria de python backend da [WoMakersCode](https://womakerscode.org/instruct) com a [Instruct](https://github.com/instruct-br).

### 1. VS Code

- O [Coding Pack for Python](https://code.visualstudio.com/docs/python/coding-pack-python) ajuda a configurar rapidamente um ambiente de codificação Python com o Visual Studio Code.
    > Ele ajuda você a instalar um interpretador Python, o VS Code, as extensões que fornecem suporte para Python no VS Code e vários pacotes Python comuns e úteis.
- O [*Visual Studio Code Tips and Tricks*](https://code.visualstudio.com/docs/getstarted/tips-and-tricks?WT.mc_id=devto-blog-gllemos), parte da documentação oficial do VS Code.
- Curso gratuito de [*Dicas e Truques com Visual Studio Code*](https://maismulheres.tech/courses/enrolled/1345414) da #MaisMulheresTech, criada pela WoMakersCode.
- Tutorial [*Advanced Visual Studio Code for Python Developers*](https://realpython.com/advanced-visual-studio-code-python/#setting-up-pylance) do Real Python.
- Projeto para experimentar a extensão [VS Code Remote - Containers](https://github.com/microsoft/vscode-remote-try-python).
    > *Obs: Vai precisar de instalar Docker.*
- Se você é estudante de ensino superior, parabéns! Você tem acceso ao GitHub Pro, acesse pelo [GitHub Student Developer Pack](https://education.github.com/pack) e ao [GitHub Copilot](https://www.youtube.com/watch?v=EGiXsfyBST8)!
    > O Copilot é uma IA que traz varias suggestões para o teu código. *Psst: O GitHub Copilot está disponível para o VS Code.*

### 2. OOP

- Programas são coleções de objetos que interagem entre si.
- A lógica é embutida nos objetos do programa.

> Leitura recomendada: [*O que é Programação Orientada a Objetos*](https://algoritmosempython.com.br/cursos/programacao-python/classes-objetos/) do blog 'Algoritmos em Python'.

### 3. Próximos passos

Na próxima aula iremos revisar os conceitos:

- Herança: estender a funcionalidade de classes existentes.
- Encapsulamento: esconder certos tipos de informação da classe.
- Polimorfismo: criar classes com uma interface unificada.

#### 1. Objetos

- Representações do mundo real.
- Possui dos componentes:
    1. Propiedades: **atributos**
    2. Comportamentos: **métodos**
- Instâncias de uma classe.

#### 2. Classes

- Definidas com `Class <NomeDaClasse>`.
- Podemos ter várias instâncias dentro dela.
- Uma instância pode ser uma concretização da classe.
- Toda classe tem um construtor def `__init__(self)`.
- O `self` indica que a instância dessa classe está sendo considerada.
- O codigo OOP tem dados de entrada o processamento e dados de saída.

### 3. 🎯 Challenge #1

Modelando um estacionamento:

1. Estabelecer os atores: estacionamento, vaga, carro, moto.
2. Identificando as propiedades deles:
    - Estacionamento: vagas totais (carro, moto), vagas livres (carro, moto)
    - Vagas: livre ou não, tipo, id. Ações: ocupar, desocupar
    - Carro: placa
    - Moto: placa

> *Veja o resultado no arquivo 📁[carro.py](https://github.com/elizaespinoza/instruct-the-women-2022/blob/master/python1/carro.py).*

## 📃 Licença

Este projeto é disponibilizado com a licença MIT. Revise o arquivo [LICENSE](https://github.com/elizaespinoza/instruct-the-women-2022/blob/master/license) para ver os direitos e as limitações da licença.

## 🙇‍♀️ Obrigada

- [WoMakersCode](https://womakerscode.org/instruct)
- [Instruct](https://github.com/instruct-br)
- [Isadora Ferrão](https://www.linkedin.com/in/isadora-ferrao/)
