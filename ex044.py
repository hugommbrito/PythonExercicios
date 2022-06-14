# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('{:*^30}'.format(' LOJAS HUGUINHO '))
preco = float(input('Qual o Valor do produto? R$'))
print('Selecione a melhor forma de pagamento para você:')
print('\033[1m[ 1 ]\033[m À vista dinheiro/cheque;')
print('\033[1m[ 2 ]\033[m À vista no cartão;')
print('\033[1m[ 3 ]\033[m Em 2x no cartão;')
print('\033[1m[ 4 ]\033[m Em mais do que 2x no cartão.')

pgto = int(input('Qual será a sua forma de pagamento?'))
if pgto == 1:
    print(f'O valor em dinheiro será R${preco * 0.9}')
elif pgto == 2:
    print(f'O valor a vista no crédito será R${preco * 0.95}')
elif pgto == 3:
    print(f'O valor em 2x no crédito será R${preco * 1}')
elif pgto == 4:
    print(f'O valor em mais de 2x no crédito será R${preco * 1.2}')
else:
    print(f'Você não digitou uma opção válida, tente novamente.')
