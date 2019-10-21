"""14_ex060_calculo_fatorial.py em 2018-12-16. Projeto Curso em Video.

Cálculo do Fatorial

Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Cálculo do Fatorial')

    print('''\tfrom funcoes import cabecalho, verificador
    
    mostra = ''
    m = 1
    fatorial = verificador('Digite um número para\\n calcular seu fatorial: ')
    for k in range(fatorial, 0, -1):
        m *= k
        mostra += f'{k}{" x " if k != 1 else " = "}'
    print(f'Calculando {fatorial}! = {mostra}{m}')
    ''')
    mostra = ''
    m = 1
    fatorial = verificador('Digite um número para\ncalcular seu fatorial: ')
    for k in range(fatorial, 0, -1):
        m *= k
        mostra += f'{k}{" x " if k != 1 else " = "}'
    print(f'Calculando {fatorial}! = {mostra}{m}')
