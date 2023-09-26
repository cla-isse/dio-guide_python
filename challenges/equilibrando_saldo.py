saldo_atual = float(input('Insira seu saldo: ')) # entrada
valor_deposito = float(input('Insira um valor de depósito: ')) # transacao 1 +
valor_retirada = float(input('Insira um valor de saque: ')) # transacao 2 -

#TO-DO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atual = saldo_atual + valor_deposito - valor_retirada

#TO-DO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(f'Saldo atualizado na conta: {saldo_atual:.1f}')