# Cores no texto
print('\033[1;31;43mOlá, mundo! ')
print('\033[30;46mOlá, mundo!\033[m ')
print('\033[4;33;42mOlá, Brasil!\033[m ')
print('\033[7;30mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m ')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{5}\033[m. ')
nome = 'Daniel'
print(f'Olá! Muito prazer em te conhecer, \033[4;34m{nome}\033[m!!!')

# OUTRA FORMA DE APLICAR CORES
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'pretoebranco':'\033[7;30m'}
print(f'Olá! Prazer em te conhecer, {cores["amarelo"]}{nome}{cores["limpa"]}!!! ')
