"""09_ex027_primeiro_ultimo_nome_pessoa.py em 2018-12-13. Projeto Curso em Video.

Primeiro e último nome de uma pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Primeiro e último nome de uma pessoa')

    print('''\tnome = str(input('Digite seu nome completo: ')).strip().title()
    print('Muito prazer em te conhecer!')
    fatiamento = nome.split(' ')
    print(f'Seu primeiro nome é {fatiamento[0]}.')
    print(f'Seu último nome é {fatiamento[-1]}.')
    print(fatiamento)
    ''')
    nome = str(input('Digite seu nome completo: ')).strip().title()
    print('Muito prazer em te conhecer!')
    fatiamento = nome.split(' ')
    print(f'Seu primeiro nome é {fatiamento[0]}.')
    print(f'Seu último nome é {fatiamento[-1]}.')
    print(fatiamento)
