# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

# Primeira forma: Como eu fiz de forma intuitiva
"""s = str(input('Qual o seu sexo [M/F]? ')).lower()
while s != 'm' and s != 'f':
    s = str(input('Você digitou uma opção inválida, digite M para MASCULINO ou F para FEMININO: ')).lower()
print(f'Sexo {s.upper()} computado com sucesso.')"""

#Segunda Forma: Como ele resolveu no vídeo

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MFmf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo.upper()))