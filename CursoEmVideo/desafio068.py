# Tabuada
usuario = tabuada = 0
multiplicador = 1
while True:
    usuario = int(input('Deseja ver a tabuada de qual valor? '))
    print('-' * 20)

    if usuario < 0:
        break

    for multiplicador in range(1, 11):
        print(f'{usuario} X {multiplicador} = {usuario * multiplicador}')
        multiplicador += 1

    print('-' * 20)
print('PROGRAMA TABUADA FINALIZADO. VOLTE SEMPRE!')
