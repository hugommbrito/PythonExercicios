# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

# Em pesquisa descobri que a soma de dois dos lados tem que ser sempre menor que o terceiro lado.

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1+r2 < r3 or r1+r3 < r2 or r2+r3 < r1:
    print('Os segmentos acima \033[1;4;44m PODEM \033[m formar um triângulo')
else:
    print('Os segmentos acima \033[1;4;41m NÃO PODEM \033[m formar um triângulo')
