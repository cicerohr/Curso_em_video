"""15_ex066_varios_numeros_com_flag.py em 2018-12-17. Projeto Curso em Video.

Vários números com flag

Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre elas (desconsiderando o flag).

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Vários números com flag')

    print('''\tfrom funcoes import cabecalho, verificador
    
    c = s = 0
    while True:
        n = verificador('Digite um valor (999 para sair):  ')
        if n == 999:
            print(f'A soma dos {c} valor(es) foi {s}!')
            break
        s += n
        c += 1
    ''')
    c = s = 0
    while True:
        n = verificador('Digite um valor (999 para sair):  ')
        if n == 999:
            print(f'A soma dos {c} valor(es) foi {s}!')
            break
        s += n
        c += 1
