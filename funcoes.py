"""funcoes.py em 2018-10-04. Projeto Practice Python.

Funções para uso geral

"""


def questao(mensagem: str, acronimos: str) -> str:
    """-> Verifica a resposta para questões com apenas duas opções

    :param mensagem: mensagem com a questão
    :type mensagem: str
    :param acronimos: tipos possíveis de reposta (ex.: SN para sim e não; MF para masculino e feminino)
    :type acronimos: str
    :return: reposta do usuário
    :rtype: str
    """
    while True:
        reposta = str(input(mensagem)).strip().upper()[0]
        if reposta not in acronimos.upper():
            print(f'{ansi("vermelho")}Digite somente letras sugeridas [{acronimos.upper()}]. Tente novamente!{ansi()}')
        else:
            return reposta


def so_numero(mensagem: str) -> int:
    """-> Verifica se a entrada é um valor inteiro

    :param mensagem: string com uma mensagem
    :type mensagem: str
    :return: valor inteiro ou mensagem de erro
    :rtype: int
    """
    while True:
        try:
            entrada_usuario = int(input(mensagem))
        except ValueError:
            print(f'{ansi("vermelho")}Digite um número inteiro. Tente novamente!{ansi()}')
            continue
        else:
            return entrada_usuario


def verificador(m, n=int):
    """-> Verifica se a entrada do usuário é um número inteiro ou real,
    caso não seja nenhuma das opções retorna uma mensagem de erro.

    :param m: mensagem da entrada
    :param n:(opcional) tipos possíveis => int; float
    :return: entrada do usuário
    """
    entrada = 0
    while True:
        try:
            if n == int:
                entrada = int(input(m))
            elif n == float:
                entrada = float(input(m))
        except ValueError:
            print(f'{ansi("vermelho")}Digite um número {"inteiro" if n == int else "real"}. Tente novamente!{ansi()}')
            continue
        else:
            return entrada


def cabecalho(titulo: str, caracteres: int = 50, tipo: str = '=') -> object:
    """-> Imprime um cabeçalho

    :param titulo: título
    :type titulo: str
    :param caracteres: número de caracteres do título
    :type caracteres: int
    :param tipo: tipo de caracter de preenchimento
    :type tipo: str
    :return: impressão do cabeçalho
    :rtype: object
    """
    return print('\n', f' {titulo} '.title().center(caracteres, tipo), '\n')


def escreva(m: str) -> object:
    """-> Imprime uma mensagem centralizada entre sequência de strings

    :param m: mensagem
    :type m: str
    :return: impressão formatada
    :rtype: object
    """
    return print(f'{(len(m) + 2) * "~"}', f'\n{str(m).center(len(m) + 2)}\n', f'{(len(m) + 2) * "~"}', sep='')


def cores(cor: str) -> str:
    """-> Dicionário com códigos de escape sequence ANSI para configurar cores no terminal

    :param cor: nome da cor
    :type cor: str
    :return: cor do dicionário
    :rtype: str
    """
    dicionario = {'limpa': '\033[m',
                  'vermelho': '\033[1;31m',
                  'verde': '\033[1;32m',
                  'amarelo': '\033[1;33m',
                  'azul': '\033[1;34m',
                  'sublinhado': '\033[4m',
                  'bold': '\033[1;30m',
                  'pretoBranco': '\033[7;30m'}
    return dicionario[cor]


def ansi(a: str = '', b: str = '', c: str = '') -> str:
    """-> Dicionário com códigos de escape sequence ANSI para configurar cores no terminal.

    A ordem dos parâmetros é irrelevante, bem como é possível colocar dois parâmetros do mesmo estilo:
    Ex.: ansi('bold', 'underline') => Coloca o caracter em BOLD e UNDERLINE

           style       back
     \\033 [  0 ; 33 ;  44   m
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
    dicionario = {'bold': 1,
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
    if a != '' and b != '' and c != '':
        cor = f'\033[{dicionario[a]};{dicionario[b]};{dicionario[c]}m'
    elif a != '' and b != '':
        cor = f'\033[{dicionario[a]};{dicionario[b]}m'
    elif a != '':
        cor = f'\033[{dicionario[a]}m'
    else:
        cor = '\033[m'

    return cor


# -------------------- programa de teste --------------------

def _gerador_teste(n, funcao, args):
    from time import time
    print(n, 'vezes', funcao.__name__)
    t0 = time()
    for i in range(n):
        funcao(*args)
    t1 = time()
    print(round(t1 - t0, 3), 'segundos,')


def _teste(n=2000):
    _gerador_teste(n, so_numero, 'Digite um número: ')


if __name__ == '__main__':
    print(__doc__)
    print(f'{cores("sublinhado")}teste{cores("limpa")}')
    print(f'{cores("azul")}teste{cores("limpa")}')
    print(f'{cores("pretoBranco")}teste{cores("limpa")}')
    print()
    print(ansi.__name__)
    print(ansi.__doc__)
    print(f'Defaults: {ansi.__defaults__}')
    print()
    print(questao.__name__)
    print(questao.__doc__)
    print(f'Defaults: {questao.__defaults__}')
    print()
    print(so_numero.__name__)
    print(so_numero.__doc__)
    print(f'Defaults: {so_numero.__defaults__}')
    print()
    print(verificador.__name__)
    print(verificador.__doc__)
    print(f'Defaults: {verificador.__defaults__}')
    print()
    print(cabecalho.__name__)
    print(cabecalho.__doc__)
    print(f'Defaults: {cabecalho.__defaults__}')
    print()
    print(cores.__name__)
    print(cores.__doc__)
    print(f'Defaults: {cores.__defaults__}')
    # _teste()
