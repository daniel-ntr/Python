#DESAFIO 52 REFEITO UTILIZANDO WHILE
print('Gerador de P.A')
print('-=' * 10)
primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')
