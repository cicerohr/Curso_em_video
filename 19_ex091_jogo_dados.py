"""19_ex091_jogo_dados.py em 2018-12-22. Projeto Curso em Video.

Jogo de Dados em Python

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

"""
from time import sleep
from random import randint
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Jogo de Dados em Python')

    print('''\tfrom time import sleep
    from random import randint
    from funcoes import cabecalho
    
    jogadores = dict(jogador_1=randint(1, 6),
                     jogador_2=randint(1, 6),
                     jogador_3=randint(1, 6),
                     jogador_4=randint(1, 6))
    c = 0
    for k, v in jogadores.items():
        print(f'{k} tirou {v} no dado.', flush=True)
        sleep(1)
    print('=-' * 15, '\\n', ' Ranking dos jogadores '.center(27, '=').upper())
    for k in sorted(jogadores, key=jogadores.get, reverse=True):
        c += 1
        print(f'{c}° lugar: {k} com {jogadores[k]}.')
        sleep(1)
    ''')
    jogadores = dict(jogador_1=randint(1, 6),
                     jogador_2=randint(1, 6),
                     jogador_3=randint(1, 6),
                     jogador_4=randint(1, 6))
    c = 0
    for k, v in jogadores.items():
        print(f'{k} tirou {v} no dado.', flush=True)
        sleep(1)
    print('=-' * 15, '\n', ' Ranking dos jogadores '.center(27, '=').upper())
    for k in sorted(jogadores, key=jogadores.get, reverse=True):
        c += 1
        print(f'{c}° lugar: {k} com {jogadores[k]}.')
        sleep(1)
