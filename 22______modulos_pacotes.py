"""22______modulos_pacotes.py em 2019-04-29. Projeto Curso em Video.

Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar
nossos códigos em outros projetos.
Vamos aprender também como agrupar vários módulos em um funcoes, ampliando ainda mais a modularização em grandes
projetos em Python.

"""
from pacotes import strings, cores
import uteis

if __name__ == '__main__':
    strings.cabecalho('Módulos e Pacotes')

    num = int(input('Digite um número: '))
    fat = uteis.fatorial(num)
    print(f'O fatorial de {num} é {cores.ansi("azul")}{fat}{cores.ansi()}.')
    print(f'O dobro de {num} é {cores.ansi("azul")}{uteis.dobro(num)}{cores.ansi()}.')
