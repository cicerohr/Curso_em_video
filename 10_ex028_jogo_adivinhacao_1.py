"""10_ex028_jogo_adivinhacao_1.py em 2018-12-13. Projeto Curso em Video.

Jogo da Adivinhação v.1.0

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


"""
from random import randint
from time import sleep
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Jogo da Adivinhação v.1.0')

    print('''\tfrom random import randint
    from time import sleep
    from cicero import cabecalho, ansi, verificador
    
    while True:
        jogador = verificador('Em que número eu pensei? ')
        if 0 <= jogador <= 5:
            print(f'{ansi("cyan")}PROCESSANDO ...{ansi()}', flush=True)
            sleep(2)
            if computador == jogador:
                print(f'{ansi("verde")}PARABÉNS! Você me venceu!{ansi()}')
                break
            else:
                print(f'{ansi("vermelho")}Ganhei! Eu pensei no número {computador} e não no número {jogador}.')
                break
        else:
            print(f'\\n{ansi("negative", "vermelho", "f_branco")} Digite um número entre 0 e 5. Tente novamente! {ansi()}\\n')
    ''')
    print(f'{ansi("amarelo")}{"-=" * 28}{ansi()}')
    print(f'{ansi("azul")}Vou pensar em um número entre 0 e 5. Tente adivinhar ...{ansi()}')
    print(f'{ansi("amarelo")}{"-=" * 28}{ansi()}\n')
    computador = randint(0, 5)
    while True:
        jogador = verificador('Em que número eu pensei? ')
        if 0 <= jogador <= 5:
            print(f'{ansi("cyan")}PROCESSANDO ...{ansi()}', flush=True)
            sleep(2)
            if computador == jogador:
                print(f'{ansi("verde")}PARABÉNS! Você me venceu!{ansi()}')
                break
            else:
                print(f'{ansi("vermelho")}Ganhei! Eu pensei no número {computador} e não no número {jogador}.')
                break
        else:
            print(f'\n{ansi("negative", "vermelho", "f_branco")}'
                  f'Digite um número entre 0 e 5. Tente novamente! {ansi()}\n')
