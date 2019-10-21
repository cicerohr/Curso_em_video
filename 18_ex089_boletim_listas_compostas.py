"""18_ex089_boletim_listas_compostas.py em 2018-12-21. Projeto Curso em Video.

Boletim com listas compostas

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.

"""
from funcoes import cabecalho, questao, ansi, verificador

if __name__ == '__main__':
    cabecalho('Boletim com listas compostas')

    print('''\tfrom funcoes import cabecalho, questao, ansi, verificador
    
    alunos = list()
    while True:
        nome = str(input('Nome: ')).strip().title()
        n1 = verificador('Nota 1: ', float)
        n2 = verificador('Nota 2: ', float)
        media = (n1 + n2) / 2
        alunos.append([nome, [n1, n2], media])
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            break
    while True:
        print('-=' * 15, '\\n', 'N°.\\tNome\\t\\t\\tMédia'.upper(), '\\n', '-' * 30, sep='')
        for k in range(len(alunos)):
            print(f'{k}\\t{alunos[k][0]}'.ljust(18), f'{alunos[k][2]:2.1f}'.rjust(4), sep='')
        print('-' * 40)
        mostra = verificador('Mostrar notas de qual aluno? [999 Sair] ')
        if mostra == 999:
            print('Finalizando...'.upper(), '\\n', '<<< Volte sempre! >>>'.upper(), sep='')
            break
        elif mostra >= len(alunos):
            print(f'{ansi("vermelho")}O número {mostra} não foi cadastrado. Tente novamente!{ansi()}')
        else:
            print(f'Notas de {ansi("cyan")}{alunos[mostra][0]}{ansi()} são: {alunos[mostra][1]}.',
                  '\\n', '-' * 40, sep='')
    ''')
    alunos = list()
    while True:
        nome = str(input('Nome: ')).strip().title()
        n1 = verificador('Nota 1: ', float)
        n2 = verificador('Nota 2: ', float)
        media = (n1 + n2) / 2
        alunos.append([nome, [n1, n2], media])
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            break
    while True:
        print('-=' * 15, '\n', 'N°.\tNome\t\t\tMédia'.upper(), '\n', '-' * 30, sep='')
        for k in range(len(alunos)):
            print(f'{k}\t{alunos[k][0]}'.ljust(18), f'{alunos[k][2]:2.1f}'.rjust(4), sep='')
        print('-' * 40)
        mostra = verificador('Mostrar notas de qual aluno? [999 Sair] ')
        if mostra == 999:
            print('Finalizando...'.upper(), '\n', '<<< Volte sempre! >>>'.upper(), sep='')
            break
        elif mostra >= len(alunos):
            print(f'{ansi("vermelho")}O número {mostra} não foi cadastrado. Tente novamente!{ansi()}')
        else:
            print(f'Notas de {ansi("cyan")}{alunos[mostra][0]}{ansi()} são: {alunos[mostra][1]}.',
                  '\n', '-' * 40, sep='')
