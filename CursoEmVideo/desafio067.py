cont = soma = 0
while True:
    usuario = float(input('Digite um valor (999 para parar): '))
    if usuario == 999:
        break
    cont += 1
    soma += usuario
print(f'A soma dos valores é {soma}. Foram lidos {cont} números.')