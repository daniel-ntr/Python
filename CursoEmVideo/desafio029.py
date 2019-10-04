from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador "pensar"
print('\033[34m-=-\033[m' * 20)
print('\033[32mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[34m-=-\033[m' * 20)
jogador = int(input('Em qual número pensei? ')) # jogador tenta adivinhar
print('\033[31mPROCESSANDO\033[m', end=' ')
print('\033[31m.\033[m', end= ' ')
sleep(1) # Espera em segundos de espera antes de continuar o restante do código
print('\033[31m.\033[m', end= ' ')
sleep(1)
print('\033[31m.\033[m')
sleep(1)
if -1 < jogador < 6:
    print(f'\033[34mO número que escolhi foi: {computador}!\033[m ')
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m' if computador == jogador else f'\033[31mGANHEI! Eu pensei no número {computador} e não no {jogador}!\033[m ')
else:
    print('\033[32mVoçê precisa escolher um número entre 0 e 5! Reinicie o jogo!\033[m ')






