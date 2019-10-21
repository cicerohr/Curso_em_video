"""21_ex103_ficha_jogador.py em 2018-12-25. Projeto Curso em Video.

Ficha do Jogador

Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

"""
from funcoes import cabecalho


def ficha(j='', g=''):
    return f'- {"<desconhecido>" if j == "" else j} fez {"0" if g == "" else g} gol{"s" if g > "1" else ""} na partida.'


if __name__ == '__main__':
    cabecalho('Ficha do Jogador')

    print('''\tdef ficha(j='', g=''):
        return f'- {"<desconhecido>" if j == "" else j} fez {"0" if g == "" else g} gol{"s" if g > "1" else ""} na partida.'

    
    jogador = str(input('Nome do jogador: ').strip().title())
    gols = str(input('Número de gols: ').strip())
    print(ficha(jogador, gols))
    ''')
    jogador = str(input('Nome do jogador: ').strip().title())
    gols = str(input('Número de gols: ').strip())
    print(ficha(jogador, gols))
