# ANÁLISE DE DADOS NUMÉRICOS
encerrar_programa = False
maior = menor = contador = media = soma = 0.0

while not encerrar_programa:
    n = float(input('Digite um número: '))
    contador += 1
    soma += n
    media = soma / contador

    continuar_programa = ' '
    while continuar_programa not in 'SN':
        continuar_programa = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if contador == 1:
            maior = menor = n
            iguais = 'Todos os números que digitou são iguais'
        if continuar_programa in 'S':
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        if continuar_programa in 'N':
            encerrar_programa = True

print('\nPrograma finalizado com sucesso!')
print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'{iguais}' if maior == menor == n else f'O maior número foi {maior:.0f} e o menor foi {menor:.0f}')