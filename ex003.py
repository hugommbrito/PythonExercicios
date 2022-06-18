# Ask for two numbers and deliver the sum between them.
n1 = int(input('Type a number:'))
n2 = int(input('Type an other one:'))
s = n1 + n2
print('\033[43mThe sum between {} and {} is {}\033[m'.format(n1, n2, s))
