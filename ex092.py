# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

registro = dict()

registro['nome'] = str(input('Nome: ')).capitalize().strip()
anoNascimento = int(input('Ano de Nascimento: '))
registro['idade'] = datetime.now().year - anoNascimento
registro['CTPS'] = int(input('Nº da Carteira de Trabaho [0 se não tiver]: '))
if registro['CTPS'] == 0:
    registro['CTPS'] = 'INEXISTENTE'
else:
    registro['contratacao'] = int(input('Ano de Contratação: '))
    registro['salario'] = int(input('Salário Atual: R$'))
    registro['idadeAposentadoria'] = registro['contratacao']-anoNascimento+30

print('=-' * 25)
for k, v in registro.items():
    print(f'  - {k} tem valor {v}')
