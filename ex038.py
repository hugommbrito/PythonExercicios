# Faça um programa que peça dois números e diga qual deles é maior.
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

if n1 > n2:
    print(f'{n1} é o \033[1mMAIOR')
elif n2 > n1:
    print(f'{n2} é o \033[1mMAIOR')
else:
    print(f'Os números são \033[1mIGUAIS')
