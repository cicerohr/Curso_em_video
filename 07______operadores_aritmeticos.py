"""07______operadores_aritmeticos.py em 2018-12-05. Projeto Curso em Video.

Operadores Aritméticos

Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência dentro de
expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação, divisão, exponenciação e
quociente na linguagem Python.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Operadores Aritméticos')
    print(f'''\t+\tAdição\t\t\t\t\t\t5 + 2 == {5 + 2}
    -\tSubtração\t\t\t\t\t5 - 2 == {5 - 2}
    *\tMultiplicação\t\t\t\t5 * 2 == {5 * 2}
    /\tDivisão\t\t\t\t\t\t5 / 2 == {5 / 2}
    **\tPotência\t\t\t\t\t5 ** 2 == {5 ** 2}
    //\tDivisão inteira\t\t\t\t5 // 2 == {5 // 2}
    %\tMódulo ou resto da divisão\t5 % 2 == {5 % 2}
    ''')

    cabecalho('Ordem de Precedência', 50, '-')

    print('''\t1° ()\t\tparenteses
    2° **\t\texponenciação
    3° * / // % multiplicação, divisão, divisão inteira e módulo
    4° + -\t\tsoma e subtração
    ''')

    print(f'5 + 3 * 2 => 5 + 6 == {5 + 3 * 2}')
    print(f'3 * 5 + 4 ** 2 => 3 * 5 + 16 => 15 + 16 == {3 * 5 + 4 ** 2}')
    print(f'3 * (5 + 4) ** 2 => 3 * 9 ** 2 => 3 * 81 == {3 * (5 + 4) ** 2}')
