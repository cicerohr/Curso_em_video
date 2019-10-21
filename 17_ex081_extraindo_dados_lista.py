"""17_ex081_extraindo_dados_lista.py em 2018-12-20. Projeto Curso em Video.

Extraindo dados de uma Lista

Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

"""
from funcoes import cabecalho, verificador, questao

if __name__ == '__main__':
    cabecalho('Extraindo dados de uma Lista')

    print('''\tfrom funcoes import cabecalho, verificador, questao
    
    lista = []
    while True:
        lista.append(verificador('Digite um valor: '))
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            lista.sort(reverse=True)
            print('-=' * 20, '\\n', f'Você digitou {len(lista)} elemento{"s" if len(lista) > 1 else ""}.', sep='')
            print(f'Os valores em ordem decrescente são {lista}')
            print(f'O valor 5 {"não " if lista.count(5) < 1 else ""}foi encontrado na lista.')
            break
    ''')
    lista = []
    while True:
        lista.append(verificador('Digite um valor: '))
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            lista.sort(reverse=True)
            print('-=' * 20, '\n', f'Você digitou {len(lista)} elemento{"s" if len(lista) > 1 else ""}.', sep='')
            print(f'Os valores em ordem decrescente são {lista}')
            print(f'O valor 5 {"não " if lista.count(5) < 1 else ""}foi encontrado na lista.')
            break
