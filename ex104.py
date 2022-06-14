# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
    num = input("Digite um número: ")
    if num.isnumeric():
        return num
    else:
        while not num.isnumeric():
            print(f"\033[1;31mERRO!\033[m Você deve digitar um número inteiro.")
            num = input("Digite um número: ")

        return num

# Programa principal
n = leiaInt()
print(f"Você acabou de digitar o número {n}")
