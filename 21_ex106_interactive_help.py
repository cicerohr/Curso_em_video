"""21_ex106_interactive_help.py em 2018-12-26. Projeto Curso em Video.

Interactive Help

Faça um mini-sistema que utiliza o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar FIM, o programa encerrará.
Obs.: use cores.fo

"""
from funcoes import cabecalho, ansi


def titulo(m, fundo='verde', letra='f_branco'):
    """-> Título com cores e auto formatação

    :param m: mensagem do título
    :type m: str
    :param fundo: cor do fundo do título
    :type fundo: str
    :param letra: cor da letra do título
    :type letra: str
    :return: impressão formatada
    :rtype: object
    """
    return print(ansi('negative', fundo, letra), (len(m) + 2) * '~', f'\n{str(m).center(len(m) + 2)}\n',
                 f'{(len(m) + 2) * "~"}\n', ansi(), sep='', end='')


def py_help(c):
    """-> Mostra o manual do Python

    :param c: leitura do usuário
    :type c: str
    """
    titulo(f'Acessando o manual do comando {c}', 'azul')
    print(ansi("negative", "branco"), end='')
    help(c)


if __name__ == '__main__':
    cabecalho('Interactive Help')

    print('''\tfrom funcoes import cabecalho, ansi
    
    
    def titulo(m, fundo='verde', letra='f_branco'):
        return print(ansi('negative', fundo, letra), (len(m) + 2) * '~', f'\\n{str(m).center(len(m) + 2)}\\n',
                 f'{(len(m) + 2) * "~"}\\n', ansi(), sep='', end='')
    
    def py_help(c):
        titulo(f'Acessando o manual do comando {c}', 'azul')
        print(ansi("negative", "branco"), end='')
        help(c)
    
    
    while True:
        titulo('SISTEMA DE AJUDA PyHELP')
        f = str(input('Função ou Biblioteca > '))
        if f in 'fimFIM':
            titulo('Até logo!', 'vermelho')
            break
        else:
            py_help(f)
    ''')
    while True:
        titulo('SISTEMA DE AJUDA PyHELP')
        f = str(input('Função ou Biblioteca > '))
        if f in 'fimFIM':
            titulo('Até logo!', 'vermelho')
            break
        else:
            py_help(f)
