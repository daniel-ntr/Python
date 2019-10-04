from time import sleep
numero1 = float(input('Primeiro valor: '))
numero2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>Digite sua opção: '))
    if opcao == 1:
        soma = numero1 + numero2
        print(f'A soma entre {numero1} + {numero2} é igual a: {soma}')
    elif opcao == 2:
        produto = numero1 * numero2
        print(f'O produto entre {numero1} X {numero2} é igual a: {produto}')
    elif opcao == 3:
        if numero1 > numero2:
            print(f'{numero1} é o maior número')
        elif numero2 > numero1:
            print(f'{numero2} é o maior número')
        else:
            print(f'Os números {numero1} e {numero2} são iguais')
    elif opcao == 4:
        print('Informe os números novamente: ')
        numero1 = float(input('Primeiro valor: '))
        numero2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando Programa...')
    else:
        print('Digite uma opção válida.')
    print('=-=' * 10)
    sleep(1)
print('Programa Finalizado.')