"""14_ex065_maior_menor_valores.py em 2018-12-17. Projeto Curso em Video.

Maior e Menor valores

Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve repostar ao usuário se ele quer ou não continuar a digitar valores.

"""
from funcoes import cabecalho, verificador, questao

if __name__ == '__main__':
    cabecalho('Maior e Menor valores')

    print('''\tfrom funcoes import cabecalho, verificador, questao
    
    maior = menor = c = s = m = 0
    reposta = 'S'
    while reposta in 'S':
        n = verificador('Digite um número: ')
        if c == 0:
            maior = menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
        s += n
        c += 1
        m = s / c
        reposta = questao('Quer continuar? [S/N] ', 'SN')
    print(f'Você digitou {c} número(s) e a média foi {m}.')
    print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
    ''')
    maior = menor = c = s = m = 0
    reposta = 'S'
    while reposta in 'S':
        n = verificador('Digite um número: ')
        if c == 0:
            maior = menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
        s += n
        c += 1
        m = s / c
        reposta = questao('Quer continuar? [S/N] ', 'SN')
    print(f'Você digitou {c} número{"s" if c > 1 else ""} e a média foi {m}.')
    print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
