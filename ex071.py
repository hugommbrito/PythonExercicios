# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

#  Primeira Forma: Como resolvi de forma intuitiva
"""print('='*30)
print(' BANCO ZÉ '.center(30, '~'))
print('='*30)

val = int(input('Qual o valor a ser sacado? R$'))

n50 = val // 50
val = val - (n50 * 50)
n20 = val // 20
val -= (n20 * 20)
n10 = val // 10
val -= (n10 * 10)
n1 = val // 1

print(f'Total de {n50:^3} notas de R$50,00' if n50 != 0 else '', end='')
print(f'\nTotal de {n20:^3} notas de R$20,00' if n20 != 0 else '', end='')
print(f'\nTotal de {n10:^3} notas de R$10,00' if n10 != 0 else '', end='')
print(f'\nTotal de {n1:^3} notas de R$1,00'if n1 != 0 else '', end='')
print('\n', '='*29, '\nVolte sempre ao Banco Zé! Tenho um bom dia!')"""

# Segunda Forma: como ele resolveu no vídeo.
print('='*30)
print(' BANCO ZÉ '.center(30, '~'))
print('='*30)

val = int(input('Qual o valor a ser sacado? R$'))
ced = 50
totced = 0

while True:
    if val >= ced:
        val -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced:^3} notas de R${ced:.2f}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if val == 0:
            break
print('='*30, '\nVolte sempre ao Banco Zé! Tenho um bom dia!')