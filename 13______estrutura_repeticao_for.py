"""13______estrutura_repeticao_for.py em 2018-12-06. Projeto Curso em Video.

Estrutura de repetição for

Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for", que é uma estrutura versátil e
simples de entender. Por exemplo:

for c in range(0, 4):
     print(c)
print('Acabou')


"""
from funcoes import cabecalho, ansi

if __name__ == '__main__':
    cabecalho('Estrutura de repetição for')

    print(f'{ansi("bold", "amarelo")}range(start, stop[, step]){ansi()}\n')
    print('''\tfor c in range(0, 6):
        print(c)''')
    for c in range(0, 6):
        print(c)
    print('-' * 30)

    print(f'{ansi("bold", "amarelo")}range(start, stop[, step]){ansi()}\n')
    print('''\tfor d in range(0, 6, 2):
        print(d)''')
    for d in range(0, 6, 2):
        print(d)
    print('-' * 30)

    print(f'{ansi("bold", "amarelo")}range(start, stop[, step]){ansi()}\n')
    print('''\tfor e in range(6, 0, -1):
        print(e)''')
    for e in range(6, 0, -1):
        print(e)
    print('-' * 30)
