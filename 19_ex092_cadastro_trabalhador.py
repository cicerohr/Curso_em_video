"""19_ex092_cadastro_trabalhador.py em 2018-12-22. Projeto Curso em Video.

Cadastro de Trabalhador em Python

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

"""
from datetime import date
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Cadastro de Trabalhador em Python')

    print('''\tfrom datetime import date
    from funcoes import cabecalho, verificador
    
    cadastro = dict()
    cadastro['nome'] = str(input('Nome: ')).strip().title()
    ano = verificador('Ano de nascimento: ')
    cadastro['idade'] = date.today().year - ano
    cadastro['ctps'] = verificador('Carteira de trabalho (0 não tem): ')
    if cadastro['ctps'] != 0:
        cadastro['contratação'] = verificador('Ano de contratação: ')
        cadastro['salário'] = verificador('Salário: ', float)
        cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - ano
    print('-=' * 30)
    for k, v in cadastro.items():
        print(f'\\t- {k} tem o valor {v}.')
    ''')
    cadastro = dict()
    cadastro['nome'] = str(input('Nome: ')).strip().title()
    ano = verificador('Ano de nascimento: ')
    cadastro['idade'] = date.today().year - ano
    cadastro['ctps'] = verificador('Carteira de trabalho (0 não tem): ')
    if cadastro['ctps'] != 0:
        cadastro['contratação'] = verificador('Ano de contratação: ')
        cadastro['salário'] = verificador('Salário: ', float)
        cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - ano
    print('-=' * 30)
    for k, v in cadastro.items():
        print(f'\t- {k} tem o valor {v}.')
