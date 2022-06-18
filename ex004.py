# Ask for some data and deliver all the Primitive Types related to it
data = input('\033[1mHey there, just type something:')

print('The primitive Type of the data is ', type(data))

print('Is it Alphanumeric?', data.isalnum())

print('Is it Alphabetic?', data.isalpha())
print('Is it in lower case?', data.islower())
print('Is it in upper case?', data.isupper())

print('Is it a number?', data.isnumeric())
print('Is it a decimal number?', data.isdecimal())
