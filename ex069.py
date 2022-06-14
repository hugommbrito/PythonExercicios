#  Crie um programa que leia a idade e o sexo de várias pessoas.
#  A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior = homens = mulherm = 0
while True:
    sexo = sair = ' '
    print('-'*35)
    print('CADASTRE UMA PESSOA'.center(35))
    print('-'*35)
    idade = int(input('Idade: '))
    while sexo not in "MmFf":
        sexo = str(input('Sexo: ')).strip()[0]

    if idade >= 18:
        maior += 1

    if sexo in 'Mm':
        homens += 1

    if sexo in 'Ff' and idade <= 20:
        mulherm += 1

    print('-' * 35)
    while sair not in 'SsNn':
        sair = str(input('Quer continuar? [S/N] ')).strip()[0]

    if sair in 'Nn':
        break


print('*'*35)
print(f'\033[1;33mPROGRAMA ENCERRADO\033[m\nForam cadastrados:\n-> {maior} pessoas acima de 18 anos.'
      f'\n-> {homens} homens foram cadastrados.\n-> {mulherm} mulheres abaixo de 20 anos foram cadastradas.')
