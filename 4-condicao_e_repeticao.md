# ![PYTHON](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
Olá, pessoa bonita! Tudo bem com você? 

Este é um resumo construído com base no curso "Introdução à Ciência de Dados e Python", na plataforma [DIO](https://web.dio.me/home).

Mentor: [@guicarvalho](https://github.com/guicarvalho)

## Sumário

[Página Inicial](./README.md)

[1. Ambiente de desenvolvimeto e Primeiros Passos com Python](./1-primeiros_passos.md)

[2. Conhecendo a Linguagem de Programação Python](./2-introducao.md)

[3. Tipos de Operadores](./3-operadores.md)

[4. Estruturas Condicionais e de Repetição](./4-condicao_e_repeticao.md#4-estruturas-condicionais-e-de-repetição) <-
* [4.1 Indentação e Blocos](#41-indentação-e-blocos)
* [4.2 Estruturas Condicionais](#42-estruturas-condicionais)
* [4.3 Estruturas de Repetição](#43-estruturas-de-repetição)

[5. Strings](#5-manipulando-strings)

[6. Listas e Tuplas](#6-listas)

[7. Conjuntos](#7-conjuntos)

[8. Dicionários]()

[9. Funções]()

---

## ![PYTHON](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

### 4. Estruturas Condicionais e de Repetição

#### 4.1 Indentação e Blocos

Indentar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco. Em Java e C por exemplo, utilizamos chaves:

```java
void sacar(double valor) { // início do bloco do método
  if(this.saldo >= valor) { // início do bloco do if
    this.saldo -= valor;
  } // fim do bloco do if
} // fim do bloco do método
```

Porém, o código ainda funciona sem indentação:

```java
void sacar(double valor) {
if(this.saldo >= valor) {
this.saldo -= valor;
}
}
```

O mesmo não acontece em Python.

```python
def sacar(self, valor:float) -> Nome # Início do bloco do método
    if self.saldo >= valor # início do bloco if
        self.saldo -= valor
    # fim do bloco if
# fim do bloco do método
```

#### 4.2 Estruturas Condicionais

Uma estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

##### If

Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada **if**. 

O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

```python
saldo = 2000.0
saque = float(input(f"Você possui um saldo de R${saldo}. Informe o valor do saque: "))

if saldo >= saque:
  print("Saque Realizado!")

if saldo < saque:
  print("Saldo Insuficiente!")
```

##### If/Else

Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas **if** e **else**. 

Se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário, o bloco de código do else será executado.

```python
saldo = 2000.0
saque = float(input(f"Você possui um saldo de R${saldo}. Informe o valor do saque: "))

if saldo >= saque:
  print("Saque Realizado!")
else:
  print("Saldo Insuficiente!")
```

##### If/Elif/Else

Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada **elif**. 

O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. 

* Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas **aumentam a complexidade do código**.

```python
opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato"))

if opcao == 1:
  valor = float(input("Informe o valor do saque: "))
  print(f"Você sacou R${valor}")

elif opcao == 2:
  print("Exibindo o Extrato")

else:
  exit("Opção Inválida")
```

##### If aninhado

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.

```python
if conta_normal:
  if saque <= saldo:
    print("Saque realizado com sucesso!")
    elif saque >= (saldo + cheque_especial):
      print("Saque realizado com uso do cheque especial")
elif conta_universítária:
  if saque <= saldo:
    print("Saque realizado com sucesso!")
  else:
    print("Saldo insuficiente")
```

##### If ternário

O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes:
1. O retorno caso a expressão retorne verdadeiro.
2. A expressão lógica. 
3. retorno caso a expressão não seja atendida.

```python
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
```

#### 4.3 Estruturas de Repetição

Estruturas de repetição são utilizadas para repetir um trecho de código um determinado número de vezes. 
* Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

Receba um número do teclado e exiba os 2 números seguintes:

```python
# Sem repetição 

a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)
```

```python
# Com repetição 

a = int(input("Informe um número inteiro: "))
print(a)

"repita 2 vezes":
  a += 1
  print(a)
```

##### For

O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS
    print(letra, end="")

else:
  print() #adiciona um quebra de linha
```

##### Range

Range é uma função built-in do Python usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). 

Se usarmos range(i, j) será produzido: 

> i, i+1, i+2, i+3, ..., j-1.

Ela recebe 3 argumentos:
* stop (obrigatório);
* start (opcional);
* step (opcional).

```python
range(start, stop, step) -> range object
```

```python
list(range(4))
>>> [0, 1, 2, 3]
```

##### Range + For

```python
for numero in range(0, 11):
  print(numero, end=" ")
>>> 0 1 2 3 4 5 6 7 8 9 10

# Exibindo a tabuada do 5
for numero in range(0, 51, 5):
  print(numero, end=" ")
> 0 5 10 15 20 25 30 35 40 45 50
```

##### While

O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

```python
opcao = 3

while opcao != 0:
  opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n"))
  if opcao == 1:
    print("Sacando")
    break # interrompe o looping
  elif opcao == 2:
    print("Exibindo o Extrato")
    break # interrompe o looping
  elif opcao == 0:
    print("Agradecemos por escolher nossos serviços!")
  else: 
    print("Escolha uma opção válida.")
```

> O comando **break** interrompe a execução do código. O comando **continue** ignora o trecho do código ao qual se refere.

---
Feito por [cla-isse](https://github.com/cla-isse) 💜