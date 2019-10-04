# ESTRUTURA EM LAÇOS/REPETIÇÃO e ITERAÇÕES
'''for i in range(0, 6):  # REPETE OS PRINTS 6 VEZES
    print('Oi')
print('FIM')

for c in range(7, 0, -1):  # CONTA DE TRÁS PRA FRENTE
    print(c)

for c in range(0, 7, 2):  # CONTA ATÉ 7 DE 2 EM DOIS
    print(c)

n = int(input('Digite um número: ')) # CONTA DE ACORDO COM A VARIAVEL N INPUTADA PELO USUARIO
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('INÍCIO: '))
f = int(input(('FIM: ')))
p = int(input('PASSO: '))

for c in range(i, f+1, p): # pode-se customizar as iterações com variáveis
    print(c)
print('FIM')'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # equivalente à s = s + n
print(f'O SOMATÓRIO DE TODOS OS VALORES FOI {s}')
