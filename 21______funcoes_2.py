"""21______funcoes_2.py em 2018-12-01. Projeto Curso em Video.

Funções (Parte 2)

Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados.

"""
from funcoes import cabecalho


def contador(i, f, p):
    """Faz a contagem e mostra na tela

    :param i: início da contagem
    :type i: int
    :param f: fim da contagem
    :type f: int
    :param p: passo da contagem
    :type p: int
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')


def somar(a=0, b=0, c=0):
    """Faz a soma de três valores e mostra o resultado na tela

    :param a: primeiro valor
    :type a: int
    :param b: segundo valor
    :type b: int
    :param c: terceiro valor
    :type c: int
    """
    return f'A soma vale {a + b + c}'


def teste(b):
    """Exemplo de variáveis de escopo

    :param b: variável escopo local
    :type b: int
    """
    global a  # força uma variável local a ser global
    a = 8  # variável de escopo local
    b += 4  # variável de escopo local
    c = 2  # variável de escopo local
    print(f'A dentro vala {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


if __name__ == '__main__':
    cabecalho('Funções (Parte 2)')

    contador(2, 10, 2)
    print(somar(3, 2, 5))
    print(somar(8, 4))
    print(somar())
    a = 5  # variável de escopo global
    teste(a)
    print(f'A fora vale {a}')
    help(contador)
    help(somar)
