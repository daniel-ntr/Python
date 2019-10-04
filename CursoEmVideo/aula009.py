# Manipulando Strings
# Fatiamento de Strings

#  0   1   2   3   4   5  6   7  8   9  10  11  12  13  14 15  16  17  18  19  20
# [C] [u] [r] [s] [o] [] [e] [m] [] [V] [í] [d] [e] [o] [] [P] [y] [t] [h] [o] [n]

# frase[9] Retorna o 9 caracter da string.
# frase[9:13] Retorna do 9 ao 12*** caracter.
# frase[9:21] Retorna do 9 até 21. Onde o 21 não existe. Como o python ignora o ultimo, o resultado fica de 9:20.
# frase[9:21:2] Retorna de 9 ao 21 pulando de dois em dois.
# frase[:5] Retorna do início até 5.
# frase[15:] Retorna de 15 até o último.
# frase[9::3] Retorna de 9 até o final, pulando de 3 em 3.

# Análise de Strings

# len(frase) Retorna a length (quantidade de caracteres) do string.
# frase.count('o') Retorna a quantidade de vezes que o caracter 'o' minúsculo aparece.
# frase.count('o',0,13) Retorna a quantidade de 'o'de 0 à 13.
# frase.find('deo') Retorna onde 'deo' começou. No 11!
# frase.find('Android') Retorna -1. Não encontrado!
# 'Curso' in frase Retorna True. Existe 'Curso' na frase!

# Transformação
# Strings são na sua essência imutáveis. O Python utilizada métodos() para modificar de forma indireta.

# frase.replace('Python', 'Android') Substitui Python por Android. O Python adiciona o vetor 22 automaticamente.
# frase.upper() Retorna toda a string em maiúsculo. *O que já estava em maiúsculo é mantido.
# frase.lower() Retorna toda a string em minúsculo. *O que já estava em maiúsculo é mantido.
# frase.capitalize() Retorna a string inteira com apenas a primeira letra em maiúsculo.
# frase.title() Retorna frase por frase com cada inicial em maíusculo.

# 0  1   2  3   4   5   6   7   8   9  10  11 12  13  14  15  16  17 18
# [] [] [] [A] [p] [r] [e] [n] [d] [a] [] [P] [y] [t] [h] [o] [n] [] []

# frase.strip() Remove os espaços nas extremidades da string.
# frase.rstrip() Remove os espaços à direita da string.
# frase.lstrip() Remove os espaços à esquerda da string.

# Divisão de Strings

#  0   1   2   3   4   5  6   7  8   9  10  11  12  13  14 15  16  17  18  19  20
# [C] [u] [r] [s] [o] [] [e] [m] [] [V] [í] [d] [e] [o] [] [P] [y] [t] [h] [o] [n]

# frase.split() Divide a string considerando os espaços, ou seja, gera uma lista com todas as palavras de uma string.
#         0   1   2   3   4    0   1    0   1   2   3   4    0  1   2    3   4   5
# Retorna [C] [u] [r] [s] [o] [e] [m]  [V] [í] [d] [e] [o]  [P] [y] [t] [h] [o] [n]
# '-'.join(frase) Junta a lista usando o caracter '-'. Retorna [Curso-em-Vídeo-Python]

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print("""Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos,
e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos
e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, 
como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. 
Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, 
e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.""")
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase[0])
#  frase[0] = 'J'  # Vai dar erro. String é imutável. Use replace.
frase = frase.replace('Python', 'Android')
print('Python' in frase)
print(frase.title().find('Android'))
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])
