peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / altura ** 2
print('''\n--- Tabela de IMC ---
[Abaixo de 18.5: Abaixo do peso]
[Entre 18.5 e 25: Peso ideal]
[25 até 30: Sobrepeso]
[30 até 40: Obesidade]
[Acima de 40: Obesidade mórbida]\n''')
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Vocês está abaixo do peso normal. ')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está no peso ideal. ')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está em sobrepeso. ')
elif 29 <= imc < 40:
    print(f' Seu IMC é {imc:.1f}. Você está em obesidade. ')
elif imc > 40:
    print(f' Seu IMC é {imc:.1f}. Voçês está em obesidade mórbida. ')
print('---FIM---')