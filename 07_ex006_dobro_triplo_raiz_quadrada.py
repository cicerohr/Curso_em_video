"""07_ex006_dobro_triplo_raiz_quadrada.py em 2018-12-10. Projeto Curso em Video.

Dobro, Triplo, Raiz Quadrada

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

"""
from math import sqrt
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Dobro, Triplo, Raiz Quadrada')

    print('''\tfrom math import sqrt
    
    n = int(input("Digite um número: "))
    print(f'O dobro de {n} é {n * 2}.')
    print(f'O triplo de {n} é {n * 3}')
    print(f'A raiz quadrada de {n} é {sqrt(n):.2f}')
        Obs.: a raiz quadrada também pode ser obtida pela exponenciação. 
              Ex.: n ** (1/2) => 81 ** (1/2) = 9
                                ou
                   pow(n, (1/2)) => pow(81, (1/2)) = 9
    ''')
    n = int(input("Digite um número: "))
    print(f'O dobro de {n} é {n * 2}.')
    print(f'O triplo de {n} é {n * 3}')
    print(f'A raiz quadrada de {n} é {sqrt(n):.2f}')
