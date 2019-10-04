from datetime import date
sexoPergunta = str(input('Qual o seu sexo? Digite M para masculino e F para feminino: ').strip().casefold())
sexo = ['m', 'f']
if sexoPergunta == sexo[1]:
    print(f'Você é do sexo Feminino. O alistamento obrigatório não se aplica.')
elif sexoPergunta == sexo[0]:
    nascimento = int(input('Digite seu ano de nascimento: '))
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    if idade == 18:
        print(f'Você completou {idade} anos. Apresente-se para alistamento imediatamente. ')
    elif idade < 18:
        saldo = 18 - idade
        ano = anoAtual + saldo
        print(f'Você  tem apenas {idade} anos. Faltam {saldo} ano(s) para se apresentar. ')
        print(f'Seu alistamento será em {ano}. ')
    else:
        saldo = idade - 18
        ano = anoAtual - saldo
        print(f'Você tem {idade} anos. O prazo para alistamento se excedeu em {saldo} ano(s). ')
        print(f'Seu alistamento foi em {ano}.')
else:
    print('Opção de sexo inválida. Tente novamente.')



