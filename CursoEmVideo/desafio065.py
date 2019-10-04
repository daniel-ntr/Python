soma = contador = n = 0
while n != 999:
    n = float(input('Digite um número ou 999 para sair: '))
    if n != 999:
        soma += n
        contador += 1
print(f'{contador} números foram digitados e a soma entre eles é: {soma:.1f}')