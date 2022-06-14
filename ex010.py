# Perguntar quanto dinheiro a pessoa tem e fazer a conversão em dolar (1USD = 3.27BRL)
n = float(input('Quanto dinheiro você tem na carteira? R$'))
d = 3.27
c = n/d
print('Você tem \033[1;32mR${:.2f}\033[m na carteira. Levando em consideração o câmbio de R${:.2f} para cada dolar,'
      'você pode comprar \033[1;32mUSD{:.2f}\033[m!'.format(n, d, c))
