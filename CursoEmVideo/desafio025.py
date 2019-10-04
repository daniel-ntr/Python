'''cidade = str(input('Digite o nome de sua cidade: ')).strip().split().casefold()
if 'Santo' == cidade[0]:
    print('Sua cidade  começa com Santo!')
else:
    print('Sua cidade não começa com Santo! ')'''

cidade = str(input('Digite o nome de sua cidade: ')).strip().casefold().split()
print(f'Essa cidade começa com Santo? {"santo" == cidade[0]} ')
