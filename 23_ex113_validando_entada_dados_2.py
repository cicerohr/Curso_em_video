"""23_ex113_validando_entada_dados_2.py em 2019-07-14. Projeto Curso em Video.

Reescreva a função so_numero(), que fizemos no exercício 104, incluindo agora a possibilidade de um número inválido.
Aproveite agora e faça uma função para ler números flutuantes com a mesma funcionalidade.

"""
from funcoes import cabecalho, ansi


def inteiro(mensagem: str) -> int:
    """-> Verifica se a entrada é um valor inteiro

    :param mensagem: string com uma mensagem
    :type mensagem: str
    :return: valor inteiro
    :rtype: int
    """
    while True:
        try:
            entrada_usuario = int(input(mensagem))
        except (ValueError, TypeError):
            print(f'{ansi("vermelho")}Digite um número inteiro válido. Tente novamente!{ansi()}')
            continue
        except KeyboardInterrupt:
            print(f'{ansi("amarelo")}O usuário preferiu não digitar um número!{ansi()}')
            return 0
        else:
            return entrada_usuario


def real(mensagem: str) -> float:
    """-> Verifica se a entrada é um valor real

    :param mensagem: string com a mensagem
    :type mensagem: str
    :return: valor real
    :rtype: float
    """
    while True:
        try:
            entrada_usuario = float(input(mensagem))
        except (ValueError, TypeError):
            print(f'{ansi("vermelho")}Digite um número real válido. Tente novamente!{ansi()}')
            continue
        except KeyboardInterrupt:
            print(f'{ansi("amarelo")}O usuário preferiu não digitar um número!{ansi()}')
            return 0
        else:
            return entrada_usuario


if __name__ == '__main__':
    cabecalho('Validando entrada de dados em Python')
    i = inteiro('Digite um número inteiro: ')
    r = real('Digite um número real: ')
    print(f'Você digitou o número {i} para inteiro e {r} para real.')
