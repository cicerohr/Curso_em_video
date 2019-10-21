"""10_ex032_ano_bissexto.py em 2018-12-13. Projeto Curso em Video.

Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

Calendário Gregoriano:

1. De 4 em 4 anos é ano bissexto.
2. De 100 em 100 anos não é ano bissexto.
3. De 400 em 400 anos é ano bissexto.
4. Prevalecem as últimas regras sobre as primeiras.

Fonte: https://pt.wikipedia.org/wiki/Ano_bissexto#Calendário_Gregoriano

"""
from datetime import datetime
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Ano Bissexto')

    print('''\tfrom datetime import datetime
    from cicero import cabecalho, verificador
    
    ano = verificador('Que ano você quer analisar? [0 analisa o ano atual] ')
    if ano == 0:
        ano = datetime.today().year
    print(f'O ano {ano}', end=' ')
    if ano % 400 == 0:
        print('é BISSEXTO.')
    elif ano % 100 == 0:
        print('NÃO é BISSEXTO.')
    elif ano % 4 == 0:
        print('é BISSEXTO.')
    else:
        print('NÃO é BISSEXTO.')
    ''')
    ano = verificador('Que ano você quer analisar? [0 analisa o ano atual] ')
    if ano == 0:
        ano = datetime.today().year
    print(f'O ano {ano}', end=' ')
    # Alternativa de código (mais elegante)
    # if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    #     print('é BISSEXTO.')
    # else:
    #     print('NÃO é BISSEXTO.')
    if ano % 400 == 0:
        print('é BISSEXTO.')
    elif ano % 100 == 0:
        print('NÃO é BISSEXTO.')
    elif ano % 4 == 0:
        print('é BISSEXTO.')
    else:
        print('NÃO é BISSEXTO.')
