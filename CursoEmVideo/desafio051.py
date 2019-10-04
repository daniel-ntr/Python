soma = 0
for usuario in range(1, 7):
    usuario = int(input(f'Digite o {usuario}º valor: '))
    if usuario % 2 == 0:
        soma += usuario
print(f'Dos números que vocês digitou, a soma dos pares é: {soma}')