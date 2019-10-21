"""13_ex053_detector_palindromo .py em 2018-12-16. Projeto Curso em Video.

Detector de Palíndromo

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Detector de Palíndromo')

    print('''\tinverso = ''
    f = str(input('Digite uma frase: ')).strip().upper().split()
    frase = ''.join(f)
    # alternativa ao laço for:
    # inverso[::-1] ==> ao laço for para inversão da frase
    for k in range(len(frase) - 1, -1, -1):
        inverso += frase[k]
    print(f'O inverso de {frase} é {inverso}.')
    if frase == inverso:
        print('A frase digitada é um palíndromo.')
    else:
        print('A frase digitada não é um palíndromo.')
    ''')
    inverso = ''
    f = str(input('Digite uma frase: ')).strip().upper().split()
    frase = ''.join(f)
    # alternativa ao laço for:
    # inverso[::-1] ==> ao laço for para inversão da frase
    for k in range(len(frase) - 1, -1, -1):
        inverso += frase[k]
    print(f'O inverso de {frase} é {inverso}.')
    if frase == inverso:
        print('A frase digitada é um palíndromo.')
    else:
        print('A frase digitada não é um palíndromo.')
