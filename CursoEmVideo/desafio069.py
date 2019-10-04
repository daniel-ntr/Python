# Jogo IMPAR/PAR

from random import randint
ganhou = soma = jogador =  total_aposta = 0
impar_par = ''
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

while True:
    jogador = int(input('Digite um valor: '))
    print('-'*30)
    total_aposta += 1
    computador = randint(0, 10)
    soma = jogador + computador

    impar_par = ' '
    while impar_par not in 'PI':
        impar_par = str(input('Par ou Ímpar? [P/I) ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)

    if soma % 2 == 0 and impar_par in 'P' or soma % 2 != 0 and impar_par in 'I':
        ganhou += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! Voçê venceu {ganhou} vez(es). ')
        break
