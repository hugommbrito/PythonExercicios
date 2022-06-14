from ex115cev.lib.interface import *
from ex115cev.lib.arquivo import *

from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print(f'Arquivo {arq} encontrado com Sucesso.')
else:
    print('Arquivo não encontrado. Vamos cria-lo para você...')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'sair do sistema'])
    if resposta == 1:
        # Opção para ver as pessoas que já estão cadastradas no sistema
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar novas pessoas
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção para sair do sistema
        cabecalho('Saindo do sistema... Até Logo')
        break
    else:
        print('\033[31mERRO! Resposta inválida, digite um número do menu acima.\033[m')
    sleep(2)
