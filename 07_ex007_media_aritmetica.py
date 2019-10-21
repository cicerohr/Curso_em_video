"""07_ex007_media_aritmetica.py em 2018-12-10. Projeto Curso em Video.

Média Aritmética

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Média Aritmética')

    print('''\tn1 = float(input('1ª nota: '))
    n2 = float(input('2ª nota: '))
    m = (n1 + n2) / 2
    print(f'A média entre {n1} e {n2} é {m}.')
    ''')
    n1 = float(input('1ª nota: '))
    n2 = float(input('2ª nota: '))
    m = (n1 + n2) / 2
    print(f'A média entre {n1} e {n2} é {m}.')
