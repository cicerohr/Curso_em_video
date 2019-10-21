"""09_ex024_verificando_primeiras_letras_texto.py em 2018-12-12. Projeto Curso em Video.

Verificando as primeiras letras de um texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

"""
from funcoes import cabecalho


def verificador(c):
    """Verifica se existe a palavra Santo

    :param c: palavra a ser analisada
    :type c: str
    :return: True ou False
    :rtype: bool
    """
    c = c.strip().upper()
    if 'SANTO' in c:
        return True
    else:
        return False


def verificador2(d):
    """Verifica se a primeira palavra é SANTO

    :param d: palavra a ser analisada
    :type d: str
    :return: True ou False
    :rtype: bool
    """
    d = d.strip().upper()
    if d[:5] == 'SANTO':
        return True
    else:
        return False


if __name__ == '__main__':
    cabecalho('Verificando as primeiras letras de um texto')

    cidade = str(input('Em que cidade você nasceu? '))
    print(verificador(cidade))
    print(verificador2(cidade))
