"""16_ex077_contando_vogais_tupla.py em 2018-12-19. Projeto Curso em Video.

Contando vogais em Tupla

Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""
from funcoes import cabecalho, ansi

if __name__ == '__main__':
    cabecalho('Contando vogais em Tupla')

    print('''\tfrom funcoes import cabecalho, ansi
    
    palavras = ('aprender', 'programar', 'linguagens', 'python', 'curso', 'gratis',
                'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro', 'www')
    for palavra in palavras:
        vogais = m_palavra = ''
        for letra in palavra:
            if letra in 'aeiou':
                vogais += f'{letra} '
                m_palavra += f'{ansi("bold", "branco")}{letra}'
            else:
                m_palavra += f'{ansi()}{letra}'
        if vogais != '':
            print(f'{ansi()}Na palavra {ansi("underline")}{palavra}{ansi()} temos: {vogais}'.ljust(55, '.'), m_palavra)
    ''')
    palavras = ('aprender', 'programar', 'linguagens', 'python', 'curso', 'gratis',
                'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro', 'www')
    for palavra in palavras:
        vogais = m_palavra = ''
        for letra in palavra:
            if letra in 'aeiou':
                vogais += f'{letra} '
                m_palavra += f'{ansi("bold", "branco")}{letra}'
            else:
                m_palavra += f'{ansi()}{letra}'
        if vogais != '':
            print(f'{ansi()}Na palavra {ansi("underline")}{palavra}{ansi()} temos: {vogais}'.ljust(55, '.'), m_palavra)
