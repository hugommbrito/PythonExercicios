# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais agevelho e quantas mulheres têm menos de 20 anos

mid_age = 0
age_older = 0
young_f = 0

# Arrecdação de dados
qnt_pess = 4
for p in range(1, qnt_pess+1):
    print(f'---------- {p}ª PESSOAL ----------')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()

    if p < qnt_pess:  # Calculo da idade média dos alunos.
        mid_age = mid_age + age
    elif p == qnt_pess:
        mid_age += age
        mid_age = mid_age / qnt_pess

    if sex == 'M' and age > age_older:  # Escolher o homem mais velho.
        name_older = name

    if sex == 'F' and age < 20:  # Contar mulheres com menos de 20 anos
        young_f = young_f + 1

print(f'A idade média é {mid_age:.0f} anos.')
print(f'O homem mais velho do grupo é {name_older}')
print(f'O grupo tem {young_f} mulheres com menos de 20 anos')
