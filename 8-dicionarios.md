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

[6. Listas e Tuplas](./6-listas_e_tuplas.md)

[7. Conjuntos](./7-conjuntos.md)

[8. Dicionários](./8-dicionarios.md#8-dicionários) <-
* [8.1 Criação de Dicionários e Acesso aos Dados](#81-criação-de-dicionários-e-acesso-aos-dados)
* [8.2 Métodos da Classe dict](#82-métodos-da-classe-dict)

[9. Funções](./9-funcoes.md)

---

## ![PYTHON](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

### 8. Dicionários

#### 8.1 Criação de Dicionários e Acesso aos Dados

Um **dicionário** é um conjunto **não ordenado** de pares chave-valor, onde as chaves são únicas em uma dada instância do dicionário.

Dicionários são delimitados por chaves e contém uma lista de pares chave-valor separada por vírgulas.

```python
pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome = "Guilherme", idade = 28)

pessoa["telefone"] = "3333-1234"
# {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
```

Os dados são acessados e modificados através da chave.

```python
dados = {"nome": "Guilherme", "idade": 28 , "telefone": "3333-1234"}

dados["nome"] 
# "Guilherme"
dados["idade"] 
# 28
dados["telefone"] 
# "3333-1234"

# Para sobrescrever os valores do dicionário

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados) 
>>> {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
```

##### Dicionários Aninhados

**Dicionários** podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números).

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", " telefone": "3333-2221"},
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos["giovanna@gmail.com"]["telefone"])
>>> "3443-2121"
```

> OBS: Para acessar um dicionário dentro de outro dicionário, não importa quantos níveis abaixo do primeiro, é só acrescentar a chave desejada entre colchetes.
>
> Ex. print(contatos["guilherme@gmail.com"]["nome_completo"]["sobrenome"])

##### Iterar Dicionários

A forma mais comum para percorrer os dados de um dicionário é utilizando o comando **for**.

```python
for chave in contatos:
  print(chave, contatos[chave])

# ou, de forma melhor:

for chave, valor in contatos.items():
  print(chave, valor)

>>> guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
>>> giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
>>> chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
>>> melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}
```

#### 8.2 Métodos da classe dict

##### clear()

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", " telefone": "3333-7766"},
}

contatos.clear()

print(contatos) 
>>> {}
```

##### copy()

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

copia = contatos.copy()

copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"]) 
# {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"]) 
# {"nome": "Gui"}
```

##### fromkeys()

Cria chaves com ou sem valores vincuados. Em um dicionário existente ou não.

```python
nome-do-dicionario.fromkeys(["nome", "telefone"]) 
# {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") 
# {"nome": "vazio", "telefone": "vazio"
```

##### get()

O método get() também retorna valores, e é mais comumente utilizado quando não se sabe se uma chave existe dentro de um dicionário.

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos["chave"] 
# KeyError

contatos.get("chave") 
# None
# Retorno padrão.

contatos.get("chave", {}) 
# {}
# O segundo argumento define o retorno padrão caso uma chave não exista.

contatos.get("guilherme@gmail.com", {}) 
# {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
```

##### items()

Retorna uma lista de tupas, contendo os itens do dicionário.

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.items() 
# dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
```

##### keys()

Retorna as chaves do dicionário.

```python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme"," telefone": "3333-2221"}
}

contatos.keys() 
# dict_keys(['guilherme@gmail.com'])
```

##### pop()

Remove a chave de um dicionário.

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.pop("guilherme@gmail.com") 
# {'nome': 'Guilherme','telefone': '3333-2221'}

contatos.pop("guilherme@gmail.com", {}) 
# {}
```

##### popitem()

Remove os valores de uma chave.

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.popitem() 
# ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone':'3333-2221'})

contatos.popitem() 
# KeyError
```

##### detdefault()

Se a chave não existir no dicionário, ela é adicionada com o valor declarado. 

Se a chave exisir no dicionário, nada acontece (o valor não é atualizado).

```python
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna") 
# Guilherme

contato 
# {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) 
# 28

contato 
# {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
```

##### update()

Se a chave não existir no dicionário, ela é adicionada com o valor declarado. 

Se a chave exisir no dicionário, o valor é atualizado.

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})

contatos 
# {'guilherme@gmail.com': {'nome': 'Gui}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})

contatos 
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322 8181'}}
```

##### values()

Retorna os valores do dicionário.

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.values() 
# dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie','telefone': '3344 9871'}, {'nome': 'Melaine', 'telefone': '3333 7766'}])
```

##### in()

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

"guilherme@gmail.com" in contatos 
# True

"megui@gmail.com" in contatos 
# False

"idade" in contatos ["guilherme@gmail.com"] 
# False

"telefone" in contatos ["giovanna@gmail. com"] 
# True
```

##### del()

```python
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

contatos
# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443 2121'}, 'melaine@gmail.com': {'nome':'Melaine', 'telefone': '3333 7766'}}
```
---
Feito por [cla-isse](https://github.com/cla-isse) 💜