# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()

dados['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = list()
for c in range(0, partidas):
    dados['gols'].append(int(input(f'   Quantos gols na {c + 1}ª partida: ')))
dados['total'] = sum(dados['gols'])

print('=-' * 28)
print(dados)
print('=-' * 28)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 28)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas')
for c in range(0, partidas):
    print(f'    => Na {c+1}ª partida ele fez {dados["gols"][c]} gols.')
print(f'foi um total de {dados["total"]} gols.')