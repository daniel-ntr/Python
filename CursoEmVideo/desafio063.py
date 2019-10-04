#DESAFIO 62 REFEITO UTILIZANDO DANDO OPÇÃO DE CALCULAR MAIS TERMOS DE ACORDO COM INPUT
print('Gerador de P.A')
print('-=' * 10)
primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
cont = 1
adicionar = 10
total = 0
while adicionar != 0:
    total += adicionar
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA.\n')
    adicionar = int(input('''Para calcular mais termos, informe o quantidade desejada. 
Ou para sair do programa digite 0: '''))
print(f'{total} de termos exibidos. FIM DO PROGRAMA')



#print('Gerador de P.A')
#print('-=' * 10)
#opcao = 0
#primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
#razao = int(input('Digite a razão: '))
#termo = primeiro_termo
#cont = 1
#while cont <= 11:
#    print(f'{termo} -> ', end='')
#    termo += razao
#    cont += 1
#    if cont == 11:
#        print('FIM.\n')
#        opcao = int(input('''Para calcular mais termos, informe o quantidade desejada.
#Ou para sair do programa digite 0: '''))
#        cont -= opcao
#print(f'FIM  PROGRAMA')


