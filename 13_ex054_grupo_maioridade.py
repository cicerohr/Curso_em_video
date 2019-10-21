"""13_ex054_grupo_maioridade.py em 2018-12-16. Projeto Curso em Video.

Grupo da Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""
from datetime import datetime
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Grupo da Maioridade')

    print('''\tfrom datetime import datetime
    from cicero import cabecalho, verificador
    
    conta = 0
    ano_hoje = datetime.today().year
    for k in range(1, 8):
        an = verificador(f'Em que ano nasceu a {k}ª pessoa? ')
        idade = ano_hoje - an
        if idade > 21:
            conta += 1
    print(f'Ao todo tivemos {conta} pessoas maiores e {7 - conta} menores de idade.')
    ''')
    conta = 0
    ano_hoje = datetime.today().year
    for k in range(1, 8):
        an = verificador(f'Em que ano nasceu a {k}ª pessoa? ')
        idade = ano_hoje - an
        if idade > 21:
            conta += 1
    print(f'Ao todo tivemos {conta} pessoas maiores e {7 - conta} menores de idade.')
