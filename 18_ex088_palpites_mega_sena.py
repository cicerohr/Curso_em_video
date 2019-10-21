"""18_ex088_palpites_mega_sena.py em 2018-12-20. Projeto Curso em Video.

Palpites para a Mega Sena

Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.

"""
from random import sample
from time import sleep
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Palpites para a Mega Sena')

    print('''\tfrom random import sample
    from time import sleep
    from funcoes import cabecalho, verificador
    
    # gera 60 número sequenciais dentro da lista (list comprehensions)
    numeros = [j for j in range(1, 61)]
    jogos = list()
    print('-' * 40, '\\n', 'Jogo na Mega Sena'.center(40).upper(), '\\n', '-' * 40, sep='')
    n_jogos = verificador('Quantos jogos você quer eu sorteie? ')
    print('\\n', f' Sorteando {n_jogos} jogo{"s" if n_jogos > 1 else ""} '.center(40, '-').upper(), sep='')
    for k in range(n_jogos):
        print(f'Jogo {k + 1}: {sorted(sample(numeros, 6))}', flush=True)
        jogos.append(sorted(sample(numeros, 6)))
        sleep(1)
    print(' < Boa Sorte! > '.center(40, '-').upper())
    ''')
    # gera 60 número sequenciais dentro da lista (list comprehensions)
    numeros = [j for j in range(1, 61)]
    jogos = list()
    print('-' * 40, '\n', 'Jogo na Mega Sena'.center(40).upper(), '\n', '-' * 40, sep='')
    n_jogos = verificador('Quantos jogos você quer eu sorteie? ')
    print('\n', f' Sorteando {n_jogos} jogo{"s" if n_jogos > 1 else ""} '.center(40, '-').upper(), sep='')
    for k in range(n_jogos):
        print(f'Jogo {k + 1}: {sorted(sample(numeros, 6))}', flush=True)
        jogos.append(sorted(sample(numeros, 6)))
        sleep(1)
    print(' < Boa Sorte! > '.center(40, '-').upper())
