"""19_ex093_cadastro_jogador_futebol.py em 2018-12-22. Projeto Curso em Video.

Cadastro de Jogador de Futebol

Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Cadastro de Jogador de Futebol')

    print('''\tfrom funcoes import cabecalho, verificador
    
    jogador = dict()
    gols = list()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['partidas'] = verificador(f'Quantas partidas {jogador["nome"]} jogou? ')
    for k in range(jogador['partidas']):
        gols.append(verificador(f'\\tQuantos gols na {k + 1}ª partida? '))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    print('-=' * 34, '\\n', jogador, '\\n', '=-' * 34, sep='')
    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}.')
    print('-=' * 34)
    for k in range(len(jogador['gols'])):
        print(f'\\t=> Na {k + 1}ª partida, fez {jogador["gols"][k]} gol{"s" if jogador["gols"][k] > 1 else ""}.')
    print(f'Foi um total de {jogador["total"]} gol{"s" if jogador["total"] > 1 else ""}.')
    ''')
    jogador = dict()
    gols = list()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['partidas'] = verificador(f'Quantas partidas {jogador["nome"]} jogou? ')
    for k in range(jogador['partidas']):
        gols.append(verificador(f'\tQuantos gols na {k + 1}ª partida? '))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    print('-=' * 34, '\n', jogador, '\n', '=-' * 34, sep='')
    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}.')
    print('-=' * 34)
    for k in range(len(jogador['gols'])):
        print(f'\t=> Na {k + 1}ª partida, fez {jogador["gols"][k]} gol{"s" if jogador["gols"][k] > 1 else ""}.')
    print(f'Foi um total de {jogador["total"]} gol{"s" if jogador["total"] > 1 else ""}.')
