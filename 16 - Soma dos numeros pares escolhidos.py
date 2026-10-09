print('Soma dos numeros pares inteiros escolhidos')
s = 0
for c in range(1,7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        s += n
print('A soma dos numeros pares escolhidos é {}'.format(s))
