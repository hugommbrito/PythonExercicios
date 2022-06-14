# Crie um programa que leia um nome completo e mostre os três seguintes resultados: Nome maiusculo, Nome Minusculo,
# quantas letras tem o nome e quantas letras tem o primeiro nome
cor = {'azul': '\033[34m', 'verde': '\033[32m', 'fim': '\033[m'}
nome = str(input('Digite seu nome completo: ')).strip()
print('{}Seu nome em maiúsculas fica: {}'.format(cor['azul'], nome.upper()))
print('{}Seu nome em minusculas fica: {}'.format(cor['verde'], nome.lower()))
print('{}Olha como ele fica apenas com a primeira letra maiúscula: {}'.format(cor['azul'], nome.capitalize()))
print('{}Porém, essa é a maneira formal de escreve-lo: {}\n'.format(cor['verde'], nome.title()))
print(f"{cor['azul']}Vamos analiza-lo?")
espaco = nome.count(' ')
letras = len(nome) - espaco
print('{}Seu nome tem {} espaços, mas sem considera-los, ele tem {} letras.'.format(cor['verde'], espaco, letras))
separa = nome.split()
print('{}Seu primeiro nome é {} e ele tem {} letras.{}'.format(cor['azul'], separa[0], len(separa[0]), cor['fim']))
