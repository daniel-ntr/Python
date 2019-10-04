from random import randint, choice

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior = menor = -1
print('Os números sorteados foram: ', end='')

for escolher in range(1, 6):
    sorteio = choice(numeros)
    if sorteio > maior and escolher == 1:
        maior = menor = sorteio
    else:
        if sorteio > maior:
            maior = sorteio
        if sorteio < menor:
            menor = sorteio
    print(sorteio, ' ', end='')
    sorteio = 0

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

'''n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10),)
print('Os valores sorteadors foram:', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')'''