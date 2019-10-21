"""07_ex015_aluguel_carros.py em 2018-12-10. Projeto Curso em Video.

Aluguel de Carros

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Aluguel de Carros')

    print('''\td = verificador('Quantos dias alugados? ')
    k = verificador('Quantos km rodados? ', float)
    print(f'O total a pagar é R$ {(60 * d) + (k * 0.15):.2f}.')
    ''')
    d = verificador('Quantos dias alugados? ')
    k = verificador('Quantos km rodados? ', float)
    print(f'O total a pagar é R$ {(60 * d) + (k * 0.15):.2f}.')
