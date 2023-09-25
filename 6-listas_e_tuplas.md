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

[5. Strings](./5-strings.md)

[6. Listas e Tuplas](./6-listas_e_tuplas.md#6-listas-e-tuplas) <-
* [6.1 Criação de Listas e Acesso aos Dados](#61-criação-e-acesso-aos-dados)
* [6.2 Métodos da Classe list](#62-métodos-da-classe-list)

[7. Conjuntos](./7-conjuntos.md)

[8. Dicionários](./8-dicionarios.md)

[9. Funções](./9-funcoes.md)

---

## ![PYTHON](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

### 6. Listas e Tuplas

#### 6.1 Criação e Acesso aos Dados

**Listas**, em Python, podem armazenar, de maneira sequencial,
qualquer tipo de objeto.

Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

> Quase todos os métodos aplicados a listas, também podem ser utilizados em tuplas.
>
> A principal diferença entre os dois está no fato de que a tupla é imutável. Assim, os métodos que alteram valores na lista não funcionam na tupla. >
>
> Além disso, a forma como os dados são declarados é diferente.

Podemos criar **listas** utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes:

```python
letras = list("python")

numeros = list(range(10))

frutas = ["laranja", "maca", "uva"]
```

> OBS: Uma lista pode ser declarada sem valores.

**Tuplas** são criadas a patir da classe **tuple**, ou colocando valores separados por vírula de parênteses.

```python
frutas = ("laranja", "pera", "uva",)

pais = ("Brasil",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])
```

> OBS: É uma boa prática colocar uma vírgula ao fim dos elementos declarados, para que o Python não confunda a tupla com precedência em operações.

A lista é uma sequência, portanto podemos acessar seus dados utilizando índices 
* Contamos o índice de determinada sequência a partir do zero.

```python
frutas = ["maçã", "laranja", "uva", "pêra"]
frutas[0] 
# maçã
frutas[2] 
# uva
```

Sequências também suportam indexação negativa, e a contagem começa em 1:

```python
frutas = ["maçã", "laranja", "uva", "pêra"]
frutas[-4] 
# maçã
frutas[-2] 
# uva
```

Tupla: ✔

##### Listas Aninhadas

Listas podem armazenar todos os tipos de objetos Python,
portanto podemos ter listas que armazenam outras listas.
Com isso, surgem estruturas bidimensionais, que podem ser
acessadas informando os índices de linha e coluna.

```python
matriz = [
  [1, "a", 2],
  ["b", 3, 4],
  [6, 5, "c"]
]

# Para acessar os itens da matriz

matriz[0] 
# [1, "a", 2]
matriz[0][-1] 
# 2
```

Tupla: ✔

##### Fatiamento de Listas

Além de acessar elementos diretamente, podemos extrair um
conjunto de valores de uma sequência.

Para isso basta passar o índice inicial e/ou final para acessar o conjunto.

Podemos, ainda, informar quantas posições o cursor deve "pular" no acesso.

```python
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] 
# ["t", "h", "o", "n"]
lista[0:3:2] 
# ["p", "t"]
lista[::-1] 
# ["n", "o", "h", "t", "y", "p"]
```

> LEMBRETE: O útlimo valor não é retornado.

Tupla: ✔

##### Iterar Listas

A forma mais comum para percorrer os dados de uma lista é utilizando o comando **for**.

```python
carros = ["gol", "celta", "palio"]

for carro in carros:
  print(carro)
```

Tupla: ✔

##### Função Enumerate

Às vezes é necessário saber qual o índice do objeto dentro do laço for Para isso podemos usar a função enumerate.

```python
carros = ["gol", "celta", "palio"]

for incdice, carro in enumerate(carros):
  print(f"{indice}: {carro}")
```

Tupla: ✔

##### Compreensão de Listas

A compreensão de lista oferece uma sintaxe mais curta
ao criar uma nova lista com base nos valores
de uma lista existente, ou aplicando alguma modificação nos elementos de uma lista existente.

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
  if numero % 2 == 0:
    pares.append(numero)

# ou

pares = [numero for numero in numeros if numero % 2 == 0]
```
Tupla: ⚠ 
> Funciona, mas a classe a receber os elementos (no caso, **pares**) deve ser uma lista, e não uma tupla.

#### 6.2 Métodos da classe list

##### append()

Tupla: ❌

Adiciona elementos à lista.

```python
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
>>> [1, "Python", [40, 30, 20]]
```

##### clear()

Tupla: ❌

Limpa todos os elementos da lista.

```python
lista = [1, Python, [40, 30, 20]]

lista.clear()

print(lista)
>>> 
```

##### copy()

Tupla: ❌

Retorna uma lista diferente com os mesmos elementos da original. Ou seja, cria uma segunda lista com um **id** diferente.

```python
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)
>>> [1, "Python", [40, 30, 20]]
```

##### count()

Tupla: ✔

Conta o número de vezes que um elemento aparece na lista.

```python
cores = [" vermelho", " azul", " verde", "azul"]

cores.count(" vermelho") 
# 1
cores.count(" azul") 
# 2
cores.count(" verde") 
# 1
```

##### extend()

Tupla: ❌

Utilizado para juntar duas listas diferentes.

> Inclusive elementos repetidos.

```python
linguagens = [" python", " js", "c"]

print(linguagens) 
>>> ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) 
>>> ["python", "js", "c", "java", "csharp"]
```

##### index()

Tupla: ✔

Retorna o índice da primeira ocorrência do objeto.

```python
linguagens = ["python", " js", " c", " java", "csharp"]

linguagens.index("java") 
# 3
linguagens.index("python") 
# 0
```

##### pop()

Tupla: ❌

Retira da lista o último elemento, a menos que o índice seja passado entre os parênteses.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop() 
# csharp
linguagens.pop() 
# java
linguagens.pop() 
# c
linguagens.pop(0) 
# python

print(linguagens)
>>> "js"
```

##### remove()

Tupla: ❌

```python
linguagens = [" python", " js", " c", " java", "csharp"]

linguagens.remove("c")

print(linguagens) 
>>> ["python", "js", "java", "csharp"]
```

##### reverse()

Tupla: ❌

```python
linguagens = ["python", " js", " c", " java", "csharp"]

linguagens.reverse()

print(linguagens) 
>>> ["csharp", "java", "c", "js", "python"]
```

##### sort()

Tupla: ❌

```python
linguagens = ["python", " js", "c", " java", "csharp"]

linguagens.sort() 
>>> ["c", "csharp", "java", "js", "python"]

linguagens.sort(reverse=True)
>>> ["python", "js", "java", "csharp", "c"]

# Ordenação crescente por tamanho das palavras
linguagens.sort(key= lambda x: len(x)) 
>>> ["c", "js", "java", "python", "csharp"]

# Ordenação decrescente por tamanho das palavras
linguagens.sort(key= lambda x: len(x), reverse= True ) 
>>> ["python", "csharp", "java", "js", "c"]
```

##### len()

Tupla: ✔

Retorna o tamanho da lista.

```python
linguagens = ["python", " js", "c", " java", "csharp"]

len(linguagens) 
# 5
```

##### sorted()

Tupla: ✔

```python
linguagens = ["python", "js", " c", " java", "csharp"]

# Ordenação crescente por tamanho das palavras
sorted(linguagens, key=
lambda x: len(x)) 
>>> ["c", "js", "java", "python", "csharp"]

# Ordenação decrescente por tamanho das palavras
sorted(linguagens, key=
lambda x: len(x), reverse= True) 
>>> ["python", "csharp",
"java", "js", "c"]
```
---
Feito por [cla-isse](https://github.com/cla-isse) 💜