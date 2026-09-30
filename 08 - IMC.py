print('Bem vindo ao IMC DIGITAL')

peso = float(input('Digite se peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso normal')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida, Vá se tratar!')

print('FIM')
