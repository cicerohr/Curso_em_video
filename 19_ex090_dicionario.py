"""19_ex090_dicionario.py em 2018-12-21. Projeto Curso em Video.

Dicionário em Python

Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Dicionário em Python')

    print('''\tficha = dict(nome='', média=0, situação='')
    ficha['nome'] = str(input('Nome: ')).strip().title()
    ficha['média'] = verificador('Média: ', float)
    if ficha['média'] >= 7:
        ficha['situação'] = 'APROVADO'
    elif 5 <= ficha['média'] < 7:
        ficha['situação'] = 'RECUPERAÇÃO'
    else:
        ficha['situação'] = 'REPROVADO'
    print('-=' * 20)
    for k, v in ficha.items():
        print(f'\\t- {k.title()} é igual a {v}.')
    ''')
    ficha = dict(nome='', média=0, situação='')
    ficha['nome'] = str(input('Nome: ')).strip().title()
    ficha['média'] = verificador('Média: ', float)
    if ficha['média'] >= 7:
        ficha['situação'] = 'APROVADO'
    elif 5 <= ficha['média'] < 7:
        ficha['situação'] = 'RECUPERAÇÃO'
    else:
        ficha['situação'] = 'REPROVADO'
    print('-=' * 20)
    for k, v in ficha.items():
        print(f'\t- {k.title()} é igual a {v}.')
