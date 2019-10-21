"""16_ex075_analise_dados_tupla.py em 2018-12-19. Projeto Curso em Video.

Análise de dados em uma Tupla

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Análise de dados em uma Tupla')

    print('''\tfrom funcoes import cabecalho, verificador
    
    pares = ''
    numeros = (verificador(f'Digite o 1° número: '),
               verificador(f'Digite o 2° número: '),
               verificador(f'Digite o 3° número: '),
               verificador(f'Digite o 4° número: '))
    for k in numeros:
        if k % 2 == 0:
            pares += f'{k} '
    print(f'Você digitou os valores {numeros}.')
    print(f'O valor 9 apareceu {numeros.count(9)} vez{"es" if numeros.count(9) > 1 else ""}.')
    if numeros.count(3) != 0:
        print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
    else:
        print(f'O valor 3 não apareceu na tupla.')
    print(f'{"Os valores pares digitado foram " if len(pares) > 2 else "O valor par digitado foi "}{pares}')
    ''')
    pares = ''
    numeros = (verificador(f'Digite o 1° número: '),
               verificador(f'Digite o 2° número: '),
               verificador(f'Digite o 3° número: '),
               verificador(f'Digite o 4° número: '))
    for k in numeros:
        if k % 2 == 0:
            pares += f'{k} '
    print(f'Você digitou os valores {numeros}.')
    print(f'O valor 9 apareceu {numeros.count(9)} vez{"es" if numeros.count(9) > 1 else ""}.')
    if numeros.count(3) != 0:
        print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
    else:
        print(f'O valor 3 não apareceu na tupla.')
    print(f'{"Os valores pares digitado foram " if len(pares) > 2 else "O valor par digitado foi "}{pares}')
