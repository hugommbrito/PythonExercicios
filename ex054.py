# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maior_idade = 21
de_maior = 0
de_menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano nasceu a {c}ª pessoa? '))
    idade = atual - ano
    if idade >= maior_idade:
        de_maior += 1
    else:
        de_menor += 1
print(f'{de_maior} pessoas tem mais que {maior_idade} anos e {de_menor} são menor de idade.')