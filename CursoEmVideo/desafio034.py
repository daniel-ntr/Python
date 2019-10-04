'''a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}. ')
print(f'O maior valor digitado foi {maior}. ')'''

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
lista =[a, b, c]
lista_ordenada = sorted(lista)
print(f'O menor número é {lista_ordenada[0]}')
print(f'O maior número é {lista_ordenada[2]}')