"""10______condicoes_1.py em 2018-12-06. Projeto Curso em Video.

Condições (Parte 1)

Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Condições')

    cabecalho('Estrutura condicional composta', 50, '-')
    tempo = int(input('Quantos anos tem seu carro? '))
    print("""
    if tempo <= 3:
        print('Carro novo')
    else:
        print('Carro velho')
    print('-- Fim --')
    """)

    if tempo <= 3:
        print('Carro novo')
    else:
        print('Carro velho')
    print('-- Fim --')

    cabecalho('Estrutura condicional simples', 50, '-')
    print("""
    print('Carro novo' if tempo <= 3 else 'Carro velho')
    print('-- Fim --')
    """)
    print('Carro novo' if tempo <= 3 else 'Carro velho')
    print('-- Fim --')

    print('-' * 50)
    n1 = float(input('Digite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    m = (n1 + n2) / 2
    print(f'A sua média foi {m:.1f}.', end=' ')
    print('Parabéns!' if m >= 6 else 'Estude mais.')
