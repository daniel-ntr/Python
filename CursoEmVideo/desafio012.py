print('Calculadora de tinta. ')
l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = l*h
print(f'Sua parede tem a dimensão de {l} x {h} e sua área é de {a:.1f}m². ')
print(f'Você precisará de {a/2:.1f}l de tinta para pintar a parede. ')