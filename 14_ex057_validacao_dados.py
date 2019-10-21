"""14_ex057_validacao_dados.py em 2018-12-16. Projeto Curso em Video.

Validação de Dados

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Validação de Dados')

    print('''\t while True:
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
        if sexo not in 'MF':
            print('Digite apenas M ou F. Tente novamente!')
        else:
            print(f'Sexo {sexo} registrado com sucesso.')
            break
    ''')
    while True:
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
        if sexo not in 'MF':
            print('Digite apenas M ou F. Tente novamente!')
        else:
            print(f'Sexo {sexo} registrado com sucesso.')
            break
