# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

pa = t
for c in range(0, 10):
    print(pa, end=' → ')
    pa += r
print('ACABOU.')
