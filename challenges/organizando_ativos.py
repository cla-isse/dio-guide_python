ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = 3

# Entrada dos códigos dos ativos
for codigoAtivo in range(quantidadeAtivos):
    codigoAtivo = input('Insira 3 ativos financeiros: ')
    ativos.append(codigoAtivo)

# TO-DO: Ordenar os ativos em ordem alfabética.

ativos.sort()

# TO-DO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.

for codigoAtivo in ativos:
    print(codigoAtivo)