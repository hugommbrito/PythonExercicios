# Faça um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra A
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).strip().lower()
print('\033[32mNessa frase a letra A aparece {} vezes. '.format(frase.count('a')))
print('\033[33mA primeira ocorrência da letra A é na posição {}'.format(frase.find('a')+1))
print('\033[34mA ultima ocorrência da letra A é na posição {}'.format(frase.rfind('a')+1))
