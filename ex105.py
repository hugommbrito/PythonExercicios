# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# – Quantidade de notas – A maior – A menor nota – A média da turma – A situação (opcional)


# Primeira forma: como eu fiz de maneira intuitiva
'''def notas(*notas, sit=False):
    """
    Essa função recebe quantas notas o usuário quiser informar e retorna as informações de TOTAL DE NOTAS INFORMADAS,
    MAIOR NOTA, MENOR NOTA, MÉDIA DAS NOTAS e A SITUAÇÃO(Opcional)
    :param notas: Informe quatnas notas quiser e receba as informações a repeito delas
    :param sit: Altere para TRUE caso queira que a situação seja exibida
    :return: Retorna um dicionário com TOTAL DE NOTAS INFORMADAS, MAIOR NOTA, MENOR NOTA, MÉDIA DAS NOTAS e A SITUAÇÃO(Opcional)
    """

    resultado = {}

    resultado['Total'] = len(notas)

    maior = menor = contador = soma = 0
    for c in notas:
        if contador == 0:
            maior = menor = c
        if c > maior:
            maior = c
        if c < menor:
            menor = c

        soma += c
        contador += 1

    resultado['Maior'] = maior
    resultado['Menor'] = menor
    resultado['Média'] = soma / contador

    if sit:
        if resultado['Média'] < 5:
            resultado['Situação'] = "RUIM"
        elif 5 <= resultado['Média'] < 7:
            resultado['Situação'] = "MEDIANO"
        elif 7 <= resultado['Média'] < 10:
            resultado['Situação'] = "BOM"
        else:
            resultado['Situação'] = "EXCELENTE"

    return resultado


# Programa Principal
resp = notas(5, 7, 2, sit=True)
print(resp)
help(notas)'''


# Segunda Forma: como ele fez, de maneira bastante simplificada:

def notas(*notas, sit=False):
    """
    Essa função recebe quantas notas o usuário quiser informar e retorna as informações de TOTAL DE NOTAS INFORMADAS,
    MAIOR NOTA, MENOR NOTA, MÉDIA DAS NOTAS e A SITUAÇÃO(Opcional)
    :param notas: Informe quatnas notas quiser e receba as informações a repeito delas
    :param sit: Altere para TRUE caso queira que a situação seja exibida
    :return: Retorna um dicionário com TOTAL DE NOTAS INFORMADAS, MAIOR NOTA, MENOR NOTA, MÉDIA DAS NOTAS e A SITUAÇÃO(Opcional)
    """

    resultado = {}

    resultado['Total'] = len(notas)
    resultado['Maior'] = max(notas)
    resultado['Menor'] = min(notas)
    resultado['Média'] = sum(notas) / len(notas)

    if sit:
        if resultado['Média'] < 5:
            resultado['Situação'] = "RUIM"
        elif 5 <= resultado['Média'] < 7:
            resultado['Situação'] = "MEDIANO"
        elif 7 <= resultado['Média'] < 10:
            resultado['Situação'] = "BOM"
        else:
            resultado['Situação'] = "EXCELENTE"

    return resultado


# Programa Principal
resp = notas(5, 7, 2, 10, sit=True)
print(resp)
help(notas)