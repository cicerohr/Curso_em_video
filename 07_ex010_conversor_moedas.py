"""07_ex010_conversor_moedas.py em 2018-12-10. Projeto Curso em Video.

Conversor de Moedas

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Cotação em 2018-12-10: € 1,00 => R$ 4,45
                       US$ 1,00 => R$ 3,92

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Conversor de Moedas')

    print('''\teuro = 4.45
    dolar = 3.92
    real = verificador('Quanto dinheiro você tem na carteira? R$ ', float)
    print(f'Com R$ {real:.2f} você pode comprar € {real / euro:.2f} ou US$ {real/dolar:.2f}.')
    ''')
    euro = 4.45
    dolar = 3.92
    real = verificador('Quanto dinheiro você tem na carteira? R$ ', float)
    print(f'Com R$ {real:.2f} você pode comprar € {real / euro:.2f} ou US$ {real/dolar:.2f}.')
