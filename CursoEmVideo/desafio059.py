from random import randint
tentativas = 0
computador = randint(0, 10)
acertou = False
print('-='*10)
print('JOGO DA ADIVINHAÇÃO!')
print('-='*10)
print('Pensei em um número entre 0 e 10...')
while not acertou:
    jogador = int(input('Qual número pensei? ').strip())
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(f'Mais... Tente de novo: ')
        elif jogador > computador:
            print(f'Menos... Tente de novo: ')
print(f'Você acertou e precisou de {tentativas} tentativas!')