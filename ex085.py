# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

tudo = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite {c}º número: '))
    if num % 2 == 0:
        tudo[0].append(num)
    else:
        tudo[1].append(num)

print('+=' * 30)
print(f'Os números pares digitados foram {sorted(tudo[0])}')
print(f'Os números impares digitados foram {sorted(tudo[1])}')
