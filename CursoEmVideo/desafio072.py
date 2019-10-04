# CONTAGEM DE CÉDULAS DE UM CAIXA ELETRÔNICO
print('=' * 30)
print('{:^30}'.format('BANCO RODILINDO'))
print('=' * 30)
notas_disponiveis = [50, 20, 10, 1]
ponteiro = 0
valor_saque = int(input('Qual valor deseja sacar? R$'))
while valor_saque > 0:
    quant_cedulas = valor_saque // notas_disponiveis[ponteiro]
    valor_saque -= quant_cedulas * notas_disponiveis[ponteiro]
    if quant_cedulas > 0:
        print(f'Total de {quant_cedulas} cédulas de R${notas_disponiveis[ponteiro]}')
    ponteiro += 1
print('=' * 30)
print('Volte sempre ao BANCO RODILINDO! Tenha um bom dia!')


'''print('=' * 30)
print('{:^30}'.format('BANCO RODILINDO'))
print('=' * 30)
saque = int(input('Quanto deseja sacar? R$'))
divida = saque
cedula = 50
total_cedula = 0
while True:
    if divida >= cedula:
        divida -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if divida == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO RODILINDO! Tenha um bom dia!')'''