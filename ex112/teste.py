# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dados

n = dados.leiaDinheiro('Digite um preço R$')
moeda.resumo(n, 25, 12)
