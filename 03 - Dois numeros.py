n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('O primeiro numero {} é maior que o segundo numero {}'.format(n1,n2))
elif n2 > n1:
    print('O segundo numero {} é maior que o primeiro numero {} '.format(n2,n1))
else:
    print('Os numeros dao iguais')
