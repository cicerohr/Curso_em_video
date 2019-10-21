"""12_ex041_classificando_atletas.py em 2018-12-14. Projeto Curso em Video.

Classificando Atletas

A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER

"""
from datetime import date
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Classificando Atletas')

    print('''\tfrom datetime import date
    from funcoes import cabecalho, verificador
    
    nascimento = verificador('Ano de nascimento: ')
    ano_hoje = date.today().year
    idade = ano_hoje - nascimento
    print(f'O atleta tem {idade} anos.')
    if idade > 25:
        print('Classificação: MASTER')
    elif 19 < idade <= 25:
        print('Classificação: SÊNIOR')
    elif 14 < idade <= 19:
        print('Classificação: JÚNIOR')
    elif 9 < idade <= 14:
        print('Classificação: INFANTIL')
    else:
        print('Classificação: MIRIM')
    ''')
    nascimento = verificador('Ano de nascimento: ')
    ano_hoje = date.today().year
    idade = ano_hoje - nascimento
    print(f'O atleta tem {idade} anos.')
    if idade > 25:
        print('Classificação: MASTER')
    elif 19 < idade <= 25:
        print('Classificação: SÊNIOR')
    elif 14 < idade <= 19:
        print('Classificação: JÚNIOR')
    elif 9 < idade <= 14:
        print('Classificação: INFANTIL')
    else:
        print('Classificação: MIRIM')
