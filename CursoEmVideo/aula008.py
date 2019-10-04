# Importação de blibliotecas e utilização de  módulos
# math.ceil -> arredonda um número para cima
# math.floor -> arredonda um número para baixo
# math.trunc -> elimina os números depois da vírgula
# math.pow -> potencia
# math.sqrt -> raiz quadrada
# math.factorial -> fatorar número
import math  # importa a biblioteca math por inteiro

n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print(f'A raiz de {n} é \033[31m{math.ceil(raiz)}\033[m. ')

#Importa métodos específicos de uma biblioteca. Exemplo abaixo de sqrt e ceil

#from math import sqrt, ceil
#n = int(input('Digite um número: '))
#raiz = sqrt(n)
#print(f'A raiz de {n} é {ceil(n)}. ')