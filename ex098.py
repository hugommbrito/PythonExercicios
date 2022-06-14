# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep
def contador(a, b, c):
    if c == 0:
        c = 1
    if b < a and c > 0:
        c *= (-1)
    if b > 0:
        b += 1
    elif b <= 0:
        b -= 1
    print('=-' * 20)
    for i in range(a, b, c):
        print(i, end=' ')
        sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('=-' * 20)
print('Agora é sua vez: ')
init = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(init, fim, passo)