print('DETECTOR DE PALINDROMOS')

f = str(input('Digite uma frase: ')).lower().strip().replace(' ', '')
#palidromo = f.split() *separa a frase em blocos
#junto = ''.join(f) *junta todas as palavras
f2 = f[::-1]

if f == f2:
    print('ISTO É UM PALINDROMO')
else:
    print('ISTO NAO É UM PALIDROMO')