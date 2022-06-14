# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    print('~' * (len(msg) + 4))
    print(msg.center(len(msg)+4))
    print('~' * (len(msg) + 4))


escreva('Olá, Mundo!')
escreva('Oi')
escreva('Teste de Mensgaem loooooonga')
