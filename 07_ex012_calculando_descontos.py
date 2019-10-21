"""07_ex012_calculando_descontos.py em 2018-12-10. Projeto Curso em Video.

Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Calculando Descontos')

    print('''\tp = verificador("qual é o preço do produto? R$ ", float)
    d = p - (p * 5/100)
    print(f'O produto que custava R$ {p}, na promoção, com desconto de 5%, vai custar R$ {d:.2f}.')
    ''')
    p = verificador("qual é o preço do produto? R$ ", float)
    d = p - (p * 5 / 100)  # equivale a p * 0.95
    print(f'O produto que custava R$ {p}, na promoção, com desconto de 5%, vai custar R$ {d:.2f}.')
