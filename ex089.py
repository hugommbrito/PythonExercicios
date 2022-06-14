# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que
# o usuário possa mostrar as notas de cada aluno individualmente.

# Em paralelo a este curso eu fiz um pequeno curso de fundamentos de JS para o processo seletivo da tribe,
# nesse curso vi o uso de funções e quis testar aqui no python

listaAlunos = []
alunoProvisorio = []
continuar = ''


def imprimirboletim():  # Função para imprimir o boletim no console
    print('-' * 40)
    print('BOLETIM DA TURMA'.center(40))
    print('-' * 40)
    print('  Nº Nome      Média')
    print('-' * 25)
    for n in range(0, len(listaAlunos)):
        print(f'{n}'.center(5), end='')
        print(f'{listaAlunos[n][0]:10}', end='')
        print(f'{((listaAlunos[n][1] + listaAlunos[n][2]) / 2):.1f}')
    print('-' * 25)


def vernotasaluno():  # Função para consultar as notas dos alunos
    while True:
        aluno = int(input('Qual o Nº do aluno que deseja ver as notas? [999 para sair] '))
        print('~' * 25)
        if aluno == 999:
            print('PROGRAMA FINALIZADO. ATÉ O PRÓXIMO BIMESTRE.')
            break
        elif aluno < len(listaAlunos):
            print(f'Aluno: {listaAlunos[aluno][0]} -> 1ª prova: {listaAlunos[aluno][1]:.1f} '
                  f'-> 2ª prova: {listaAlunos[aluno][2]}:.1f')
        else:
            print('Aluno não cadastrado.')

while True: # Laço while se repete até que todos os alunos estejam cadastrados
    alunoProvisorio.append(str(input('Nome: ')).strip().capitalize())
    alunoProvisorio.append(float(input('1ª Nota: ')))
    alunoProvisorio.append(float(input('2 Nota: ')))
    listaAlunos.append(alunoProvisorio[:])
    alunoProvisorio.clear()
    continuar = str(input('Deseja cadastrar outro aluno? [S/N] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Resposta inválida. Deseja cadastrar outro aluno? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

imprimirboletim()
vernotasaluno()
