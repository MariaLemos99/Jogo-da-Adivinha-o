from random import randint

print(' Iníciando Jogo de Advinhação')

random = randint(0, 100)
chute = 0;
chances = 10;
while chute != random:
    chute = input('Chute um número entre 0 a 100: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('')
            print('Parabéns, você venceu!\nO número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break;
        if chute < 0 or chute > 100:
            print('')
            print('Número inválido, por favor digite um número entre 0 a 100.')
            print('')
        else:
            print('')
            if chute > random:
                print('Você errou!É um número menor.')
            else:
                print('Você errou!É um número maior.')
            print('Você ainda possui {} chances.'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram, você perdeu!')
            print('')
            break;
    else:
        print('')
        print('Esse caractere não é válido! Digite apenas números.')
        print('')

print('Fim de jogo')