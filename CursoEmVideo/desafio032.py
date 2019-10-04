distancia = float(input('Informe a distância da viagem: '))
print(f'Voçê está preste a começar uma viagem de {distancia}km')
preco = distancia * 0.5 if distancia < 200 else distancia * 0.45
print(f'O preço da passagem será {preco}R$. ')

'''distancia = float(input('Informe a distância da viagem: '))
print(f'Voçê está preste a começar uma viagem de {distancia}km')
    if distancia <= 200.0:
    print(f'Sua passagem custará: {distancia * 0.50:.2f} R$. ')
else:
    print(f'Sua passagem custará: {distancia * 0.45:.2f} R$ no preço promocional. ')
print('--FIM--')'''


