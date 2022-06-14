# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

from time import sleep

print('Gerador de PA\n', '=-'*15)
pt = int(input('Qual o primeiro termo da PA desejada? '))
rz = int(input('Qual a razão da PA desejada? '))
qt = int(input('Quantos termos você deseja ver na PA? '))
print('=-'*15)

print('\033[1;32mGERANDO PA...\033[m')
sleep(1.5)

print(pt, '-> ', end='')
while qt > 1:
    pt = pt + rz
    print(pt, '-> ', end='')
    qt -= 1

print('FIM')
