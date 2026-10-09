print('E ai gordinho!')
'''
pesosl = []
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    pesosl.append(peso)

maior = max(pesosl)
menor = min(pesosl)

print('O maior peso {:.1f}Kg e o menor peso {:.1f}Kg.'.format(maior, menor))'''
maior = 0
menor = 0

for p in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if p == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso {:.1f}Kg e o menor peso {:.1f}Kg.'.format(maior, menor))