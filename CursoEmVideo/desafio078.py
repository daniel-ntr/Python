# CONTANDO VOGAIS EM TUPLA

palavras = ('programar', 'linguagem', 'python', 'programador', 'futuro', 'trabalhar',
            'curso', 'mercado', 'estudar', 'praticar', 'aprender', 'curso', 'gratis')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')