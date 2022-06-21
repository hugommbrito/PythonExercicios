# Ask for a nunber and deliver it's mutiplication table.

# In here I've done it just what was tought this far in this course, because I know that it will be remade later in an
# other exercise using the FOR loop.
color = {'red': '\033[1;31m',
       'black': '\033[1;30m',
       'green': '\033[1;32m',
       'yellow': '\033[1;33m',
       'blue': '\033[1;34m',
       'purple': '\033[1;35m'}

number = int(input('Type a integere number between 0 e 9:'))
print(f'Here it is the multiplication table for {number}:')
print(f'{color["red"]}=-'*10)
print(f'{color["green"]}',number, 'x 1 = ', number * 1)
print(number, 'x 2 = ', number * 2)
print(number, 'x 3 = ', number * 3)
print(number, 'x 4 = ', number * 4)
print(number, 'x 5 = ', number * 5)
print(number, 'x 6 = ', number * 6)
print(number, 'x 7 = ', number * 7)
print(number, 'x 8 = ', number * 8)
print(number, 'x 9 = ', number * 9)
print(f'{color["red"]}-='*10)
