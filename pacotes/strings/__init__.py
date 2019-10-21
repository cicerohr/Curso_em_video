def questao(mensagem: str, acronimos: str) -> str:
    """-> Verifica a resposta para questões com apenas duas opções

    :param mensagem: mensagem com a questão
    :type mensagem: str
    :param acronimos: tipos possíveis de reposta (ex.: SN para sim e não; MF para masculino e feminino)
    :type acronimos: str
    :return: reposta do usuário
    :rtype: str
    """
    from funcoes import ansi

    while True:
        reposta = str(input(mensagem)).strip().upper()[0]
        if reposta not in acronimos.upper():
            print(f'{ansi("vermelho")}'
                  f'Digite somente letras sugeridas [{acronimos.upper()}]. Tente novamente!{ansi()}')
        else:
            return reposta


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
