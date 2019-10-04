#Empréstimo

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salário: '))
tempo = int(input('Em quantos anos deseja quitar a casa? '))
tempo = tempo * 12
prestacao = valor_casa / tempo
if prestacao > salario * 1.3:
   print('Infelizmente você não pode financiar essa casa. ')
else:
    print('Parabéns! Seu empréstimo foi aprovado! ')
print(f'Valor da prestação: R${prestacao:.2f} em {tempo} vezes. ')
