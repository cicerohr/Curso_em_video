"""11______cores_no_terminal.py em 2018-12-06. Projeto Curso em Video.

Cores no Terminal

Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para
os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

"""
from funcoes import cabecalho


def ansi(a='', b='', c=''):
    """Dicionário com códigos de escape sequence ANSI para configurar cores no terminal.

    A ordem dos parâmetros é irrelevante, bem como é possível colocar dois parâmetros do mesmo tipo:
    Ex.: ansi('bold', 'underline') => Coloca o caracter em BOLD e UNDERLINE

           style       back
     \033 [  0 ; 33 ;  44   m
                text
    Obs.: a ordem dos números não é importante; não é necessário utilizar todos os números.

      Style        Text    Background
    0  None         30         40     (branco)
    1  Bold         31         41     (vermelho)
    4  Underline    32         42     (verde)
    7  Negative     33         43     (amarelo)
                    34         44     (azul)
                    35         45     (magenta)
                    36         46     (cyan)
                    37         47     (cinza)

    Sempre termine cada sequência de escape com ansi(), sem parâmetros, que equivale a \033[m (limpa Escape Sequence)

    :param a: estilo do caracter ou cor do caracter ou cor do fundo ou vazio
    :type a: str
    :param b: estilo do caracter ou cor do caracter ou cor do fundo ou vazio
    :type b: str
    :param c: estilo do caracter ou cor do caracter ou cor do fundo ou vazio
    :type c: str
    :return: escape sequence ANSI
    :rtype: str

    """
    dicionario = {'': '',
                  'none': 0,
                  'bold': 1,
                  'underline': 4,
                  'negative': 7,
                  'branco': 30,
                  'vermelho': 31,
                  'verde': 32,
                  'amarelo': 33,
                  'azul': 34,
                  'magenta': 35,
                  'cyan': 36,
                  'cinza': 37,
                  'f_branco': 40,
                  'f_vermelho': 41,
                  'f_verde': 42,
                  'f_amarelo': 43,
                  'f_azul': 44,
                  'f_magenta': 45,
                  'f_cyan': 46,
                  'f_cinza': 47}

    return f'\033[{dicionario[a]};{dicionario[b]};{dicionario[c]}m'


if __name__ == '__main__':
    cabecalho('Cores no Terminal')

    cabecalho('escape sequence ANSI', 50, '-')
    print('\t style\t   back')
    print(f'\\{ansi("vermelho")}033{ansi()}[  {ansi("amarelo")}0{ansi()}; {ansi("amarelo")}33{ansi()};  '
          f'{ansi("amarelo")}44{ansi()}{ansi("azul")}m{ansi()}')
    print('\t\t text\n')
    print('Obs.: a ordem dos números não é importante; não é necessário utilizar todos os números.\n')
    print(f'{ansi("bold", "underline")}Style\t\tText\tBack{ansi()}\n')
    print(f'{ansi("none")}0{ansi()} None\t\t{ansi("branco")}30{ansi()}\t\t{ansi("negative", "branco")}40{ansi()}')
    print(f'{ansi("bold")}1{ansi()} Bold\t\t{ansi("vermelho")}31{ansi()}\t\t{ansi("negative", "vermelho")}41{ansi()}')
    print(f'{ansi("underline")}4{ansi()} Underline\t{ansi("verde")}32{ansi()}\t\t{ansi("negative", "verde")}42{ansi()}')
    print(
        f'{ansi("negative")}7{ansi()} Negative\t{ansi("amarelo")}33{ansi()}\t\t{ansi("negative", "amarelo")}43{ansi()}')
    print(f'\t\t\t{ansi("azul")}34{ansi()}\t\t{ansi("negative", "azul")}44{ansi()}')
    print(f'\t\t\t{ansi("magenta")}35{ansi()}\t\t{ansi("negative", "magenta")}45{ansi()}')
    print(f'\t\t\t{ansi("cyan")}36{ansi()}\t\t{ansi("negative", "cyan")}46{ansi()}')
    print(f'\t\t\t{ansi("cinza")}37{ansi()}\t\t{ansi("negative", "cinza")}47{ansi()}')
