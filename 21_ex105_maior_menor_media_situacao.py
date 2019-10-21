"""21_ex105_maior_menor_media_situacao.py em 2018-12-26. Projeto Curso em Video.


Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as sequintes informações:
- quantidade de notas;
- a maior nota;
- a menor nota;
- a média da turma;
- a situação atual (opcional)

Adicione também as docstrings da função.

"""
from funcoes import cabecalho


def notas(*args, sit=False):
    """-> Analisa várias notas e a situação de vários alunos

    :param args: uma ou mais notas de alunos
    :type args: float
    :param sit: (opcional) indica se mostra ou não a situação
    :type sit: bool
    :return: dicionário com as informações
    :rtype: dict
    """
    alunos = dict(total=0, maior=0, menor=0, média=0)
    alunos['total'] = len(args)
    alunos['maior'] = max(args)
    alunos['menor'] = min(args)
    alunos['média'] = sum(args) / len(args)

    if sit:
        if alunos['média'] >= 7:
            alunos['situação'] = 'BOA'
        elif 6 <= alunos['média'] < 7:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    return alunos


if __name__ == '__main__':
    cabecalho('')

    print('''\tdef notas(*args, sit=False):
        alunos = dict(total=0, maior=0, menor=0, média=0)
        alunos['total'] = len(args)
        alunos['maior'] = max(args)
        alunos['menor'] = min(args)
        alunos['média'] = sum(args) / len(args)
    
        if sit:
            if alunos['média'] >= 7:
                alunos['situação'] = 'BOA'
            elif 6 <= alunos['média'] < 7:
                alunos['situação'] = 'RAZOÁVEL'
            else:
                alunos['situação'] = 'RUIM'
        return alunos
    
    
    print(notas(5.5, 9.5, 10, 6.5, sit=True))
    print(notas(6.5, 6, 6.5, sit=True))
    print(notas(3.5, 2, 6.5, 2, 7, 4, sit=True))
    print(notas(3.5, 2, 6.5, 2, 7, 4))
    help(notas)
    ''')
    print(notas(5.5, 9.5, 10, 6.5, sit=True))
    print(notas(6.5, 6, 6.5, sit=True))
    print(notas(3.5, 2, 6.5, 2, 7, 4, sit=True))
    print(notas(3.5, 2, 6.5, 2, 7, 4))
    help(notas)
