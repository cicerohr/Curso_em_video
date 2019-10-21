"""14_ex064_tratando_varios_valores_1.py em 2018-12-17. Projeto Curso em Video.

Tratando vários valores v1.0

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Tratando vários valores v1.0')

    print('''\tfrom funcoes import cabecalho, verificador
    
    while True:
        n = verificador('Digite um número [999 para sair]: ')
        if n == 999:
            print(f'Você digitou {c} números e a soma entre eles é {s}.')
            break
        s += n
        c += 1
    ''')
    c = s = 0
    while True:
        n = verificador('Digite um número [999 para sair]: ')
        if n == 999:
            print(f'Você digitou {c} números e a soma entre eles é {s}.')
            break
        s += n
        c += 1
