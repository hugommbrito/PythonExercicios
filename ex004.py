# Pedir um dado e entregar todos os tipos primitivos relacionados a ele.
dado = input('\033[1mEi moral, digita aí qualquer coisa:')

print('o tipo primitivo do dado é', type(dado))

print('O dado é Alfanumérico?', dado.isalnum())

print('O dado é Alfabético?', dado.isalpha())
print('O dado está em Caixa Baixa?', dado.islower())
print('O dado está em Caixa Alta?', dado.isupper())

print('O dado é um Número?', dado.isnumeric())
print('O dado é um Número Decimal?', dado.isdecimal())
