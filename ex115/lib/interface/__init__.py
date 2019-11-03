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


def cria_cabecalho(s: int, c: str = '-', t: int = 50) -> object:
    """-> Cria um cabeçalho centralizado para cada opção

    :param s: seleção da lista opções
    :type s: int
    :param c: (opcional) caracter para a impressão
    :type c: str
    :param t: (opcional) largura do cabeçalho
    :type t: int
    :return: imprime no terminal o cabeçalho
    :rtype: object
    """
    opcoes = ['Menu Principal', 'Pessoas Cadastradas', 'Novo Cadastro', 'Saindo do sistema... Até logo!',
              'Cadastrar e listar pessoas']
    return print('\n', c * t, '\n', opcoes[s].center(t).upper(), '\n', c * t, sep='')


def mostra_menu():
    """-> Cria menu de interação com o usuário

    """
    from time import sleep

    menu = {1: 'Ver pessoas cadastradas', 2: 'Cadastrar novas pessoas', 3: 'Sair do sistema'}
    sleep(1)
    cria_cabecalho(0, '>')
    for k, v in menu.items():
        print(f'{ansi("amarelo", "bold")}{k} - {ansi("azul", "bold")}{v}{ansi()}')
    print('-' * 50)


def arquivo_existe(arquivo: str) -> bool:
    """-> Verifica se o arquivo existe, caso contrário o cria

    :param arquivo: destino e nome do arquivo
    :type arquivo: str
    :return: True
    :rtype: bool
    """
    try:
        file = open(arquivo, 'r', encoding='utf8')
    except FileNotFoundError:
        file = open(arquivo, 'w', encoding='utf8')
        file.close()
        return True
    else:
        file.close()
        return True


def le_arquivo(arquivo):
    """-> Lê e imprime conteúdo do arquivo

    :param arquivo: destino e nome do arquivo
    :type arquivo: str
    """
    cria_cabecalho(1)
    file = open(arquivo, 'r', encoding='utf8')
    for linha in file:
        print(linha, end='')
    file.close()


def escreve_arquivo(arquivo):
    """-> Escreve no arquivo

    :param arquivo: destino e nome do arquivo
    :type arquivo: str
    """
    cria_cabecalho(2)
    nome = input(str('Nome: ')).strip().title()
    idade = verificador('Idade: ')
    file = open(arquivo, 'r', encoding='utf8')
    conteudo = file.readlines()
    conteudo.append(f'\n{nome:40}{idade:3} ano(s)')
    file = open(arquivo, 'w', encoding='utf8')
    file.writelines(conteudo)
    file.close()
    print(f'Novo registro de {nome} adicionado.')
