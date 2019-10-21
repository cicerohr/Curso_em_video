"""08______modulos.py em 2018-12-05. Projeto Curso em Video.

Utilizando Módulos

Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando
módulos built-in e módulos externos, oferecidos no PyPi.

"""
import random
from math import sqrt, trunc
import emoji
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Utilizando Módulos')

    print('''
    math
        ceil      (arredonda para cima e retorna um inteiro)
        floor     (arredonda para baixo e retorna um inteiro)
        trunc     (arredonda um número real x para um inteiro mais próximo em direção a 0.)
        pow       (potenciação)
        sqrt      (raiz quadrada)
        factorial (fatorial)
    ''')

    print('''
    import math             (importa todas as funções do módulo math)
    from math import sqrt   (importa somente a função sqrt)
    ''')
    num = int(input('Digite um número: '))
    raiz = sqrt(num)
    print(f'''
    A raiz quadrada de {num} é {raiz}.
    trunc(25.999) => {trunc(25.999)}
    Um número aleatório da biblioteca random (random.random()): {random.random()}
    'random.random() -> retorna um número Real aleatório no intervalo [0.0, 1.0].
    Um número inteiro aleatório (random.randint()): {random.randint(1, 10)}
    random.randint(a, b) -> Retorna um inteiro aleatório N tal que a <= N <= b.
    
    Pacotes para instalação (PyPi) - https://pypi.org
    print(emoji.emojize(":poop:", use_aliases=True)) => {emoji.emojize(":poop:", use_aliases=True)}''')
