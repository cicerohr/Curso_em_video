"""12______condicoes_aninhadas.py em 2018-12-06. Projeto Curso em Video.

Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else
em programas Python.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Condições Aninhadas')

    cabecalho('Estrutura condicional simples', 50, '-')
    print('''\tif nome == 'Gustavo':
        print('Que nome bonito!')''')

    cabecalho('Estrutura condicional composta', 50, '-')
    print('''\tif nome == 'Gustavo':
        print('Que nome bonito!')
    else:
        print('Seu nome é bem normal.')''')

    cabecalho('Estrutura condicional aninhada', 50, '-')
    print('''\tif nome == 'Gustavo':
        print('Que nome bonito!')
    elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
        print('Seu nome é bem popular no Brasil.')
    elif nome in 'Ana Cláudia Juliana Jéssica':
        print('Belo nome feminino.')
    else:
        print('Seu nome é bem normal.')
    ''')

    nome = str(input('Qual é seu nome? '))
    if nome == 'Gustavo':
        print('Que nome bonito!')
    elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
        print('Seu nome é bem popular no Brasil.')
    elif nome in 'Ana Cláudia Juliana Jéssica':
        print('Belo nome feminino.')
    else:
        print('Seu nome é bem normal.')
    print(f'Tenha um bom dia {nome}!')
