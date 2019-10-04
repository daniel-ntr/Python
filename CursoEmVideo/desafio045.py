produto = (float(input('Informe o valor do produto: R$ ').strip()))
print('''\n --- Formas de pagamento --- 
[ 1 ] - À vista Dinheiro ou Cheque: 10% de desconto.
[ 2 ] - À vista no cartão: 5% de desconto.
[ 3 ] - Até 2x no cartão: Sem desconto.
[ 4 ] - 3 x ou mais no cartão: 20% de juros. ''')
opcao = (str(input('\n Selecione uma das opções acima: ').strip()))
if opcao == '1':
    dc = produto * 0.9
    print(f'Valor a pagar: R${dc:.2f}. DESCONTO DE 10% APLICADO. ')
elif opcao == '2':
    cartaov = produto * 0.95
    print(f'Valor a pagar: R${cartaov:.2f}. DESCONTO DE 5% APLICADO. ')
elif opcao == '3':
    cartaop2 = produto / 2
    print(f'Valor a pagar: 2 x de R${cartaop2:.2f}. SEM DESCONTO. ')
elif opcao == '4':
    parcelas = int(input('Quantas parcelas? '))
    cartaop3 = produto * 1.20
    print(f'Sua compra será parcelada em {parcelas}x de R${cartaop3/parcelas}. Valor Total: R${cartaop3:.2f}. JUROS DE 20% APLICADO. ')
else:
    print('Opção de pagamento inválida!')
