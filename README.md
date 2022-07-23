# Aula 1: Instruct the Women 
Anotações das aulas da mentoria de python backend da @WoMakersCode com a @Instruct.

## 🛸 Instalando e configurando o VS Code:
- O [Coding Pack for Python](https://code.visualstudio.com/docs/python/coding-pack-python) ajuda a configurar rapidamente um ambiente de codificação Python com o Visual Studio Code. 
    > Ele ajuda você a instalar um interpretador Python, O Visual Studio Code, as extensões que fornecem suporte para Python no Visual Studio Code e vários pacotes Python comuns e úteis.
- O [*Visual Studio Code Tips and Tricks*](https://code.visualstudio.com/docs/getstarted/tips-and-tricks?WT.mc_id=devto-blog-gllemos), parte da documentação oficial do VS Code.
- Curso gratuito de [*Dicas e Truques com Visual Studio Code*](https://maismulheres.tech/courses/enrolled/1345414) da #MaisMulheresTech, criada pela WoMakersCode.
- Tutorial [*Advanced Visual Studio Code for Python Developers*](https://realpython.com/advanced-visual-studio-code-python/#setting-up-pylance) do Real Python.
- Projeto para experimentar a extensão [VS Code Remote - Containers](https://github.com/microsoft/vscode-remote-try-python) .
    > *Obs: Vai precisar de instalar Docker.*
- Se você é estudante de ensino superior, parabéns! Você tem acceso ao GitHub Pro, acesse pelo [GitHub Student Developer Pack](https://education.github.com/pack) e ao [GitHub Copilot](https://www.youtube.com/watch?v=EGiXsfyBST8)! 
    > O Copilot é uma IA que traz varias suggestões para o teu código. *Psst: O GitHub Copilot está disponível para o VS Code.*

## 🤹 Orientação a Objetos
- Representações do mundo real
- Possui dos componentes
    1. Propiedades
    2. Comportamentos (ações, ,mêtodos)
> Leitura recomendada: [*O que é Programação Orientada a Objetos*](https://algoritmosempython.com.br/cursos/programacao-python/classes-objetos/) do blog 'Algoritmos em Python'.

### Classes
- Definidas com Class <NomeDaClasse>
- Podemos ter várias instâncias dentro dela.
- Uma instância pode ser uma concretização da classe.
- Toda classe tem um construtor def `__init__(self)`
- O self indica que a instância dessa classe está sendo considerada.
- O codigo OOP tem dados de entrada o processamento e dados de saída.

#### 🎯 Exercício: Modelando um estacionamento
1. Estabelecer os atores: estacionamento, vaga, carro, moto
2. Identificando as propiedades deles:
    - estacionamento: vagas (carro, moto), vagas livres (moto, carro)
    - vagas: livre ou não, tipo, id. Acoes: ocupar, desocupar
    - carro: placa
    - moto: placa
> 📁 Meu resultado é o [carro.py](https://github.com/elizaespinoza/instruct-the-women-2022/blob/master/python1/carro.py)

## 📃 Licença
Este projeto é disponibilizado com a licença MIT. Revise o arquivo [LICENSE](https://github.com/elizaespinoza/instruct-the-women-2022/blob/master/license) para ver os direitos e as limitações da licença.

## 🙇‍♀️ Obrigada!
- [WoMakersCode](https://womakerscode.org/instruct)
- [Instruct](https://github.com/instruct-br)
- [Isadora Ferrão](https://www.linkedin.com/in/isadora-ferrao/)