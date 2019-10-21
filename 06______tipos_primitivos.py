"""06______tipos_primitivos.py em 2018-12-05. Projeto Curso em Video.

Tipos Primitivos e Saída de Dados

Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades
do int() float() bool() e str().
Além disso, veremos como fazer as primeiras operações com a função print() do Python.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Tipos Primitivos e Saída de Dados')

    print(f'''Número Primitivos
    \t\t\t\t\t\t\t\t\t\t\tEx.:
    int - números inteiros\t\t\t\t\t\t7; -4; 0; 9875
    float - números reais ou ponto flutuante\t4.5; 0.0076; -15.2333; 3.1415; 7.0
    bool - valores lógicos ou booleanos\t\t\tTrue; False
    str - valores caracteres ou string\t\t\t'Olá'; '7.5'; ''
    ''')
    cabecalho('concatenação de duas strings', 50, '-')

    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    s1 = n1 + n2

    print(f'n1 => {type(n1)}')
    print(f'n2 => {type(n2)}')
    print(f's1 => {type(s1)}')
    print('s1 = n1 + n2')
    print(f'concatenação de n1 e n2 => {n1 + n2}\n')

    m1 = int(input('Digite um número: '))
    m2 = int(input('Digite outro número: '))
    # soma de dois valores inteiros
    s2 = m1 + m2
    print(f'A soma entre {m1} e {m2} vale {s2}')
    print(f'm1 => {type(m1)}')
    print(f'm2 => {type(m2)}')
    print(f's2 => {type(s2)}')

    t1 = str(input('Digite um valor: '))
    print(f'{t1} => {type(t1)}')
    t2 = int(input('Digite um valor: '))
    print(f'{t2} => {type(t2)}')
    t3 = bool(input('Digite um valor: '))
    print(f'{t3} => {type(t3)}')

    # Método de teste de tipo
    # verifica se a string em letras maiúsculas
    s = input('Digite algo: ')
    print(s.isupper())
