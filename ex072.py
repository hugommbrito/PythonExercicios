# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

pedido = int(input('Digite um número entre 0 e 20: '))
while True:
    if pedido > 20 or pedido < 0:
        pedido = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
    else:
        break

print(f'Você digitou o número {extenso[pedido]}')
