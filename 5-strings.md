# ![PYTHON](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
Olá, pessoa bonita! Tudo bem com você? 

Este é um resumo construído com base no curso "Introdução à Ciência de Dados e Python", na plataforma [DIO](https://web.dio.me/home).

Mentor: [@guicarvalho](https://github.com/guicarvalho)

## Sumário

[Página Inicial](./README.md)

[1. Ambiente de desenvolvimeto e Primeiros Passos com Python](./1-primeiros_passos.md)

[2. Conhecendo a Linguagem de Programação Python](./2-introducao.md)

[3. Tipos de Operadores](./3-operadores.md)

[4. Estruturas Condicionais e de Repetição](./4-condicao_e_repeticao.md)

[5. Strings](./5-strings.md#5-strings) <-
* [5.1 Conhecendo Métodos Úteis da Classe String](#51-conhecendo-métodos-úteis-da-classe-string)
* [5.2 Interpolação de Variáveis](#52-interpolação-de-variáveis)
* [5.3 Fatiamento de String](#53-fatiamento-de-strings)
* [5.4 String de múltiplas linhas](#54-string-de-múltiplas-linhas)

[6. Listas e Tuplas](./6-listas_e_tuplas.md)

[7. Conjuntos](./7-conjuntos.md)

[8. Dicionários](./8-dicionarios.md)

[9. Funções](./9-funcoes.md)

---


## ![PYTHON](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

### 5. Strings

#### 5.1 Conhecendo Métodos Úteis da Classe String

A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.

Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

##### Maíuscula, minúscula e título

```python
curso = "pYThOn"

print(curso.upper())
>>> PYTHON

print(curso.lower())
>>> python

print(curso.title())
>>> Python
```

##### Eliminar espaços em branco

```python
curso = " Python "

print(curso.strip())
>>> "Python"

print(curso.lstrip())
>>> "Python "

print(curso.rstrip())
>>> " Python"
```

##### Junções e centralização

```python
curso = "Python"

print(curso.center(10, "#"))
>>> "##Python##"

print(".".join(curso))
>>> "P.y.t.h.o.n"
```

#### 5.2 Interpolação de Variáveis

Em Python temos 3 formas de interpolar variáveis em strings:
* Usando o sinal %;
* O método format;
* f strings.

> A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro.

##### Format

```python
nome = "Carol"
idade = "28"
profissao = "progamadora"
curso = "python"

print("Olá, eu me chamo {}. Tenho {} anos, trabalho como {} e estou aprendendo {}." .format(nome, idade, profissao, curso))

# ou 

print ("Olá, eu me chamo {1}. Tenho {0} anos, trabalho como {2} e estou aprendendo {3}." .format(idade, nome, profissao, curso))
```

##### F-String

```python
nome = "Carol"
idade = "28"
profissao = "progamadora"
curso = "python"

print(f"Olá, eu me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e estou aprendendo {curso}.")
>>> "Olá, eu me chamo Carol. Tenho 28 anos, trabalho como progamadora e estou aprendendo python."
```

Pode receber argumentos de formatação:
* caracteres totais na string;
> OBS: Considera os caracteres da string e acrescenta, em espaços vazios, o que falta para chegar ao número informado.
>
>Ex. Se o argumento for 10, e a palavra for "arroz", serão acrescidos 5 espaços em branco antes da palavra.
* digitos após a vírgula.

```python
PI = 3.14159

print(f"Pi é igual a: {PI:.2f}")
>>> "Pi é igual a: 3.14"

print(f"Pi é igual a: {PI:10.2f}")
>>> "Pi é igual a:       3.14"
```

#### 5.3 Fatiamento de Strings

Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step).

```python
nome: "Guilherme Arthur de Carvalho"

nome[0]
>>> "G"

nome[:9]
>>> "Guilherme"

nome[10:]
>>> "Arthur de Carvalho"

nome[10:16]
>>> "Arthur"

nome[10:16:2] # a partir do 10, até o 16, pulando um caractere.
>>> "Atu"

nome[:]
>>> "Guilherme Arthur de Carvalho"

nome[::-1]
>>> "ohlavraC ed ruhtrA emrehliuG"
```

#### 5.4 String de Múltiplas Linhas

Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. 
* Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final. 

```python
nome = "Guilherme"

mensagem = f"""
Olá, meu nome é {nome}.
    Estou aprendendo Python.
"""
print(mensagem)

>>> Olá, meu nome é Guiherme.
     Estou aprendendo Python.
```
---
Feito por [cla-isse](https://github.com/cla-isse) 💜