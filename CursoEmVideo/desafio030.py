velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de 80Km/h. \nSua multa será de {multa:.2f} R$. ')
print('Tenha um bom dia! Diriga com segurança.')
