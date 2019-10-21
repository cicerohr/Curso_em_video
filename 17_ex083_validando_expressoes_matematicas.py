"""17_ex083_validando_expressoes_matematicas.py em 2018-12-20. Projeto Curso em Video.

Validando expressões matemáticas

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

"""
from funcoes import cabecalho, ansi

if __name__ == '__main__':
    cabecalho('Validando expressões matemáticas')

    print('''\tfrom funcoes import cabecalho, ansi
    
    expressao = list()
    expressao.append(str(input('Digite uma expressão: ')))
    if expressao[0].count('(') != expressao[0].count(')'):
        print(f'{ansi("vermelho")}Sua expressão esta errada!{ansi()}')
    else:
        print(f'{ansi("azul")}Sua expressão esta correta!{ansi()}')
    ''')
    expressao = list()
    expressao.append(str(input('Digite uma expressão: ')))
    if expressao[0].count('(') != expressao[0].count(')'):
        print(f'{ansi("vermelho")}Sua expressão esta errada!{ansi()}')
    else:
        print(f'{ansi("azul")}Sua expressão esta correta!{ansi()}')
