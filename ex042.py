# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('\033[1;32mSerá possíve formar um triângulo com essas retas!')
    if l1 == l2 == l3:
        print('Com todos os lados iguais, este será um triângulo EQUILÁTERO')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('Com dois lads iguais, este será um triâgulo ISÓCELES')
    else:
        print('Com todos os lados diferentes, este será um triângulo ESACLENO.')
else:
    print('\033[1;31mNão será possível formar um triângulo com esses segmentos de reta.')
