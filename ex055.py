# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior_peso = None
menor_peso = None
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if maior_peso is None:
        maior_peso = peso
    elif maior_peso < peso:
        maior_peso = peso
    if menor_peso is None:
        menor_peso = peso
    elif menor_peso > peso:
        menor_peso = peso
print(f'O maior peso da lista é {maior_peso}\nO menor peso da lista é {menor_peso}')
