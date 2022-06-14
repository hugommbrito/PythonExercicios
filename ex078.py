# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = []
for n in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {n+1}: ')))

print('=-' * 22)
print(f'Você digitou os números {lista}')
print(f'O maior valor foi {max(lista)} e ele apreceu primeiro na posição {lista.index(max(lista))+1}')
print(f'O menor valor foi {min(lista)} e ele apareceu primero na posição {lista.index(min(lista))+1}')