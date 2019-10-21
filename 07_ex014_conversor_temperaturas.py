"""07_ex014_conversor_temperaturas.py em 2018-12-10. Projeto Curso em Video.

Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
K = C + 273
F = 1,8 . C + 32

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Conversor de Temperaturas')

    print('''\tc = verificador('Informe a temperatura em °C: ', float)
    print(f'A temperatura de {c}°C corresponde a {c + 273:.1f}°K ou {1.8 * c + 32:.1f}°F.')
    ''')
    c = verificador('Informe a temperatura em °C: ', float)
    print(f'A temperatura de {c}°C corresponde a {c + 273:.1f}°K ou {1.8 * c + 32:.1f}°F.')
