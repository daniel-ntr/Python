dias = int(input('Quantos dias o carro permaneceu alugado? '))
km = float(input('Quantos quilômetros o carro percorreu? '))
aluguel = (dias * 60) + (km * 0.15)
print(f'Custo do aluguel: R${aluguel}')

