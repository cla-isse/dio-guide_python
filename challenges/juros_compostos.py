valor_inicial = float(input('Insira o montante a ser investido: '))
taxa_juros = float(input('Insira, em decimal, o valor mensal da taxa de juros: '))
periodo = int(input('Insira, em meses, o período do investimento: '))

# TO-DO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

valor_final = valor_inicial * (1 + taxa_juros) ** periodo

print(f'Valor final do investimento: R$ {valor_final:.2f}')