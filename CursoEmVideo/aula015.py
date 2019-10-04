# Interropendo repetições While

s = n = 0
while True: #loop infinito
    n = int(input('Digite um número: '))
    if n == 999:
        break # FORÇA A SAÍDA DO WHILE CONFORME A CONDIÇÃO DO IF
    s += n
print(f'A soma vale {s}')