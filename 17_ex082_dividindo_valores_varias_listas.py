"""17_ex082_dividindo_valores_varias_listas.py em 2018-12-20. Projeto Curso em Video.

Dividindo valores em várias listas

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.

"""
from funcoes import cabecalho, verificador, questao

if __name__ == '__main__':
    cabecalho('Dividindo valores em várias listas')

    print('''\tfrom funcoes import cabecalho, verificador, questao
    
    lista = []
    pares = []
    impares = []
    while True:
        numero = verificador('Digite um valor: ')
        lista.append(numero)
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            print('-=' * 20, '\\n', f'A lista completa é {lista}', sep='')
            print(f'A lista de par{"es" if len(pares) > 1 else ""} é {pares}')
            print(f'A lista de ímpar{"es" if len(impares) > 1 else ""} é {impares}.')
            break
    ''')
    lista = []
    pares = []
    impares = []
    while True:
        numero = verificador('Digite um valor: ')
        lista.append(numero)
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            print('-=' * 20, '\n', f'A lista completa é {lista}', sep='')
            print(f'A lista de par{"es" if len(pares) > 1 else ""} é {pares}')
            print(f'A lista de ímpar{"es" if len(impares) > 1 else ""} é {impares}.')
            break
