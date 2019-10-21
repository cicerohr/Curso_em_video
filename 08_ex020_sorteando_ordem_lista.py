"""08_ex020_sorteando_ordem_lista.py em 2018-12-10. Projeto Curso em Video.

Sorteando uma ordem na lista

O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

"""
from random import shuffle
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Sorteando uma ordem na lista')

    print('''\tfrom random import shuffle
    
    alunos = []
    for a in range(1, 5):
        aluno = str(input(f'{a}° aluno: ').strip().capitalize())
        alunos.append(aluno)
    shuffle(alunos)
    print(f'A ordem de apresentação é\\n{alunos}')
    ''')
    alunos = []
    for a in range(1, 5):
        aluno = str(input(f'{a}° aluno: ').strip().capitalize())
        alunos.append(aluno)
    shuffle(alunos)
    print(f'A ordem de apresentação é\n{alunos}')

