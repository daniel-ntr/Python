# PROGRESSÃO ARITMÉTICA - EXIBA OS 10 PRIMEIROS TERMOS DE UMA RAZÃO.
primeiroTermo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
decimo = primeiroTermo + (10 - 1) * razao
for progressaoAritmetica in range(primeiroTermo, decimo + razao, razao):
    print(f'{progressaoAritmetica}', end=' → ')
print('FIM')
