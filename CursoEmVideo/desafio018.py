from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipot = hypot(co, ca)
'''hi = (co ** 2 + ca ** 2) ** (1/2)'''
print(f'A hipotenusa é: {hipot:.2f}')
