print('Soma dos numeros impares multiplos de 3, entre 1 e 50')
s = 0
cont = 0
for c in range(0,501):
    if c % 2 != 0 and c % 3 == 0:
        cont += 1
        s += c
print('O resultado da soma é {}.' .format(s))
print(cont)

print('FIM')
