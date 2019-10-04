# Analise de Dados de Compra
total_produtos = total_compra = menor_preco = maior_preco = preco_maior_mil = 0
produto_barato = ''
print('-'*35)
print('       LOJAS XIMIRA E PEIXOLA')
print('-'*35)

while True:
    nome_produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$').strip())
    total_compra += preco
    total_produtos += 1

    if preco > 1000:
        preco_maior_mil += 1
    if total_produtos == 1 or preco < menor_preco:
        maior_preco = menor_preco = preco
        produto_barato = nome_produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total_compra:.2f}')
print(f'Temos {preco_maior_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${menor_preco:.2f}')
