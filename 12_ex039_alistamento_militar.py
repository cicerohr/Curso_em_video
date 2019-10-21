"""12_ex039_alistamento_militar.py em 2018-12-14. Projeto Curso em Video.

Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
from datetime import date
from funcoes import cabecalho, verificador, ansi

if __name__ == '__main__':
    cabecalho('Alistamento Militar')

    print('''\tfrom datetime import date
    from cicero import cabecalho, verificador, ansi
    
    nascimento = verificador('Ano de nascimento: ')
    ano_hoje = date.today().year
    idade = ano_hoje - nascimento
    print(f'Quem nasceu no ano de {nascimento} tem {idade} anos em {ano_hoje}.')
    if idade < 18:
        print(f'Ainda falta(m) {18 - idade} ano(s) para o alistamento.')
        print(f'Seu alistamento foi em {ano_hoje - (idade - 18)}.')
    elif idade > 18:
        print(f'Você deveria ter se alistado há {idade - 18} ano(s).')
        print(f'Seu alistamento foi em {ano_hoje - (idade - 18)}.')
    else:
        print(f'Você tem que se alistar {ansi("bold", "vermelho")}IMEDIATAMENTE{ansi()}!')
    ''')
    nascimento = verificador('Ano de nascimento: ')
    ano_hoje = date.today().year
    idade = ano_hoje - nascimento
    print(f'Quem nasceu no ano de {nascimento} tem {idade} anos em {ano_hoje}.')
    if idade < 18:
        print(f'Ainda falta(m) {18 - idade} ano(s) para o alistamento.')
        print(f'Seu alistamento foi em {ano_hoje - (idade - 18)}.')
    elif idade > 18:
        print(f'Você deveria ter se alistado há {idade - 18} ano(s).')
        print(f'Seu alistamento foi em {ano_hoje - (idade - 18)}.')
    else:
        print(f'Você tem que se alistar {ansi("bold", "vermelho")}IMEDIATAMENTE{ansi()}!')
