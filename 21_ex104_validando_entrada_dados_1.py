"""21_ex104_validando_entrada_dados_1.py em 2018-12-25. Projeto Curso em Video.

Validando entrada de dados em Python

Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')

"""
from funcoes import cabecalho, ansi


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


if __name__ == '__main__':
    cabecalho('Validando entrada de dados em Python')

    print('''\tfrom funcoes import cabecalho, ansi
    
    
    def so_numero(mensagem):
        while True:
            try:
                entrada_usuario = int(input(mensagem))
            except ValueError:
                print(f'{ansi("vermelho")}Digite um número inteiro. Tente novamente!{ansi()}')
                continue
            else:
                return entrada_usuario
    
    
    n = so_numero('Digite um número: ')
    print(f'Você digitou o número {n}.')
    ''')
    n = so_numero('Digite um número: ')
    print(f'Você digitou o número {n}.')
