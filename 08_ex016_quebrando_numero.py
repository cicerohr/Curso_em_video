"""08_ex016_quebrando_numero.py em 2018-12-10. Projeto Curso em Video.

Quebrando um número

Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

"""
from math import floor, trunc
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Quebrando um número')

    print('''\tfrom math import floor, trunc
    
    n = verificador(f'Digite um número: ', float)
    print(f'O valor digitado foi {n} e a sua porção inteira é {floor(n)}.')
    print(f'O valor digitado foi {n} e a sua porção inteira é {trunc(n)}.')
    print(f'O valor digitado foi {n} e a sua porção inteira é {int(n)}.')
    ''')
    n = verificador(f'Digite um número: ', float)
    print(f'O valor digitado foi {n} e a sua porção inteira é {floor(n)}.')
    print(f'O valor digitado foi {n} e a sua porção inteira é {trunc(n)}.')
    print(f'O valor digitado foi {n} e a sua porção inteira é {int(n)}.')
