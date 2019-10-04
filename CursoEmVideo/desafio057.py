soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0
for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')
    nome = str(input('Digite seu nome: ').strip())
    idade = int(input('Digite sua idade: ').strip())
    sexo = str(input('Sexo [M/F]: ').strip())
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1
media_idade = soma_idade / pessoa
print('Análise dos Dados: ')
print(f'A média de idade do grupo é {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e seu nome é {nome_velho}.')
print(f'Ao todo {total_mulher_20} mulher(es) tem menos de 20 anos.')