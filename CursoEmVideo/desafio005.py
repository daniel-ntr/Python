n = input('Digite algo: ')
cores = {'limpa':'\033[m', 'verde':'\033[32m'}
print('O tipo primivito desse valor é:', type(n))
print('Está em maiúsculo? ', n.isupper())
print('É alfanumérico? ', n.isalnum())
print('É alfabético? ', n.isalpha())
print('É ASCII? ', n.isascii())
print('É decimal? ', n.isdecimal())
print('É dígito? ', n.isdigit())
print('É um identificador? ', n.isidentifier())
print('Está em minúsculo? ', n.islower())
print('É numérico?' ,n.isnumeric())
print('É printável?', n.isprintable())
print('Só tem espaços?', n.isspace())
print('Está capitalizada?', n.istitle())


