print('Bem vindo ao DIGITAL FINANCEIRO')
valor = float(input('qual valor da casa R$:'))
sal = float(input ('qual seu salario R$:'))
temp = int(input ('Em quanto tempo em anos voce quer pagar a casa?'))

tempm = temp*12
parcela = valor / tempm

if parcela > sal * 0.3:
    print('parcela excede 30% do salario, financiamento negado')
else:
    print('parabens voce pode comprar o Imovel.')
    print('imovel no valor de R$:{}'.format(valor))
    print('{} vezes de {}'.format(tempm,parcela))

print('FIM')


