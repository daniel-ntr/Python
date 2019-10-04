# Leia 7 anos de nascimento e determine quantas pessoas são maiores e menores de idade.
from datetime import date
ano_atual = date.today().year
grupo_maiores = 0
grupo_menores = 0
for pessoas in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {pessoas}ª pessoa: '))
    idade = ano_atual - nascimento
    if idade >= 21:
        grupo_maiores += 1
    else:
        grupo_menores += 1
print('\nRESULTADO DOS DADOS INFORMADOS: ')
print(f'{grupo_menores} pessoas são menores de idade. \n{grupo_maiores} pessoas são maiores de idade. ')
