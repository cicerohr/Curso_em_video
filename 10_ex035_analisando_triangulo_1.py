"""10_ex035_analisando_triangulo_1.py em 2018-12-14. Projeto Curso em Video.

Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


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
    cabecalho('Analisando Triângulo v1.0')

    print('''\tfrom cicero import cabecalho, ansi, verificador
    
    lados = {'a': 0, 'b': 0, 'c': 0}
    for k in lados.keys():
        lado = verificador(f'lado {ansi("bold", "underline", "azul")}{k}{ansi()}: ')
        lados[k] = lado
    print(f'lados => {lados}')
    if abs(lados['b'] - lados['c']) < lados['a'] < (lados['b'] + lados['c']):
        print(f'Os lados acima {ansi("cyan")}PODEM FORMAR{ansi()} um triângulo.')
    else:
        print(f'Os lados acima {ansi("vermelho")}NÃO FORMAM{ansi()} um triângulo.')
    ''')
    lados = {'a': 0, 'b': 0, 'c': 0}
    for k in lados.keys():
        lado = verificador(f'lado {ansi("bold", "underline", "azul")}{k}{ansi()}: ')
        lados[k] = lado
    print(f'lados => {lados}')
    if abs(lados['b'] - lados['c']) < lados['a'] < (lados['b'] + lados['c']):
        print(f'Os lados acima {ansi("cyan")}PODEM FORMAR{ansi()} um triângulo.')
    else:
        print(f'Os lados acima {ansi("vermelho")}NÃO FORMAM{ansi()} um triângulo.')

    # Código alternativo
    if lados['a'] < (lados['b'] + lados['c']) and lados['b'] < (lados['a'] + lados['c']) and lados['c'] < (
            lados['a'] + lados['b']):
        print(f'Os lados acima {ansi("cyan")}PODEM FORMAR{ansi()} um triângulo.')
    else:
        print(f'Os lados acima {ansi("vermelho")}NÃO FORMAM{ansi()} um triângulo.')
