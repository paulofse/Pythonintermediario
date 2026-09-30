print('Bom dia!')
num = int(input('Escolha um numero'))
conv = str(input('Escolha uma conversao\n 1 para binário\n 2 para octal\n 3 para hexadecimal'))
if conv == '1':
    nbin = bin(num)
    print('O numero em binario é', nbin[2:])
    #print(nbin) com prefixo
elif conv == '2':
    noct = oct(num)
    print('O numero em octal é:',noct[2:])
    #print(noct) com prefixo
elif conv == '3':
    nhex = hex(num)
    print('O numero em hexadecimal é:',nhex[2:])
    #print(nhex) com prefixo
else:
    print('Opção invalida')