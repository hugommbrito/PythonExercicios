# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

n = float(input('Digite um preço R$'))

print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, formatar=False)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n)}')
print(f'Aumentando 10% temos {moeda.aumentar(n)}')
print(f'Diminuindo 10% temos {moeda.diminuir(n, formatar=False)}')
