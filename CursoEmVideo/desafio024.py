
#Solução matemática
'''numero = int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')'''

#Solução com String
num = str(input('Digite um número de 0 até 9999: ')).zfill(4)
print(f'Unidade: {num[3]}. ')
print(f'Dezena: {num[2]}.')
print(f'Centena: {num[1]}. ')
print(f'Milhara: {num[0]}. ')


"""num = '000' + str(input('Digite um número entre 0 e 9999: '))
print(f'Unidade: {num[-1]}. ')
print(f'Dezena: {num[-2]}. ')
print(f'Centena: {num[-3]}. ')
print(f'Milhar: {num[-4]}. ')"""


#n = str(num)  # n Transforma o valor inputado em string

