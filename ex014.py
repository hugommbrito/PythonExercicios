# Peça uma temperatura em °C e converta para °F
c = float(input('Digite uma temperatura em ºC:'))
f = c * 1.8 + 32
print('\033[1m{:.1f}ºC corresponde a {:.0f}ºF'.format(c, f))
