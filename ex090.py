# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

# Primeira Forma: como eu fiz de forma intuitiva
"""nome = str(input('Nome: ')).strip().capitalize()
media = float(input(f'Média de {nome}: '))
if media >= 7:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'
info = {'nome': nome, 'media': media, 'situacao': situacao}

print('=-' * 12)
print(f'O nome do aluno é {info["nome"]}\nA média do aluno é {info["media"]}')
print(f'{info["nome"]} foi {info["situacao"]}!')"""

# Segunda Forma: como ele resolveu no vídeo
info = dict()
info['nome'] = str(input('Nome: ')).strip().capitalize()
info['media'] = float(input(f'Média de {info["nome"]}: '))
if info["media"] >= 7:
    info['situacao'] = 'APROVADO'
else:
    info['situacao'] = 'REPROVADO'

print('+-' * 20)
for k, v in info.items():
    print(f'{k} é igual a {v}')
