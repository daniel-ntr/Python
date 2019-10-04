#Fatorial
fatorial = 1
numero = int(input('Digite um número para calcular seu fatorial: '))
anterior = numero
print(f'Calculando {numero}! = ', end='')
while anterior > 0:
    print(f'{anterior}', end='')
    print(' X ' if anterior > 1 else ' = ', end='')
    fatorial *= anterior
    anterior -= 1
print(f'{fatorial}', end='')

'''fatorial = 1
numero = int(input('Digite um número: '))
anterior = numero
print(f'Calculando {numero}! = ', end='')
for numero in range(numero, 0, -1):
    print(f'{numero}', end='')
    print(' X ' if numero > 1 else ' = ', end='')
    fatorial *= anterior
    anterior -= 1
print(f'{fatorial}', end='')'''


'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''
