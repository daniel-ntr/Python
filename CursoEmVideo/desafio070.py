# Análise de Dados de Cadastro
total_maiores = total_homens = mulheres_menos20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: ').strip())
    sexo = ' ' # VARIÁEL PRECISA ESTAR FORA DAS ESTRUTURAS MAIS INTERNAS PARA QUE POSSA SER RESETADOR E RECEBER UM NOVO INPUT
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            total_homens += 1
        if sexo == 'F' and idade < 20:
            mulheres_menos20 += 1
        if idade >= 18:
            total_maiores += 1
    continuar = ' ' # VARIÁEL PRECISA ESTAR FORA DAS ESTRUTURAS MAIS INTERNAS PARA QUE POSSA SER RESETADOR E RECEBER UM NOVO INPUT
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('========= FIM DO PROGRAMA ===========')
print(f' Total de pessoas maiores de idade: {total_maiores}')
print(f' Ao todo temos {total_homens} homens cadastrados')
print(f' E temos {mulheres_menos20} mulher(es) com menos de 20 anos')
