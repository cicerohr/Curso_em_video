"""10_ex033_maior_menor_valores.py em 2018-12-14. Projeto Curso em Video.

Maior e menor valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Maior e menor valores')

    print('''\tfrom cicero import cabecalho, so_numero
    
    valores = list()
    for k in range(1, 4):
        valor = verificador(f'{k}° valor: ')
        valores.append(valor)
    print(f'valores => {valores}')
    print(f'O menor valor digitado foi {min(valores)}')
    print(f'O maior valor digitado foi {max(valores)}')
    ''')
    valores = list()
    for k in range(1, 4):
        valor = verificador(f'{k}° valor: ')
        valores.append(valor)
    print(f'valores => {valores}')
    print(f'O menor valor digitado foi {min(valores)}')
    print(f'O maior valor digitado foi {max(valores)}')
