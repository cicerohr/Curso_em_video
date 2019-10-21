"""12_ex042_analisando_triangulo_2.py em 2018-12-14. Projeto Curso em Video.

Analisando Triângulos v2.0

Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes


Condição de existência de um triângulo
Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos
outros dois e maior que o valor absoluto da diferença entre essas medidas.

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

Fonte: https://brasilescola.uol.com.br/matematica/triangulo.htm

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Analisando Triângulos v2.0')

    print('''\tfrom cicero import cabecalho, ansi, verificador
    
    lados = {'a': 0, 'b': 0, 'c': 0}
    for k in lados.keys():
        lado = verificador(f'lado {ansi("bold", "underline", "azul")}{k}{ansi()}: ')
        lados[k] = lado
    print(f'lados => {lados}')
    if abs(lados['b'] - lados['c']) < lados['a'] < (lados['b'] + lados['c']):
        print(f'Os lados acima {ansi("cyan")}PODEM FORMAR{ansi()} um triângulo', end=' ')
        if lados['a'] == lados['b'] == lados['c']:
            print(f'{ansi("bold", "cyan")}EQUILÁTERO{ansi()}.')
        elif lados['a'] == lados['b'] or lados['a'] == lados['c'] or lados['b'] == lados['c']:
            print(f'{ansi("bold", "cyan")}ISÓSCELES{ansi()}.')
        else:
            print(f'{ansi("bold", "cyan")}ESCALENO{ansi()}.')
    else:
        print(f'Os lados acima {ansi("vermelho")}NÃO FORMAM{ansi()} um triângulo.')
    ''')
    lados = {'a': 0, 'b': 0, 'c': 0}
    for k in lados.keys():
        lado = verificador(f'lado {ansi("bold", "underline", "azul")}{k}{ansi()}: ')
        lados[k] = lado
    print(f'lados => {lados}')
    if abs(lados['b'] - lados['c']) < lados['a'] < (lados['b'] + lados['c']):
        print(f'Os lados acima {ansi("cyan")}PODEM FORMAR{ansi()} um triângulo', end=' ')
        if lados['a'] == lados['b'] == lados['c']:
            print(f'{ansi("bold", "cyan")}EQUILÁTERO{ansi()}.')
        elif lados['a'] == lados['b'] or lados['a'] == lados['c'] or lados['b'] == lados['c']:
            print(f'{ansi("bold", "cyan")}ISÓSCELES{ansi()}.')
        else:
            print(f'{ansi("bold", "cyan")}ESCALENO{ansi()}.')
    else:
        print(f'Os lados acima {ansi("vermelho")}NÃO FORMAM{ansi()} um triângulo.')
