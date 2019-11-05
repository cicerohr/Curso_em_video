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
    from ex115.lib.interface import cria_cabecalho
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
    from ex115.lib.interface import cria_cabecalho, verificador
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
