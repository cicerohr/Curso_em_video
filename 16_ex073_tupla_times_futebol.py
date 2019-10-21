"""16_ex073_tupla_times_futebol.py em 2018-12-19. Projeto Curso em Video.

Tupla com Times de Futebol

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.

"""
from funcoes import cabecalho, ansi

if __name__ == '__main__':
    cabecalho('Tupla com Times de Futebol')

    print('''\tfrom funcoes import cabecalho, ansi
    
    brasileirao = ('Atlético', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense', 'América-MG', 'São Paulo',
                   'Grêmio', 'Vasco da Gama', 'Internacional', 'Botafogo', 'Sport Recife', 'Cruzeiro', 'EC Vitória',
                   'Santos', 'Chapecoense', 'Atlético-PR', 'Bahia', 'Ceará SC', 'Paraná')
    print('=-=' * 30, '\\n', f'Lista de times: {brasileirao}', sep='')
    print('=-=' * 30, '\\n', f'Os 5 primeiros são: {brasileirao[:5]}', sep='')
    print('=-=' * 30, '\\n', f'Os 4 últimos são: {brasileirao[-4:]}', sep='')
    print('=-=' * 30, '\\n', f'Times em ordem alfabética: {sorted(brasileirao)}', sep='')
    print('=-=' * 30, '\\n', f'A Chapecoense esta na posição {brasileirao.index("Chapecoense") + 1}.', sep='')
    
    # Variação do exercício
    print('\\n', '=' * 42, '\\n', f'Tabela do Brasileirão'.center(42).upper(), '\\n', '=' * 42, sep='')
    for k in range(len(brasileirao)):
        if k < 6:
            print(f'{ansi("azul")}{k + 1:2}° {brasileirao[k]}{ansi()}')
        elif k > 15:
            print(f'{ansi("vermelho")}{k + 1:2}° {brasileirao[k]}{ansi()}')
        else:
            print(f'{k + 1:2}° {brasileirao[k]}')
    print('-' * 42, '\\n', f'{ansi("azul")}█{ansi()} Zona de Classificação para Libertadores', sep='')
    print(f'{ansi("vermelho")}█{ansi()} Zona de Rebaixamento')
    ''')
    brasileirao = ('Atlético', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense', 'América-MG', 'São Paulo',
                   'Grêmio', 'Vasco da Gama', 'Internacional', 'Botafogo', 'Sport Recife', 'Cruzeiro', 'EC Vitória',
                   'Santos', 'Chapecoense', 'Atlético-PR', 'Bahia', 'Ceará SC', 'Paraná')
    print('=-=' * 30, '\n', f'Lista de times: {brasileirao}', sep='')
    print('=-=' * 30, '\n', f'Os 5 primeiros são: {brasileirao[:5]}', sep='')
    print('=-=' * 30, '\n', f'Os 4 últimos são: {brasileirao[-4:]}', sep='')
    print('=-=' * 30, '\n', f'Times em ordem alfabética: {sorted(brasileirao)}', sep='')
    print('=-=' * 30, '\n', f'A Chapecoense esta na posição {brasileirao.index("Chapecoense") + 1}.', sep='')
    # Variação do exercício
    print('\n', '=' * 42, '\n', f'Tabela do Brasileirão'.center(42).upper(), '\n', '=' * 42, sep='')
    for k in range(len(brasileirao)):
        if k < 6:
            print(f'{ansi("azul")}{k + 1:2}° {brasileirao[k]}{ansi()}')
        elif k > 15:
            print(f'{ansi("vermelho")}{k + 1:2}° {brasileirao[k]}{ansi()}')
        else:
            print(f'{k + 1:2}° {brasileirao[k]}')
    print('-' * 42, '\n', f'{ansi("azul")}█{ansi()} Zona de Classificação para Libertadores', sep='')
    print(f'{ansi("vermelho")}█{ansi()} Zona de Rebaixamento')
