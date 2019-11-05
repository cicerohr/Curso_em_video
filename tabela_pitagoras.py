"""-> Tabela de multiplicação por coordenadas cartesianas



"""
from funcoes import ansi

for linha in range(0, 11):
    print(f'{ansi("negative", "bold")}{linha:3} {ansi()}', end='')
    for coluna in range(1, 11):
        if linha == 0 and coluna < 10:
            print(f'{ansi("negative", "bold")}{coluna:3} ', end='')
        elif linha == 0 and coluna == 10:
            print(f'{ansi("negative", "bold")}{coluna:3} {ansi()}')
        else:
            if coluna == 10 and linha != 10:
                print(f'{coluna * linha:3} ')
            else:
                if linha == coluna:
                    print(f'{ansi("negative", "bold", "vermelho")}{coluna * linha:3} {ansi()}', end='')
                else:
                    print(f'{coluna * linha:3} ', end='')
