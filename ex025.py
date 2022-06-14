# Faça um programa que peça o nome completo de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual é o seu nome completo? ')).strip().upper()
procurar = 'MELO'
print('Seu nome tem {}? \033[31m{}\033[m'.format(procurar, procurar in nome))
