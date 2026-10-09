import datetime
year = datetime.date.today().year

mih = 0
nh = ''
tm = 0
nm = ''
si = 0

for c in range(0, 4):
    while True:
        sexo = str(input('Masculino(M) ou Feminino(F): ')).lower().strip()
        if sexo == 'm' or sexo == 'f':
            break
        else:
            print('Voce digitou um valor invalido')

    nome = str(input('Nome: ')).lower().strip()
    ano = int(input('Ano de nascimento: '))
    idade = year - ano
    si += idade

    if sexo == 'm':
        if idade > mih:
            mih = idade
            nh = nome
    elif sexo == 'f':
        if idade < 20:
            tm += 1

print('O homem mais velho do grupo é {} com {} anos'.format(nh.capitalize(), mih))
print('Ao todo, temos {} mulheres com menos de 20 anos'.format(tm))
print('A media de idade do grupo é {} anos'.format(si / 4))

