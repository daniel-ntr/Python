# TUPLAS (SÃO IMUTÁVEIS DURANTE A EXECUÇÃO)

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(len(lanche))
print('\n')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('\n')

for pos, comida in enumerate(lanche):  # Enumerate retorna tanto o dado quanto a posição
    print(f'Eu vou comer {comida} na posição {pos}')
print('\n')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('\n')
print('Comi pra caramba!')
print(lanche[-1])
print(lanche[:2])
print(lanche[-2:])
print(lanche[::])
print(lanche[1])
print(sorted(lanche))
print('\n')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
d = a + b
print(c)
print(d)
print(len(c))
print(len(d))
print(c.count(5))  # Quantas vezes o 5 aparece em c
print(c.index(8))  # Retorna a posição do número 8
print(c.index(5, 1))  # Retorna a posição de 5 depois da posição 1
print('\n')

pessoa = ('Gustavo', 39, 'M', 99.98)  # Tuplas aceitam  dados de tipos diferentes
print(pessoa)
del(pessoa)  # Apaga a tupla.