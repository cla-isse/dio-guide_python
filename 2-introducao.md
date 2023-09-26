# ![PYTHON](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
Olá, pessoa bonita! Tudo bem com você? 

Este é um resumo construído com base no curso "Introdução à Ciência de Dados e Python", na plataforma [DIO](https://web.dio.me/home).

Mentor: [@guicarvalho](https://github.com/guicarvalho)

## Sumário

[Página Inicial](./README.md)

[1. Ambiente de desenvolvimeto e Primeiros Passos com Python](./1-primeiros_passos.md)

[2. Conhecendo a Linguagem de Programação Python](./2-introducao.md#2-conhecendo-a-linguagem-de-programação-python) <-
* [2.1 Tipos de Dados](#21-tipos-de-dados)
* [2.2 Modo Interativo](#22-modo-interativo)
* [2.3 Variáveis e Constantes](#23-variáveis-e-constantes)
* [2.4 Conversão de Tipos](#24-conversão-de-tipos)
* [2.5 Funções de Entrada e Saída](#25-funções-de-entrada-e-saída)

[3. Tipos de Operadores](./3-operadores.md)

[4. Estruturas Condicionais e de Repetição](./4-condicao_e_repeticao.md)

[5. Strings](./5-strings.md)

[6. Listas e Tuplas](./6-listas_e_tuplas.md)

[7. Conjuntos](./7-conjuntos.md)

[8. Dicionários](./8-dicionarios.md)

[9. Funções](./9-funcoes.md)

[Bônus: Desafios de Código](./challenges/)

---


## ![PYTHON](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

### 2. Conhecendo a Linguagem de Programação Python

#### 2.1 Tipos de Dados

Tipos servem para denifir as caracerísticas e comportamentos de um objeto para o interpretador.

Os tipos built-in mais comuns são:

|Tipo|Classe|
|---|---|
|Texto|str|
|Numérico|int, float, complex|
|Sequência|list, tuple, range|
|Mapa|dict|
|Coleção|set, frozenset|
|Booleano|bool|
|Binário|bytes, bytearray, memoryview|

> Mapa = chave:valor ->  nome:guilherme

#### Tipos Numéricos

##### Números Inteiros

São representados pela classe **int** e possuem precisão ilimitada.
>Ex. 1, 10, 100

##### Números de ponto flutuante

São usados para representar os números racionais e sua implementação é feita pela classe **float**.
> Ex. 1.5, -10.435, 0.75

#### Tipo Booleano

É usado para representar valores de verdadeiro ou falso, e é impementado pela classe **bool**. 
* Em Python, é uma subclasse de **int**, uma vez que qualquer número diferente de 0 representa **verdadeiro** e 0 representa **falso**.

> Ex. True e False

#### Tipo Texto

Strings, ou cadeia de caracteres, são usadas para representar valores alfanuméricos. Em Python, são definidas pela classe **str**.

> Ex. "Python", 'Python', """Python""", 'p'

#### 2.2 Modo Interativo

No VSCode Studio, é possível ativar o modo interativo do interpretador Python no terminal.

Basta escrever:
```python
python
```

ou executando o script com a flag -i:
```python
python -i nome-do-arquivo.py
```
Para sair do modo interatitvo:
```python
exit()
```

Dessa forma, é possível executar comandos (como operaões numéricas, por exemplo) sem a necessidade de escrever e executar um script.

##### dir()

A função **dir**, sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válido para o objeto.

```python
dir()
```

##### help()

A função **help** invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável.

```python
help()
```
#### 2.3 Variáveis e Constantes

##### Variáveis

**Varáveis** são valores (objetos) que podem sofrer variações ao longo da execução de um programa.

Não é preciso declarar o tipo de dados da variável, o Python reconhece automaticamente.

Dessa forma, nãoé possível declarar uma variável sem um valor atribuído.

* Para alterar o valor de uma variável, basta fazer a tribuição de um novo valor.

```python
name = 'Gui'
age = 23
# ou name, age = ('Gui', 23)

print(f'Meu nome é {name} e eu tenho {age} anos de idade.')
>>> Meu nome é Gui e eu tenho 23 anos de idade
```

##### Constantes

**Constantes** são valores (objetos) que **NÃO** podem sofrer variações ao longo da execução de um programa. O valor é imutável.

Contudo, não existe uma palavra reservada, em Python, para informar ao interpretador que o valor é constante.

Em Python, usamos a **convenção** que diz ao **programador** que determinado valor é uma constante. Para fazer isso, o valor deve ser declarado com todas as letras maíusculas.

```python
ABS_PATH = '/home/gui/Documents/python_course/'

STATES = [
  'SP',
  'RJ',
  'MG',
]

AMOUNT = 30.2
```

##### Boas Práticas

* O padrão de nomes deve ser **snake_case**;
* Nomes devem ser intuitivos e sugestivos;
* Nome de constantes todo em maíusculo.

#### 2.4 Conversão de Tipos

Pode ser necessário converter o tipo de uma variável para que seja manipulada de forma diferente. 

>Ex. Uma variável string que armazena um número que passará por alguma operação matemática.

##### int para float
```python
preco = 10
print(preco)
>>> 10

preco = float(preco)
print(preco)
>>> 10.0

# Para voltar de float para int:
preco = int(preco)
print(preco)
>>> 10
```

##### numérico para string
```python
preco = 10.50
idade = 23

print(str(preco))
>>> 10.5

# ou

texto = f"idade {idade} preco {preco}"
print(texto)
>>> idade 28 preco 10.5
```

##### string para numérico

```python
preco = "10.50"
idade = "28"

print(float(preco))
>>> 10.50

print(int(idade))
>>> 28
```
#### 2.5 Funções de entrada e saída

input -> output

##### Função input()

A função built-in **input()** é utilizada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). 

A função lê a entrada, converte para string e retorna o valor.

```python
nome = input("Informe seu nome: ")
>>> Informe o seu nome: |
```

##### Função print()

A função built-in **print()** é utilizada quando queremos exibir dados na saída padrão (tela). 

Ela recebe um argumento onrigatório, do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). 

Todos os objetos são convertidos para string, separados por *sep* e terminados por *end*. A string final é exibida para o usuário.

```python
nome = "Janaina"
sobrenome = "Souza"

print(nome, sobrenome)
>>> Jananina Souza

pritn(nome, sobrenome, sep="-" end="...\n")
>>> Janaina-Souza...
```
---
Feito por [cla-isse](https://github.com/cla-isse) 💜