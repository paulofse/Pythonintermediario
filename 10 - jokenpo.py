import random
from time import sleep
print('VAMOS BRINCAR DE JOKENPÔ')

print(' Famoso pedra, papel e tesoura!')

print('Regras sao simples,\npedra ganha de tesoura\npapel ganha de pedra\ntesoura ganha de papel ')

print('Sabendo disso, Let´s play:')

print('Vamos usar \n 1 ou pedra \n 2 ou papel \n 3 ou tesoura')

escolhas = {1:'pedra', 2:'papel', 3:'tesoura', 'pedra':'pedra', 'papel':'papel', 'tesoura':'tesoura'}
jokenpo = {'pedra':'tesoura', 'papel':'pedra', 'tesoura':'papel' }

while True:
    choice = random.randint(1, 3)
    choice = escolhas[choice]
    #print(choice)

    user = input('HORA DE ESCOLHER! DIGITE O QUE VOCE QUER!') .lower().strip()
    if user.isdigit():
        user = int(user)
    print('JooOOO...')
    sleep(1)
    print('Keeeen...')
    sleep(1)
    print('POOO!!!')
    sleep(1)

    print('*-'*15)
    if user not in escolhas:
        print("Opção inválida! Escolha apenas 1 ou pedra, 2 ou papel, 3 ou tesoura.")
    else:
        user = escolhas[user]

        if user == choice:
            print('EMPATE')
        elif jokenpo[user] == choice:
            print('VOCE VENCEU')
            if user == 'tesoura':
                print('TESOURA VENCE PAPEL')
            elif user == 'pedra':
                print('PEDRA VENCE TESOURA')
            else:
                print('PAPEL VENCE PEDRA')
        else:
            print('EU VENCI')
            if choice == 'tesoura':
                print('TESOURA VENCE PAPEL')
            elif choice == 'pedra':
                print('PEDRA VENCE TESOURA')
            else:
                print('PAPEL VENCE PEDRA')
        print('*-' * 15)
        continuar = input('Quer jogar de novo? (S/N): ').strip().lower()
        if continuar == 'n':
            print('Obrigado por jogar! Até mais.')
            break


