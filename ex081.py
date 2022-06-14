# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    kg = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if kg in 'Nn':
        break
    else:
        continue


print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')

if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 NÃO foi encontrado na lista.')
