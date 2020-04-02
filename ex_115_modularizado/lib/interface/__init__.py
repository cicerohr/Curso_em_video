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


def linha(tam=42):
    """-> Cria uma linha de decoração

    :param tam: tamanho da linha
    :return: a linha
    """
    return '-' * tam


def cabecalho(txt):
    """-> Cria um cabeçalho com texto no centro

    :param txt: Texto do cabeçalho centralizado
    """
    print(linha())
    print(txt.center(42).upper())
    print(linha())


def menu(lista):
    """-> Cria um menu baseado em uma lista

    :param lista: lista comas opções
    :return: o menu
    """
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{ansi("bold", "azul")}{c} - {item}{ansi()}')
        c += 1
    print(linha())
    opc = verificador('Sua opção: ')
    return opc
