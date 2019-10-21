"""21_ex101_funcoes_votacao.py em 2018-12-24. Projeto Curso em Video.

Funções para votação

Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

"""
from datetime import date
from funcoes import cabecalho, verificador


def voto(a: int) -> str:
    """Verifica a condição do usuário para votar

    :param a: ano de nascimento
    :type a: int
    :return: situação para votação
    :rtype: str
    """
    idade = date.today().year - a
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


if __name__ == '__main__':
    cabecalho('Funções para votação')

    print('''\tfrom datetime import date
    from funcoes import cabecalho, verificador
    
    
    def voto(a):
    idade = date.today().year - a
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO
    
    
    ano = verificador('Em que ano você nasceu? ')
    print(f'Com {date.today().year - ano} anos: VOTO {voto(ano)}')
    ''')
    ano = verificador('Em que ano você nasceu? ')
    print(f'Com {date.today().year - ano} anos: VOTO {voto(ano)}')
