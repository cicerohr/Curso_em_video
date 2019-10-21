"""20______funcoes_1.py em 2018-12-09. Projeto Curso em Video.

Funções (Parte 1)

Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de
código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o
comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

"""
from funcoes import cabecalho, ansi


def titulo(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


if __name__ == '__main__':
    cabecalho('Funções (Parte 1)')

    print('''\tdef titulo(msg):
        print('-' * 30)
        print(msg)
        print('-' * 30)
    ''')
    print(f"\t{ansi('cyan', 'bold', 'bold')}titulo('      Curso em vídeo'){ansi()}")
    titulo('      Curso em vídeo')
    print(f"\n\t{ansi('cyan', 'bold')}titulo('   Python é muito bom'){ansi()}")
    titulo('   Python é muito bom')
    print(f"\n\t{ansi('cyan', 'bold')}titulo('oi'){ansi()}")
    titulo('oi')
