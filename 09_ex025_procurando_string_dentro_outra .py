"""09_ex025_procurando_string_dentro_outra .py em 2018-12-12. Projeto Curso em Video.

Procurando uma string dentro de outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Procurando uma string dentro de outra')

    print('''\tnome = str(input('Qual é o seu nome completo? ')).strip().upper()
    print(f'Seu nome tem silva? {"SILVA" in nome}')
    ''')
    nome = str(input('Qual é o seu nome completo? ')).strip().upper()
    print(f'Seu nome tem silva? {"SILVA" in nome}')
