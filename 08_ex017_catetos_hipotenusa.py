"""08_ex017_catetos_hipotenusa.py em 2018-12-10. Projeto Curso em Video.

Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
a² = b² + c² => a = √b² + c²

"""
from math import sqrt, hypot
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Catetos e Hipotenusa')

    print('''\tfrom math import sqrt, hypot
    
    b = verificador('Comprimento do cateto oposto: ', float)
    c = verificador('Comprimento do cateto adjacente: ', float)
    print(f'A hipotenusa vai medir {(b ** 2 + c ** 2) ** (1 / 2)}')
    print(f'A hipotenusa vai medir {pow((pow(b, 2) + pow(c, 2)), 1 / 2)}')
    print(f'A hipotenusa vai medir {sqrt((pow(b, 2) + pow(c, 2)))}')
    print(f'A hipotenusa vai medir {hypot(b, c)}')
    ''')
    b = verificador('Comprimento do cateto oposto: ', float)
    c = verificador('Comprimento do cateto adjacente: ', float)
    print(f'A hipotenusa vai medir {(b ** 2 + c ** 2) ** (1 / 2)}')
    print(f'A hipotenusa vai medir {pow((pow(b, 2) + pow(c, 2)), 1 / 2)}')
    print(f'A hipotenusa vai medir {sqrt((pow(b, 2) + pow(c, 2)))}')
    print(f'A hipotenusa vai medir {hypot(b, c)}')
