from ex_115_modularizado.lib.interface import cabecalho


def arquivo_existe(nome):
    """-> Verifica se o arquivo existe

    :param nome: nome do arquivo
    :return: verdadeiro ou falso
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """-> Cria um arquivo de texto

    :param nome: nome do arquivo
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except FileExistsError:
        print('Ocorreu um ERRO na criação do arquivo!')
    else:
        print(f'Aquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    """-> Lê um arquivo já existente

    :param nome: nome do arquivo
    """
    try:
        a = open(nome, 'rt')
    except FileExistsError:
        print('Ocorreu um ERRO ao ler o arquivo!')
    else:
        cabecalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    """-> Escreve no arquivo, já existente, um nome e um número

    :param arq: nome do arquivo
    :param nome: nome a ser cadastrado
    :param idade: número a ser cadastrado
    """
    try:
        a = open(arq, 'at')
    except FileExistsError:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except FileExistsError:
            print('Ocorreu um Erro no momento da escrita dos dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
