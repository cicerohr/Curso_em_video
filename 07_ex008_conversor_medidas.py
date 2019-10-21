"""07_ex008_conversor_medidas.py em 2018-12-10. Projeto Curso em Video.

Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Conversor de Medidas')

    print('''\tm = float(input('Uma distância em metros: '))
    print(f'{m:.0f}m => {m / 1000}km')
    print(f'{m:.0f}m => {m / 100}hm')
    print(f'{m:.0f}m => {m / 10}dam')
    print(f'{m:.0f}m => {m * 10:.0f}dm')
    print(f'{m:.0f}m => {m * 100:.0f}cm')
    print(f'{m:.0f}m => {m * 1000:.0f}mm')
    ''')
    m = float(input('Uma distância em metros: '))
    print(f'{m:.0f}m => {m / 1000}km')
    print(f'{m:.0f}m => {m / 100}hm')
    print(f'{m:.0f}m => {m / 10}dam')
    print(f'{m:.0f}m => {m * 10:.0f}dm')
    print(f'{m:.0f}m => {m * 100:.0f}cm')
    print(f'{m:.0f}m => {m * 1000:.0f}mm')
