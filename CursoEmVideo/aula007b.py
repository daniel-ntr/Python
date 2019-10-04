n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# formatação de números // :."x"f = limita quantidade em "x" vezes de digitos após o ponto // end='' = não quebra linha /// \n = nova linha
print(f'A soma é: \033[32m{s}\033[m \nO produto é: \033[31m{m}\033[m \nA divisão é \033[34m{d:.3f}\033[m.', end=' ')
print(f'A divisão inteira é \033[35m{di:.2f}\033[m e a potência \033[36m{e}\033[m.')
