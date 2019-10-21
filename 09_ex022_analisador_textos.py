"""09_ex022_analisador_textos.py em 2018-12-11. Projeto Curso em Video.

Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao _todo﻿﻿ (sem considerar espaços).
- Quantas letras tem o primeiro nome.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Analisador de Textos')

    print('''\tnome = str(input('Digite seu nome completo: ').strip().title())
    print(f'Seu nome em maiúsculas é {nome.upper()}.')
    print(f'Seu nome em minúsculas é {nome.lower()}.')
    print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
    print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
    analisador = nome.split(' ')    
    print(f'Seu primeiro nome tem {len(analisador[0])} letras.')
    print(analisador)
    ''')
    nome = str(input('Digite seu nome completo: ').strip().title())
    print(f'Seu nome em maiúsculas é {nome.upper()}.')
    print(f'Seu nome em minúsculas é {nome.lower()}.')
    print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
    print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
    analisador = nome.split(' ')
    print(f'Seu primeiro nome tem {len(analisador[0])} letras.')
    print(analisador)
