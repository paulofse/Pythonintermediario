print('primeiro vamos saber se as retas formam um triangulo')

r1 = int(input('primeira reta: '))
r2 = int(input('segunda reta: '))
r3 = int(input('terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Suas retas formam um triangulo')
    if r1 == r2 == r3:
        print('Triangulo Equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3: #r1 =! r2 =! r3 =! r1:
        print('Isoceles')
    else:
        print('Triangulo Escaleno')
else:
    print('Infelizmente não temos um triangulo')
print('fim')