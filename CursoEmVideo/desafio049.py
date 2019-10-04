soma = 0
cont = 0
for impar in range(1, 22, 2):
    if impar % 3 == 0:
        cont += 1
        soma += impar
print(f'{cont} números ímpares multiplos de 3 de 1 até 21 encontrados')
print(f'Soma entre eles: {soma}.')
