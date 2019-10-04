from emoji import emojize
from random import choice
from time import sleep
jokenpo = str(emojize(' \033[34mJokenpô!!! VAMOS JOGAR!!!\033[m \033[31m:fist:\033[m \033[33m:hand:\033[m \033[35m:v:\033[m ', use_aliases=True))
print(f'\n{jokenpo:=^75}')
print('\nVamos começar!')
print('''\n[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
aposta = '1Pedra 2Papel 3Tesoura'.split()
computador = choice(aposta)
jogador = str(input('\nDigite um dos números acima para apostar: ').strip())
ganha = str(f'\033[32mSortudo! Eu escolhi {computador[1:]}. VOCÊ GANHOU!\033[m')
perde = str(f'\033[31mHAHAHA!!! Eu escolhi {computador[1:]}. VOCÊ PERDEU!\033[m')
print('-=' * 15)
if jogador == '1' or jogador == '2' or jogador == '3':
    print('Boa sorte!\n\033[31mPedra,\033[m \033[33mPapel e\033[m \033[35mTesoooooooura!!!...\033[m\n')
    sleep(2)
    if jogador in aposta[0] and computador in aposta[2] or jogador in aposta[1] and computador in aposta[0] or jogador in aposta[2] and computador in aposta[1]:
        print(ganha)
    elif jogador in aposta[0] and computador in aposta[1] or jogador in aposta[1] and computador in aposta[2] or jogador in aposta[2] and computador in aposta[0]:
        print(perde)
    else:
        print(f'Eu escolhi {computador[1:]} e você também. EMPATE! ')
else:
    print('\nOpção inválida! Tente novamente!')
print('-='*15)
