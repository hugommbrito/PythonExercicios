# Ask for the hight and length of a wall and calculate how many liters of paint will be necessarie to paint it.
# (consider that 1L of paint is enought for 2m²)
color = {'green': '\033[1;32m',
         'blue': '\033[1;34m',
         'clean': '\033[m'}
hight = float(input('What is the HEIGHT of your wall?'))
length = float(input('What is the LENGTH of your wall?'))
area = hight * length
inkNeeded = area / 2
print(f"Your wall has {color['green']}{area:.2f}m²{color['clean']} and it will need about "
      f"{color['blue']}{inkNeeded:.2f}L{color['clean']} of ink to be painted")
