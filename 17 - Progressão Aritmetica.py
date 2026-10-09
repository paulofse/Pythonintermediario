print('PROGRESSÃO ARITMETICA')

t1 = int(input('Digite o Primeiro termo da PA'))
ra = int(input('Digite a razao da PA'))
t = int(input('quantos termos voce quer ver?'))
tf = t*ra+ra
s = 0
for c in range(t1,tf,ra):
    if c <= t1+(t-1)*ra:
        print(c, end=' ')
        s += c
print(s, end='')

