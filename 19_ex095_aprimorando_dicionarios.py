"""19_ex095_aprimorando_dicionarios.py em 2018-12-23. Projeto Curso em Video.

Aprimorando os Dicionários

Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento de cada jogador.

"""
from funcoes import cabecalho, verificador, questao, ansi

if __name__ == '__main__':
    cabecalho('Aprimorando os Dicionários')

    print('''\tfrom funcoes import cabecalho, verificador, questao, ansi
    jogadores = list()
    jogador = dict()
    gols = list()
    while True:
        jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
        jogador['partidas'] = verificador(f'Quantas partidas {jogador["nome"]} jogou? ')
        for k in range(jogador['partidas']):
            gols.append(verificador(f'\\tQuantos gols na {k + 1}ª partida? '))
            jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
        jogadores.append(jogador.copy())
        gols.clear()
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            break
    while True:
        print('-' * 50, '\\n', f'{"cod":4}', f'{"nome":20}', f'{"gols":20}', f'{"total":5}', '\\n', '-' * 50, sep='')
        for k, v in enumerate(jogadores):
            print(f'{str(k):3}', f'{v["nome"]:20}', f'{str(v["gols"]):24}', f'{str(v["total"]):3}', sep='')
        print('-' * 50, sep='')
        mostrar = verificador('Mostrar dados de qual jogador? (999 sair) ')
        if mostrar == 999:
            print('<< Volte Sempre >>>'.upper())
            break
        elif mostrar >= len(jogadores):
            print(f'{ansi("vermelho")}Erro! Não existe jogador com código {mostrar}!{ansi()}')
        else:
            print(f'-- Levantamento do jogador {jogadores[mostrar]["nome"]}:')
            for k, v in enumerate(jogadores[mostrar]['gols']):
                print(f'\\t=> Na {k + 1}ª partida, fez {v}'
                      f' gol{"s" if jogador["gols"][k] > 1 else ""}.')
    ''')
    jogadores = list()
    jogador = dict()
    gols = list()
    while True:
        jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
        jogador['partidas'] = verificador(f'Quantas partidas {jogador["nome"]} jogou? ')
        for k in range(jogador['partidas']):
            gols.append(verificador(f'\tQuantos gols na {k + 1}ª partida? '))
            jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
        jogadores.append(jogador.copy())
        gols.clear()
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            break
    while True:
        print('-' * 50, '\n', f'{"cod":4}', f'{"nome":20}', f'{"gols":20}', f'{"total":5}', '\n', '-' * 50, sep='')
        for k, v in enumerate(jogadores):
            print(f'{str(k):3}', f'{v["nome"]:20}', f'{str(v["gols"]):24}', f'{str(v["total"]):3}', sep='')
        print('-' * 50, sep='')
        mostrar = verificador('Mostrar dados de qual jogador? (999 sair) ')
        if mostrar == 999:
            print('<< Volte Sempre >>>'.upper())
            break
        elif mostrar >= len(jogadores):
            print(f'{ansi("vermelho")}Erro! Não existe jogador com código {mostrar}!{ansi()}')
        else:
            print(f'-- Levantamento do jogador {jogadores[mostrar]["nome"]}:')
            for k, v in enumerate(jogadores[mostrar]['gols']):
                print(f'\t=> Na {k + 1}ª partida, fez {v}'
                      f' gol{"s" if jogador["gols"][k] > 1 else ""}.')
