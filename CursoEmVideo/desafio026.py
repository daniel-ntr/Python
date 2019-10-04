'''nome = str(input('Digite seu nome: '))
if 'Silva' in nome:
    print('Você tem Silva no nome: ')
else:
    print('Você não tem Silva no nome: ')'''
nome = str(input('Digite seu nome completo: ')).strip().casefold().split()
print(f'Você tem Silva no nome? {"silva" in nome[:]}. ')

