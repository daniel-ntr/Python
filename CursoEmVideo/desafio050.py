print('-='*8)
print('TABUADA')
print('-='*8)
usuario = int(input('Digite um número para exibir sua tabuada: '))
for tabuada in range(1, 11):
    resultado = usuario * tabuada
    print(f'{usuario} x {tabuada:2} = {resultado}')
print('FIM')

'''num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} X {c:2} = {num*c}')'''
