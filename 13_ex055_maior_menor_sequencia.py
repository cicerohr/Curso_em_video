"""13_ex055_maior_menor_sequencia.py em 2018-12-16. Projeto Curso em Video.

Maior e menor da sequência

Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Maior e menor da sequência')

    print('''\tmaior = menor = 0
    for k in range(1, 6):
        pessoa = verificador(f'Massa da {k}ª pessoa: [kg] ', float)
        if maior == 0 and menor == 0:
            menor = maior = pessoa
        elif pessoa > maior:
            maior = pessoa
        elif pessoa < menor:
            menor = pessoa
    print(f'A maior massa lida foi {maior}kg.')
    print(f'A menor massa lida foi {menor}kg.')
    ''')
    maior = menor = 0
    for k in range(1, 6):
        pessoa = verificador(f'Massa da {k}ª pessoa: [kg] ', float)
        if maior == 0 and menor == 0:
            menor = maior = pessoa
        elif pessoa > maior:
            maior = pessoa
        elif pessoa < menor:
            menor = pessoa
    print(f'A maior massa lida foi {maior}kg.')
    print(f'A menor massa lida foi {menor}kg.')
