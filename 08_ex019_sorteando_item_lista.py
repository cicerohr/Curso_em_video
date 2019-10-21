"""08_ex019_sorteando_item_lista.py em 2018-12-10. Projeto Curso em Video.

Sorteando um item na lista

Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

"""
from random import choice
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Sorteando um item na lista')

    print('''\tfrom random import choice
    
    alunos = []
    for a in range(1, 5):
        aluno = str(input(f'{a}° aluno: ').strip().title())
        alunos.append(aluno)
    print(f'O aluno escolhido foi {choice(alunos)}.')
    ''')
    alunos = []
    for a in range(1, 5):
        aluno = str(input(f'{a}° aluno: ').strip().title())
        alunos.append(aluno)
    print(f'O aluno escolhido foi {choice(alunos)}.')
    print(alunos)
