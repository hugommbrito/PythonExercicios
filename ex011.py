# Perguntar a altura e largura de uma parede para calcular sua área e quanto de tinta deve ser usado para pinta-la
# (para pintar 2m² usa 1L de tinta)
cor = {'verde': '\033[1;32m',
       'azul': '\033[1;34m',
       'fim': '\033[m'}
x = float(input('Qual a ALTURA da sua parede?'))
y = float(input('Qual a LARGURA da sua parede?'))
a = x * y
t = a/2
print('Sua parede mede {}{:.2f}m²{} e precisará de aproximadamente {}{:.2f}L{} de tinta para ser pintada'
      .format(cor['verde'], a, cor['fim'], cor['azul'], t, cor['fim']))
