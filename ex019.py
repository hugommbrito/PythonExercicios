# Desenvolva um programa que escolha o nome de um aluno dentro de uma lista de nomes.

# Primeira Forma: Importando a biblioteca random completa
import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
sala = [a, b, c, d]
escolhido = random.choice(sala)
print('\033[1;30;44mO aluno escolhido foi', escolhido, '\033[m')

# Segunda Forma: Importando apenas a função choice na biblioteca random
"""from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
sala = [a1, a2, a3, a4]
escolhido = choice(sala)
print('O aluno escolhido foi {}'.format(escolhido))"""
