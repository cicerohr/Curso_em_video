"""10_ex030_par_impar.py em 2018-12-13. Projeto Curso em Video.

Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Par ou Ímpar?')

    print("""\tfrom cicero import cabecalho, verificador
    
    numero = verificador(f'{ansi("bold", "magenta")}Diga-me um número qualquer: {ansi()}')
    print(f'O número {numero} é {ansi("bold", "azul")}', end='')
    if numero % 2 == 0:
        print(f'PAR{ansi()}.')
    else:
        print(f'ÍMPAR{ansi()}.')
    """)
    numero = verificador(f'{ansi("bold", "magenta")}Diga-me um número qualquer: {ansi()}')
    print(f'O número {numero} é {ansi("bold", "azul")}', end='')
    if numero % 2 == 0:
        print(f'PAR{ansi()}.')
    else:
        print(f'ÍMPAR{ansi()}.')
