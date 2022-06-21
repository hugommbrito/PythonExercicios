# Ask for a mesure in meters and return it converted to centimiters and milimiters.
measure = float(input('Type a measure in meters:'))
cm = measure * 100
mm = measure * 1000
print(f'You have typed \033[7m{measure:.2f}m\033[m, that may be converted to \033[1;34m{cm:.0f}cm\033[m or '
      f'\033[1;36m{mm:.0f}mm\033[m')
