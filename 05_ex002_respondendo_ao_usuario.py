"""05_ex002_respondendo_ao_usuario.py em 2018-12-10. Projeto Curso em Video.

Respondendo ao Usuário

Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Respondendo ao Usuário')

    print('''\tnome = str(input('Digite seu nome: '))
    print(f'É um prazer te conhecer {nome}!')
    ''')
    nome = str(input('Digite seu nome: '))
    print(f'É um prazer te conhecer {nome}!')
