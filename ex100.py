# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def sorteia():
    for c in range(0, 5):
        sorteado = randint(0, 50)
        lista.append(sorteado)
    print(f'Sorteando 5 valores para a lista: {lista}')


def somaPar():
    totPar = 0
    for c in lista:
        if c % 2 == 0:
            totPar += c
    print(f'Somando os valores pares da lista, temos um total de {totPar}')


lista = []
sorteia()
somaPar()
