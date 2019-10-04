peso = []
for pessoas in range(1, 6):
    usuario = float(input(f'Digite o peso(Kg) da {pessoas}ª pessoa: '))
    peso.append(usuario)
listaPesos = sorted(peso)
print(f'O menor peso digitado foi {listaPesos[0]}Kg. ')
print(f'O maior peso digitado foi {listaPesos[-1]}Kg. ')

'''for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {maior}Kg')'''
