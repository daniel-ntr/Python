extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
            'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
            'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: ').strip())
while not -1 < num < 21:
    num = int(input(('Tente novamente. Digite um número entre 0 e 20: ')))
print(f'Você digitou o número {extenso[num]}')
