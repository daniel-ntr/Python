frase = str(input('Digite uma frase qualquer: ')).strip().casefold().split()
frase = ''.join(frase)
print(f'A letra A aparece {frase.count("a")} vezes. ')
print(f'A letra A aparece pela primeira vez na posição {frase.find("a") + 1}. ')
print(f'A letra A aparece pela última vez na posição {frase.rfind("a") + 1}. ')