# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverso = ''
for letra in range(len(junta)-1, -1, -1):
    inverso = inverso + junta[letra]
print(f'A frase {junta} ao contrário fica {inverso}')
if junta == inverso:
    print('Temos um palíndromo.')
else:
    print('Essa frase não forma um palíndromo.')
