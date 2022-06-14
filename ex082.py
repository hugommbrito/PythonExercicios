# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listaImpar = []
listaPar = []
continuar = 'z'

while True:
    num = int(input('Digite um Número: '))
    lista.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

    continuar = str(input('Deseja Continuar? [S/N] ')).strip().lower()[0]
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Resposta Inválida. Deseja continuar? [S/N] ')).strip().lower()[0]

    if continuar == 'n':
        break
    elif continuar == 's':
        continue

print(f'Os números digitados foram {lista}\nOs pares são {listaPar}\nOs ímpares são {listaImpar}')
