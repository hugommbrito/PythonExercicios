# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
soma = 0
for c in range(1, n+1):
    div = n % c
    if div == 0:
        soma = soma + 1
        print('{}{}{}'.format('\033[32m', c, '\033[m'), end=' ')
    else:
        print('{}{}{}'.format('\033[31m', c, '\033[m'), end=' ')
if soma == 2:
    print(f'\033[1;32m\n{n} é um número primo!\033[m')
else:
    print(f'\033[1;31m\n{n} não é primo, ele é divisível por {soma} números.\033[m')
