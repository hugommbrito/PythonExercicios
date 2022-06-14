# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*num):
    maior = 0
    for c in range(0, len(num)):
        if c == 0:
            maior = num[c]
        else:
            if num[c] > maior:
                maior = num[c]

    print('=-' * 20, '\nAnalisando os valores passados...')
    for c in range(0, len(num)):
        print(num[c], end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(1, 2, 3, 5, 4)
maior(1, 4, 7, -3, 25, -10)
maior(10, 20)
maior()
maior(-2, -4, -10, -1)
