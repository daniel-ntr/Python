n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'{n1} é maior do que {n2}. ')
elif n1 < n2:
    print(f'{n2} é maior de que {n1}. ')
else:
    print('Não há valor maior. Os dois são iguais. ')