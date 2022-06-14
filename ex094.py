# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

listaGeral = []
dictTemp = {}
kg = 'z'
while True:
    dictTemp['nome'] = str(input('Nome: ')).strip().capitalize()
    dictTemp['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while dictTemp['sexo'] not in 'MF':
        dictTemp['sexo'] = str(input('Entrada inválida, digite apenas M ou F.\nSexo: [M/F] ')).strip().upper()[0]
    dictTemp['idade'] = int(input('Idade: '))
    listaGeral.append(dictTemp.copy())
    dictTemp.clear()
    kg = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while kg not in 'SN':
        kg = str(input('Entrada inválida, digite apenas S ou N\nDeseja continuar? [S/N]')).strip().upper()[0]
    if kg == 'N':
        break

# print(listaGeral)
# print(dictTemp)

print('=-' * 20)
print(f'A) Ao todo, {len(listaGeral)} pessoas foram cadastradas')
idadeTotal = 0
for c in range(0, len(listaGeral)):
    idadeTotal += listaGeral[c]['idade']
idadeMedia = idadeTotal / len(listaGeral)
print(f'B) A média das idades é de {idadeMedia:.0f}')
mulheres = []
for c in listaGeral:
    if c['sexo'] == 'F':
        mulheres.append(c['nome'])
print(f'C) As mulheres cadastradas foram: {mulheres}')
print('D) Lista de pessoas com idade acima da média:')
for c in range(0, len(listaGeral)):
    if listaGeral[c]['idade'] > idadeMedia:
        print(f'    => Nome: {listaGeral[c]["nome"]} // Sexo: {listaGeral[c]["sexo"]} // Idade: {listaGeral[c]["idade"]}')
print('<<< PROGRAMA ENCERRADO >>>'.center(40))
