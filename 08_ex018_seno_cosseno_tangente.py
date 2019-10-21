"""08_ex018_seno_cosseno_tangente.py em 2018-12-10. Projeto Curso em Video.

Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""
from math import sin, cos, tan, radians
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Seno, Cosseno e Tangente')

    print('''\tfrom math import sin, cos, tan, radians
    
    a = verificador('Digite o ângulo que você deseja: ', float)
    print(f'O seno de {a}° é {sin(radians(a)):.2f}.')
    print(f'O cosseno de {a}° é {cos(radians(a)):.2f}.')
    print(f'A tangente de {a}° é {tan(radians(a)):.2f}.')
    ''')
    a = verificador('Digite o ângulo que você deseja: ', float)
    print(f'O seno de {a}° é {sin(radians(a)):.2f}.')
    print(f'O cosseno de {a}° é {cos(radians(a)):.2f}.')
    print(f'A tangente de {a}° é {tan(radians(a)):.2f}.')
