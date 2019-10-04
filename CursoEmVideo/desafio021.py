from random import shuffle
a1 = str(input('Digite um primeiro aluno para sortear: '))
a2 = str(input('Digite um segundo aluno para sortear: '))
a3 = str(input('Digite um terceiro aluno para sortear: '))
a4 = str(input('Digite um quarto aluno para sortear: '))
ordem = [a1, a2, a3, a4]
shuffle(ordem)
print(f'Ordem de apresentação: {ordem}')
