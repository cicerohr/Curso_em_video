"""12_ex038_comparando_numeros.py em 2018-12-14. Projeto Curso em Video.

Comparando Números

Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Comparando Números')

    print('''\tfrom funcoes import cabecalho, ansi, verificador
    
    n1 = verificador('Digite o 1° número: ')
    n2 = verificador('Digite o 2° número: ')
    if n1 == n2:
        print(f'{ansi("bold", "vermelho")}Não existe valor maior, os dois são iguais.{ansi()}')
    elif n1 > n2:
        print(f'{ansi("azul")}O primeiro valor é maior.{ansi()}')
    elif n1 < n2:
        print(f'{ansi("azul")}O segundo valor é maior.{ansi()}')
    ''')
    n1 = verificador('Digite o 1° número: ')
    n2 = verificador('Digite o 2° número: ')
    if n1 == n2:
        print(f'{ansi("bold", "vermelho")}Não existe valor maior, os dois são iguais.{ansi()}')
    elif n1 > n2:
        print(f'{ansi("azul")}O primeiro valor é maior.{ansi()}')
    elif n1 < n2:
        print(f'{ansi("azul")}O segundo valor é maior.{ansi()}')
