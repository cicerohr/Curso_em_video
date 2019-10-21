"""07_ex011_pintando_parede.py em 2018-12-10. Projeto Curso em Video.

Pintando Parede

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².

"""
from math import ceil
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Pintando Parede')

    print('''\tl = verificador('Largura da parede: ', float)
    h = verificador('Altura da parede: ', float)
    a = l * h
    print(f'Sua parade tem a dimensão de {l} x {h} e sua área é de {a}m².')
    print(f'Para pintar essa parede, você precisará de {a / 2:.2f} litros de tinta.')
    print(f'Sugerimos comprar {ceil(a / 2)} litros.')
    ''')
    l = verificador('Largura da parede: ', float)
    h = verificador('Altura da parede: ', float)
    a = l * h
    print(f'Sua parade tem a dimensão de {l} x {h} e sua área é de {a}m².')
    print(f'Para pintar essa parede, você precisará de {a / 2:.2f} litros de tinta.')
    print(f'Sugerimos comprar {ceil(a / 2)} litros.')
