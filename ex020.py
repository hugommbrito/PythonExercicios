# Crie um programa que peça o nome de 4 alunos e os embaralhe para determinar a ordem de apresentação de um trabalho.
from random import shuffle

a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno:'))
a3 = str(input('Terceiro Aluno:'))
a4 = str(input('Quarto ALuno: '))
sala = [a1, a2, a3, a4]
shuffle(sala)
print('\033[1mA ordem de apresentação será {}'.format(sala))
