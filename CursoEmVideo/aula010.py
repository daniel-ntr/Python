# ESTRUTURAS Condicionais

'''tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <=3:
    print('Seu carro é novo.')
else:
    print('Seu carro é velho. ')
print('--Fim--')'''

#tempo = int(input('Quantos anos tem o seu carro? '))
#print('carro novo'if tempo <= 3 else 'carro velho')
#print('--Fim--')

'''nome = str(input('Qual é o seu nome? '))
if nome == 'Daniel':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal! ')
print(f'Bom dia, {nome}! ')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}. ')
if m >= 6.0:
    print('Sua média foi boa! Parabéns! ')
else:
    print('Sua média foi ruim! Estude mais! ')

#print('PARABÉNS!' if m>=6 else'ESTUDE MAIS!')