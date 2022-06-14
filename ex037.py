# Escreva um programa que leia um número inteiro e paça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para hexadecimal e 3 para octal

n = int(input('Digite um número inteiro: '))
h = str(hex(n))
b = str(bin(n))
o = str(oct(n))

print('[ 1 ]\033[32m Converter para BINÁRIO\033[m\n[ 2 ]\033[33m Converter para HEXADECIMAL\033[m\n'
      '[ 3 ]\033[34m Converter para OCTAL\033[m')
op = int(input('Qual a sua opção? '))

if op == 1:
    print(f'\033[1;32m O número {n} em binário é {b[2:]}.\033[m')
elif op == 2:
    print(f'\033[1;33m O número {n} em hexadecimal é {h[2:]}.\033[m')
elif op == 3:
    print(f'\033[1;34m O número {n} em octal é {o[2:]}.\033[m')
else:
    print('Você não digitou uma opção válida, tente novamente')
