"""15_ex068_jogo_par_impar.py em 2018-12-17. Projeto Curso em Video.

Jogo do Par ou Ímpar

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

"""
from random import randint
from funcoes import cabecalho, verificador, questao

if __name__ == '__main__':
    cabecalho('Jogo do Par ou Ímpar')

    print('''\tfrom random import randint
    from funcoes import cabecalho, verificador, questao
    
    c = 0
    computador = randint(0, 10)
    while True:
        jogador = verificador('Digite um valor: ')
        par_impar = questao('Par ou ímpar? [P/I] ', 'PI')
        s = jogador + computador
        print('--' * 30)
        print(f'Você jogou {jogador} e o computador {computador}. '
              f'Total de {s} {"DEU PAR" if s % 2 == 0 else "DEU ÍMPAR"}.')
        print('--' * 30)
        if (s % 2 == 0 and par_impar == 'P') or (s % 2 != 0 and par_impar == 'I'):
            print('Você venceu! \\nVamos jogar novamente...')
            print('--' * 30)
            c += 1
        else:
            print('Você perdeu!')
            print('=-' * 30)
            print(f'GAME OVER! Você venceu {c} vez(es).')
            break
    ''')
    c = 0
    computador = randint(0, 10)
    while True:
        jogador = verificador('Digite um valor: ')
        par_impar = questao('Par ou ímpar? [P/I] ', 'PI')
        s = jogador + computador
        print('--' * 30)
        print(f'Você jogou {jogador} e o computador {computador}. '
              f'Total de {s} {"DEU PAR" if s % 2 == 0 else "DEU ÍMPAR"}.')
        print('--' * 30)
        if (s % 2 == 0 and par_impar == 'P') or (s % 2 != 0 and par_impar == 'I'):
            print('Você venceu! \nVamos jogar novamente...')
            print('--' * 30)
            c += 1
        else:
            print('Você perdeu!')
            print('=-' * 30)
            print(f'GAME OVER! Você venceu {c} vez(es).')
            break
