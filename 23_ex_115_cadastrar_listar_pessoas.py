"""23_ex_115_cadastrar_listar_pessoas.py em 2019-07-16. Projeto Curso em Video.

Manipulando arquivo de texto

Crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções:
    - cadastrar uma nova pessoa;
    - listar todas as pessoas cadastradas.

"""
from funcoes import cabecalho, ansi, verificador


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


def cria_cabecalho(s: int, t: int = 50) -> object:
    """-> Cria um cabecalho centralizado para cada opção

    :param s: seleção da lista opcoes
    :type s: int
    :param t: (opcional) largura do cabecalho
    :type t: int
    :return: imprime no terminal o cabecalho
    :rtype: object
    """
    opcoes = ['Menu Principal', 'Pessoas Cadastradas', 'Novo Cadastro', 'Saindo do sistema... Até logo!']
    return print('\n', '=' * t, '\n', opcoes[s].center(t).upper(), '\n', '=' * t, sep='')


def mostra_menu():
    """-> Cria menu de interação com o usuário

    """
    from time import sleep

    menu = {1: 'Ver pessoas cadastradas', 2: 'Cadastrar novas pessoas', 3: 'Sair do sistema'}
    sleep(1)
    cria_cabecalho(0)
    for k, v in menu.items():
        print(f'{ansi("amarelo", "bold")}{k} - {ansi()}{ansi("azul", "bold")}{v}{ansi()}')
    print('-' * 50)


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


if __name__ == '__main__':
    cabecalho('Cadastrar e listar pessoas')

    destino = 'txt/cadastro.txt'
    if arquivo_existe(destino):
        while True:
            mostra_menu()
            opcao = verificador(f'{ansi("amarelo", "bold")}Sua opção:{ansi()} ')
            if opcao == 1:
                le_arquivo(destino)
            elif opcao == 2:
                escreve_arquivo(destino)
            elif opcao == 3:
                cria_cabecalho(3)
                break
            else:
                print(f'{ansi("vermelho", "bold")}ERRO! Digite uma opção válida. Tente novamente!{ansi()}')
                continue
