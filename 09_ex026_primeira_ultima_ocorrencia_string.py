"""09_ex026_primeira_ultima_ocorrencia_string.py em 2018-12-12. Projeto Curso em Video.

Primeira e última ocorrência de uma string

Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Primeira e última ocorrência de uma string')

    print('''\tfrase = str(input('Digite uma frase: ')).strip().lower()
    print(f'A letra "A" aparece {frase.count("a")} vez(es) na frase.')
    print(f'A primeira letra "A" apareceu na posição {frase.find("a") + 1}.')
    print(f'A última letra "A" apareceu na posição {frase.rfind("a") + 1}.')
    ''')
    frase = str(input('Digite uma frase: ')).strip().lower()
    print(f'A letra "A" aparece {frase.count("a")} vez(es) na frase.')
    print(f'A primeira letra "A" apareceu na posição {frase.find("a") + 1}.')
    print(f'A última letra "A" apareceu na posição {frase.rfind("a") + 1}.')
