# Faça um programa que peça um número e diga se ele é par ou ímpar.

num = int(input('Digite um número: '))
rest_div = float(num % 2)

if rest_div > 0:
    print('O número {} é \033[30;44m ÍMPAR! \033[m'.format(num))
else:
    print('O número {} é \033[30;43m PAR! \033[m'.format(num))
