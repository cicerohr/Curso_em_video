"""14______estrutura_repeticao_while.py em 2018-12-06. Projeto Curso em Video.

Estrutura de repetição while

Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.
Por exemplo:

c=1
while c != 10:
     print(c)
     c+=1
print('Acabou')

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Estrutura de repetição while')

    print('''\tc = 1
    while c < 10:
        print(c)
        c += 1''')
    c = 1
    while c < 10:
        print(c)
        c += 1
    print('-' * 30)

    print('''\tr = 's'
    while r == 's':
        n = int(input('Digite um valor: '))
        r = str(input('Quer continuar? [S/N] ')).lower()
        ''')
    r = 's'
    while r == 's':
        n = int(input('Digite um valor: '))
        r = str(input('Quer continuar? [S/N] ')).lower()
    print('-' * 30)

    print('''\twhile n != 0:
        n = int(input('Digite um valor: '))
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    print(f'Você digitou {par} pares e {impar} impares.')
    ''')
    n = 1
    par = impar = 0
    while n != 0:
        n = int(input('Digite um valor: '))
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    print(f'Você digitou {par} pares e {impar} impares.')
    print('-' * 30)
