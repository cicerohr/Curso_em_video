"""12_ex045_pedra_papel_tesoura.py em 2018-12-14. Projeto Curso em Video.

GAME: Pedra Papel e Tesoura

Crie um programa que faça o computador jogar Jokenpô com você.

"""
from time import sleep
from random import randint
from funcoes import cabecalho, verificador, ansi, questao

if __name__ == '__main__':
    cabecalho('GAME: Pedra Papel e Tesoura')

    print('''\tfrom time import sleep
    from random import randint
    from funcoes import cabecalho, verificador, ansi, questao
    
    menu = {0: 'PEDRA', 1: 'PAPEL', 2: 'TESOURA'}
    jokenpo = ['JO', 'KEN', 'PO!!!']
    continuar = ' '
    while continuar != 'N':
        computador = randint(0, 2)
        for k, v in menu.items():
            print(f'[{k}] {v}')
        jogador = verificador('\\nQual é sua jogada? ')
        if 0 <= jogador <= 2:
            for k in range(0, 3):
                print(jokenpo[k], flush=True)
                sleep(1)
            print('-=' * 13)
            print(f' Computador jogou {menu[computador]} \\n Jogador jogou {menu[jogador]}')
            print('-=' * 13)
            if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
                print('Jogador Vence.\\n')
            elif jogador == computador:
                print('Houve um empate.\\n')
            else:
                print('Computador vence.\\n')
        else:
            print(f'{ansi("vermelho")}Digite um número entre 0 e 2.{ansi()}')
        continuar = questao('Quer continuar [S/N] ', 'SN')
    ''')
    menu = {0: 'PEDRA', 1: 'PAPEL', 2: 'TESOURA'}
    jokenpo = ['JO', 'KEN', 'PO!!!']
    continuar = ' '
    while continuar != 'N':
        computador = randint(0, 2)
        for k, v in menu.items():
            print(f'[{k}] {v}')
        jogador = verificador('\nQual é sua jogada? ')
        if 0 <= jogador <= 2:
            for k in range(0, 3):
                print(jokenpo[k], flush=True)
                sleep(1)
            print('-=' * 13)
            print(f' Computador jogou {menu[computador]} \n Jogador jogou {menu[jogador]}')
            print('-=' * 13)
            if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
                print('Jogador Vence.\n')
            elif jogador == computador:
                print('Houve um empate.\n')
            else:
                print('Computador vence.\n')
        else:
            print(f'{ansi("vermelho")}Digite um número entre 0 e 2.{ansi()}')
        continuar = questao('Quer continuar [S/N] ', 'SN')
