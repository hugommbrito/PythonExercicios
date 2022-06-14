# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-'*40)
print(' LOJA SUPER BARATÃO '.center(40, '*'))
print('-'*40)

tot = prod1k = 0
prodBV = prodBN = None
while True:
    prod = input('Produto: ')
    val = float(input('Preço: R$'))

    tot += val

    if val > 1000:
        prod1k += 1

    if prodBV is None or prodBV >= val:
        prodBN = prod
        prodBV = val

    sai = ' '
    while sai not in 'SN':
        sai = input('Quer continuar?[S/N] ').strip().upper()[0]
    if sai == 'N':
        break

print(' FIM DO PROGRAMA '.center(40, '-'))
print(f'O total da compra foi de R${tot:.2f}')
print(f'Temos {prod1k} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {prodBN} que custa R${prodBV:.2f}')
