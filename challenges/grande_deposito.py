valor = float(input('Insira um valor de depósito: '))

if valor > 0:
  # TO-DO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
  print(f'Deposito realizado com sucesso!\n Saldo atual: R$ {valor:.2f}')
elif valor == 0:
  # TO-DO: Imprimir a mensagem de valor inválido.
  print('Encerrando o programa...')
else:
  # TO-DO: Imprimir a mensagem de encerrar o programa.
  print('Valor invalido! Digite um valor maior que zero.')