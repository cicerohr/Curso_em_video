"""07_ex005_antecessor_sucessor.py em 2018-12-10. Projeto Curso em Video.

Antecessor e Sucessor

Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Antecessor e Sucessor')

    print('''\tn = int(input("Digite um número: "))
    print(f'Analisando o valor {n}; seu antecessor é {n - 1} e o sucessor é {n + 1}')
    ''')
    n = int(input("Digite um número: "))
    print(f'Analisando o valor {n}; seu antecessor é {n - 1} e o sucessor é {n + 1}')
