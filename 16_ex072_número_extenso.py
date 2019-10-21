"""16_ex072_número_extenso.py em 2018-12-19. Projeto Curso em Video.

Número por Extenso

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Número por Extenso')

    print('''\tfrom funcoes import cabecalho, verificador
    
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
               'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    while True:
        numero = verificador('Digite um número entre 0 e 20: ')
        if 0 <= numero <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {numeros[numero]}.')
    ''')
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
               'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    while True:
        numero = verificador('Digite um número entre 0 e 20: ')
        if 0 <= numero <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {numeros[numero]}.')
