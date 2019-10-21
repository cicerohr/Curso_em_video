"""06_ex004_dissecando_uma_variavel.py em 2018-12-10. Projeto Curso em Video.

Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Dissecando uma Variável')

    print('''\ta = input('Digite algo: ')
    print(f'O tipo primitivo desse a é {type(a)}')
    print(f'Só tem espaço? {a.isspace()}')
    print(f'É um número? {a.isnumeric()}')
    print(f'É alfabético? {a.isalpha()}')
    print(f'É alfanumérico? {a.isalnum()}')
    print(f'Esta em maiúscula? {a.isupper()}')
    print(f'Esta em minúscula? {a.islower()}')
    print(f'Esta capitalizada? {a.istitle()}')
    ''')
    a = input('Digite algo: ')
    print(f'O tipo primitivo desse a é {type(a)}')
    print(f'Só tem espaço? {a.isspace()}')
    print(f'É um número? {a.isnumeric()}')
    print(f'É alfabético? {a.isalpha()}')
    print(f'É alfanumérico? {a.isalnum()}')
    print(f'Esta em maiúscula? {a.isupper()}')
    print(f'Esta em minúscula? {a.islower()}')
    print(f'Esta capitalizada? {a.istitle()}')
