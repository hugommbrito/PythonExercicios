# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# Primeira forma: Como fiz de forma intuitiva
"""from random import sample

sorteio = sample(range(9), k=5)
tupla = tuple(sorteio)
print(tupla)

big = 0
small = 10

for l in range(0, 5):
    if tupla[l] > big:
        big = tupla[l]
    elif tupla[l] < small:
        small = tupla[l]

print(f'O maior número é {big} e o menor é {small}.')"""

# Segunda forma: como ele resolveu no curso
from random import randint

lista = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(lista)
print(f'O maior número é {max(lista)} e o menor é {min(lista)}.')