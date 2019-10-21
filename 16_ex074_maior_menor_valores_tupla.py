"""16_ex074_maior_menor_valores_tupla.py em 2018-12-19. Projeto Curso em Video.

Maior e menor valores em Tupla

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""
from random import randint
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Maior e menor valores em Tupla')

    print('''\tfrom random import randint
    
    numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    print(f'numeros => {numeros}')
    print(f'Maior => {max(numeros)}')
    print(f'Menor => {min(numeros)}')
    ''')
    numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    print(f'numeros => {numeros}')
    print(f'Maior => {max(numeros)}')
    print(f'Menor => {min(numeros)}')
