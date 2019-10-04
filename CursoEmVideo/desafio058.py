sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite M para masculino ou F para femino: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')