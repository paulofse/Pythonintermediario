print('Bem vindo ao Sistema Escolar Digital')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2


if media >= 7:
    print('Sua média é : {}'.format(media))
    print('Aprovado')
elif 6.9 > media >= 5:
    print('Sua média é : {}'.format(media))
    print('Recuperação')

else:
    print('Sua média é : {}'.format(media))
    print('Reprovado')
