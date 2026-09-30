from datetime import date
hoje = date.today()
ano = hoje.year

print('Confederação de Atletas')
print('Vamos a sua classificação de categoria de acordo com a sua idade!')

print(' Até 9 anos, MIRIM.\n Até 14 anos, INFANTIL.\n até 19 anos, JUNIOR.\n até 20 anos, Senior.\n De 21 anos em diante, Master.')

idade = int(input('Informe o ano de nascimento: '))

cat = ano - idade

if cat <= 9:
    print('MIRIM')
elif cat <= 14:
    print('INFANTIL')
elif cat <= 19:
    print('JUNIOR')
elif cat <= 20:
    print('SENIOR')
else:
    print('MASTER')