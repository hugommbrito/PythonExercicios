# Escreva um programa que leia um nome completo e diga qual o primeiro e ultimo nome da pessoa.

nome = str(input('Digite o seu nome completo: ')).strip().lower()
separa_nome = nome.split()
primeiro_nome = separa_nome[0]
ultimo_nome = separa_nome[len(separa_nome)-1]
print('\033[32mSeu primeiro nome é {}'.format(primeiro_nome))
print('\033[33mSeu ultimo nome é {}' .format(ultimo_nome))
print('\033[34mSeu nome no passaporte será: {}, {}'.format(ultimo_nome.capitalize(), primeiro_nome.capitalize()))
