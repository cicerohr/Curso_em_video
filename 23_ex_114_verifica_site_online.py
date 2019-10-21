"""23_ex_114_verifica_site_online.py em 2019-07-15. Projeto Curso em Video.

Crie um código em Python que teste se o site www.pudim.com.br está acessível pelo computador usado.

"""
from funcoes import cabecalho, ansi


def testa_conexao(url: str) -> object:
    """-> Verifica se um site esta online a partir do dispositivo do usuário

    :param url: endereço a ser verificado
    :type url: str
    """
    import requests
    try:
        requests.get(url, timeout=6.0)
    except requests.ConnectionError:
        return print(f'{ansi("vermelho")}Erro de conexão com o site {url}!{ansi()}')
    else:
        return print(f'{ansi("verde")}Conexão estabelecida com o site {url}!{ansi()}')


if __name__ == '__main__':
    cabecalho('Verificando site Pudim.com.br')

    testa_conexao('http://pudim.com.br')
