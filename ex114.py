# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

from urllib import request

try:
    site = request.urlopen('http://pudim.com.br')
except:
    print('O site do pudim não está acessível no momento, procure outra sobremesa.')
else:
    print('O site do pudim está acessível no momento, bom apetitte.')
