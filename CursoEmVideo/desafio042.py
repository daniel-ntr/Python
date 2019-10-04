from datetime import date
ano = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano - nascimento
if idade <= 9:
    print(f'Você tem {idade} anos. Sua categoria é MIRIM. ')
elif idade <= 14:
    print(f'Você tem {idade} anos. Sua categoria é INFANTIL. ')
elif idade <= 19:
    print(f'Você tem {idade} anos. Sua categoria é JUNIOR. ')
elif idade <= 25:
    print(f'Você tem {idade} anos. Sua categoria é SENIOR. ')
else:
    print(f'Você tem {idade} anos. Sua categoria é MASTER. ')


