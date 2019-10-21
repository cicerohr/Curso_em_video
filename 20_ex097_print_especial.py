"""20_ex097_print_especial.py em 2018-12-23. Projeto Curso em Video.

Um print especial

Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável.

Ex.:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~

"""
from funcoes import cabecalho


def escreva(m: str) -> object:
    """Imprime uma mensagem centralizada entre sequência de strings

    :param m: mensagem
    :type m: str
    :return: impressão formatada
    :rtype: object
    """
    return print(f'{(len(m) + 2) * "~"}', f'\n{str(m).center(len(m) + 2)}\n', f'{(len(m) + 2) * "~"}', sep='')


if __name__ == '__main__':
    cabecalho('Um print especial')

    print('''\tdef escreva(m):
        return print(f'{(len(m) + 2) * "~"}', f'\\n{str(m).center(len(m) + 2)}\\n', f'{(len(m) + 2) * "~"}', sep='')
    
    escreva('Curso de Python em Vídeo')
    escreva('Olá mundo!')
    escreva('Gustavo Guanabara')
    ''')
    escreva('Curso de Python em Vídeo')
    escreva('Olá mundo!')
    escreva('Gustavo Guanabara')
