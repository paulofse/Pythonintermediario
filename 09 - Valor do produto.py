print('BEM VINDO A LOJA ONLINE')

produto = float(input('Digite o valor do produto: '))

print('O pagamento deverá ser feito das seguintas formas:')
print('à vista, com 10% de desconto. DIGITE 1')
vista = produto - (produto*10/100)
print('à vista no cartão, com 5% de desconto. DIGITE 2')
vistac = produto - (produto*5/100)
print('Em até 2x no cartão sem juros DIGITE 3')
#usar a var produto
print('Em 3x ou mais com 20% de juros DIGITE 4')
cartao3 = produto + (produto*20/100)



pag = int(input('DIGITE A FORMA DE PAGAMENTO:'))
if pag == 4:
    parcelas = int(input('em quantas vezes:'))

if pag == 1:
    print('Sua compra no valor de R${:.2f} ficará por, R${:.2f} com 10% de desconto'.format(produto, vista))
    print('Seu desconto foi de R$:{}'.format(produto*10/100))
elif pag == 2:
    print('Sua compra no valor de R${:.2f} ficará por, R${:.2f} com 5% de desconto'.format(produto, vistac))
    print('Seu desconto foi de R$:{}'.format(produto*5/100))
elif pag == 3:
    print('Sua compra no valor de R${:.2f} em 2x sem juros.'.format(produto))
    print('Sua compra nao teve descontos')
elif pag == 4:
    print('sua compra no valor de R${:.2f} em {} vezes no cartão, ficará por R${:.2f} com 20% de juros.'.format(produto, parcelas, cartao3))
    print('Seu acrescimo foi de R$:{}'.format(produto*20/100))


