print('-='*20)
print('Conversor de base numérica')
print('-='*20)
n = int(input('\nDigite um número inteiro: '))
print('''Agora, escolha uma das bases para conversão abaixo:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Insira uma opção: '))
if escolha == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif escolha == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif escolha == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente. ')