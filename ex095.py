#  Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
#  de detalhes do aproveitamento de cada jogador.

dados = dict()
time = list()
kg = 'z'

while True:
    dados['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    dados['gols'] = list()
    for c in range(0, partidas):
        dados['gols'].append(int(input(f'   Quantos gols na {c + 1}ª partida: ')))
    dados['total'] = sum(dados['gols'])
    time.append(dados.copy())
    dados.clear()

    kg = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    while kg not in 'SN':
        kg = str(input('Resposta inválida, digite apenas S ou N!\nDeseja Continuar? [S/N]')).strip().upper()[0]
    if kg == 'N':
        break

# print(time)
# print(dados)

print('=-' * 25)
print('COD', 'NOME'.center(15), 'GOLS'.center(20), 'TOTAL')
print('-' * 50)
for i, v in enumerate(time):
    print(f'{i:^3}', v['nome'].center(15), f'{str(v["gols"]):^20}', f'{v["total"]:^12}')

while True:
    print('-' * 50)
    mostrar = int(input('Mostrar dados de qual jogador? [999 para sair] '))
    while mostrar > len(time)-1 and mostrar != 999:
        mostrar = int(input('Entrada inválida! Digite o código do jogador.'))
    if mostrar == 999:
        break

    print(f'Levantamento do jogador {time[mostrar]["nome"].upper()}'.center(50, '~'))
    for i, v in enumerate(time[mostrar]['gols']):
        print(f'No jogo {i+1} fez {v} gols.'.center(50))

print('<<<PROGRAMA ENCERRADO>>>'.center(50))
