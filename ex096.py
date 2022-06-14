#  Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
#  terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    print(f'O terreno mede {larg} x {comp} e su área é de {larg*comp}m²')


print('-' * 20)
print('CALCULADORA DE ÁREA'.center(20))
print('-' * 20)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
