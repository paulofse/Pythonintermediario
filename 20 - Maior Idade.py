import datetime
from datetime import date
today = date.today()
ano = today.year
mai = 0
men = 0

print('Bem vindo ao Contador de Maior Idade (21 anos)')

for c in range(0, 7):
    idade = int(input('Digite seu ano de nascimento: '))
    if ano - idade >= 21:
        mai += 1
    else:
        men += 1
print('das 7 pessoas {} são maiores de idade'.format(mai))
print('das 7 pessoas {} são menores de idade'.format(men))