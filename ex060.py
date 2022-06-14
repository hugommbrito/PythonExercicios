# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Primeira Forma: Como fiz de forma intuitiva
"""n = int(input('Digite um número: '))
count_n = n
fact_n = n

while count_n > 1:
   count_n = count_n - 1
   fact_n = fact_n * count_n

print(f'CALCULANDO: {n}! = {fact_n}')"""

# Segunda Forma: Importando a função FACTORIAL da biblioteca MATH
"""from math import factorial
n = int(input('Digite um número para ver o seu fatorial: '))
f = factorial(n)
print(f'CALCULANDO 2: {n}! = {f}')"""

# Terceira Forma: Como ele fez no vídeo, adicionando o texto
"""n = int(input('Digite um número para ver o seu fatorial:'))
l = n
f = n

print(f'CALCULANDO: {n}! = ', end='')
while l >= 1:
    print(f'{l} ', end='')
    print('X ' if l > 1 else '= ', end='')
    l -= 1
    if l > 1:
        f *= l

print(f)"""

#Quarta Forma: Usando o FOR

n = int(input('Digite um número para ver o seu fatorial: '))
cont= n
f = n
for c in range(0, cont-1):
    cont -= 1
    f = f * cont

print(f'{n}! = {f}')