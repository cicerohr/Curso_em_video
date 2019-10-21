"""20_ex096_funcao_calcula_area.py em 2018-12-23. Projeto Curso em Video.

Função que calcula área

Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.


"""
from funcoes import cabecalho, verificador


def area(l: float, c: float) -> float:
    """Calcula uam área retangular

    :param l: largura
    :type l: float
    :param c: comprimento
    :type c: float
    :return: área em m²
    :rtype: float
    """
    return l * c


if __name__ == '__main__':
    cabecalho('Função que calcula área')

    print('''\tdef area(l, c):
        return l * c
    
    
    largura = verificador('Largura: (m) ', float)
    comprimento = verificador('Comprimento: (m) ', float)
    print(f'A área do terreno {largura} x {comprimento} é {area(largura, comprimento)}m².')
    ''')
    largura = verificador('Largura: (m) ', float)
    comprimento = verificador('Comprimento: (m) ', float)
    print(f'A área do terreno {largura} x {comprimento} é {area(largura, comprimento)}m².')
