sal = float(input('Digite o seu salário: '))
if sal <= 1250.00:
    print(f'Seu novo salário será: R${sal*1.15}. ')
else:
    print(f'Seu novo salário será: R${sal*1.1}. ')