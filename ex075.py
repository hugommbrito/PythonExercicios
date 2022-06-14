# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Primeira Forma: como eu fiz de maneira intuitiva
"""n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o útimo valor: '))

lista = (n1, n2, n3, n4)
print(lista)

n9 = 0
for n in range(0, len(lista)):
    if lista[n] == 9:
        n9 += 1
print(f'O número 9 apareceu {n9} vezes.')
print(f'O número 3 apareceu na {lista.index(3)+1}ª posição')

pares = ''
for n in range(0, len(lista)):
    if lista[n] % 2 == 0:
        pares += str(lista[n])
print(f'Os números pares foram {pares}')"""

# Segunda Forma: como ele resolveu no vídeo
núm = (int(input('Digite um número: ')), int(input('Digite outro número: ')),int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os números {núm}')
print(f'O número 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O número 3 apareceu na posição {núm.index(3)+1}')
else:
    print(f'O número 3 não foi digitado.')
print('Os números pares digitados foram: ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, ' ', end='')
