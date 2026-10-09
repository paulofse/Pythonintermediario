print('Tabuada 2.0')

n = int(input('Digite um numero para saber a tabuada: '))
s = 0
m = 0
print('Tabuada de Adição do {}'.format(n))
for c in range(1,11):
    s = n + c
    print('{} + {} = {}' . format(n,c,s))

print( '-=' * 40)

print('Tabuada de Multiplicação do {}'.format(n))
for c in range(1,11):
    m = n * c
    print('{} * {} = {}' . format(n,c,m))

print('E essa foi a tabuada 2.0')
