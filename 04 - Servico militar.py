from datetime import date
hoje = date.today()
ano = hoje.year
#print(hoje)
#print(ano)

print('Bem vindo ao sistema de serviço militar')
print('Data atualizada {}'.format(hoje))
print('de acordo com a sua idade saberemos quando será o seu alistamento!!!')

anouser = int(input('Digite o ano de nascimento: '))
idade = ano - anouser

if idade > 21:
    print('Voce tem {} anos \ne perdeu o prazo de alistamento, Deverá pagar uma multa para regularizar a situação!'.format(idade))
elif 21 > idade > 18:
    print('Voce tem {} anos e terá que se alistar, antes dos 21 anos!'.format(idade))
else:
    print('Voce ainda tem {} anos, e ainda nao está elegivel para o alistamento'.format(idade))



