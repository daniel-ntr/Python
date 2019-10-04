#Sequência de Fibonacci
anterior_1 = 0
anterior_2 = 1
contador = 3
print('-=' * 12)
print('Sequência de Fibonacci')
print('-=' * 12)
quantidade_termos = int(input('Quantos termos deseja mostrar? '))
print(anterior_1, end=' -> ')
print(anterior_2, end=' -> ')
while contador <= quantidade_termos:
    contador += 1
    proximo = anterior_1 + anterior_2
    anterior_1 = anterior_2
    anterior_2 = proximo
    print(proximo, end=' -> ')
print('FIM')