"""15_ex070_estatisticas_produtos.py em 2018-12-18. Projeto Curso em Video.

Estatísticas em produtos

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário se vai continuar ou não.

No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$ 1000,00.
C) qual é o nome do produto mais barato.

"""
from funcoes import cabecalho, questao, verificador

if __name__ == '__main__':
    cabecalho('Estatísticas em produtos')

    print('''\tfrom funcoes import cabecalho, questao, verificador
    
    total = c = 0
    barato = ['', 0]
    print('-' * 40)
    print('Loja Super Baratão'.center(40).upper())
    print('-' * 40)
    while True:
        produto = str(input('Nome do produto: ')).strip().capitalize()
        preco = verificador('Preço: R$ ')
        if barato[1] == 0 or barato[1] > preco:
            barato[0] = produto
            barato[1] = preco
        total += preco
        if preco > 1000:
            c += 1
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            print(' Fim do programa '.center(40, '-').upper())
            print(f'O total da compra foi R$ {total:.2f}.')
            print(f'Temos {c} custando mais de R$ 1000.00.')
            print(f'O produto mais barato foi {barato[0]} que custa R$ {barato[1]:.2f}.')
            break
    ''')
    total = c = 0
    barato = ['', 0]
    print('-' * 40)
    print('Loja Super Baratão'.center(40).upper())
    print('-' * 40)
    while True:
        produto = str(input('Nome do produto: ')).strip().capitalize()
        preco = verificador('Preço: R$ ')
        if barato[1] == 0 or barato[1] > preco:
            barato[0] = produto
            barato[1] = preco
        total += preco
        if preco > 1000:
            c += 1
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            print(' Fim do programa '.center(40, '-').upper())
            print(f'O total da compra foi R$ {total:.2f}.')
            print(f'Temos {c} custando mais de R$ 1000.00.')
            print(f'O produto mais barato foi {barato[0]} que custa R$ {barato[1]:.2f}.')
            break
