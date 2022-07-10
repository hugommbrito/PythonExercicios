# Ask for the temperature in ºC and convert it to ºF
c = float(input('Type a temperature in ºC:'))
f = c * 1.8 + 32
print(f'\033[1m{c:.1f}ºC is the same as {f:.0f}ºF')
