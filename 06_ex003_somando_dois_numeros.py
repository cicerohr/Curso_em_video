"""06_ex003_somando_dois_numeros.py em 2018-12-10. Projeto Curso em Video.

Somando dois números

Crie um programa que leia dois números e mostre a soma entre eles.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Somando dois números')

    print('''\tv1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))
    print(f'A soma entre {v1} e {v2} é  igual a {v1 + v2}.')
    ''')
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))
    print(f'A soma entre {v1} e {v2} é igual a {v1 + v2}.')
