"""15_ex069_analise_dados_grupo.py em 2018-12-17. Projeto Curso em Video.

Análise de dados do grupo

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar.

No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.

"""
from funcoes import cabecalho, verificador, questao

if __name__ == '__main__':
    cabecalho('Análise de dados do grupo')

    print('''\tfrom funcoes import cabecalho, verificador, questao
    
    ci = cm = cf = 0
    while True:
        print('-' * 25)
        print('Cadastre uma pessoa'.center(25).upper())
        print('-' * 25)
        idade = verificador('Idade: ')
        sexo = questao('Sexo: [M/F] ', 'MF')
        if idade > 18:
            ci += 1
        if sexo == 'M':
            cm += 1
        if sexo == 'F' and idade < 20:
            cf += 1
        print('-' * 25)
        continuar = questao('Que continuar? [S/N] ', 'SN')
        if continuar == 'N':
            print('-' * 25)
            print(f'Total de pessoas com mais de 18 anos: {ci}')
            print(f'Ao todo temos {cm} home{"ns" if cm > 1 else "m"} cadastrado{"s" if cm > 1 else ""}.')
            print(f'E temos {cf} mulher{"es" if cf > 1 else ""} com menos de 20 anos.')
            break
    ''')
    ci = cm = cf = 0
    while True:
        print('-' * 25)
        print('Cadastre uma pessoa'.center(25).upper())
        print('-' * 25)
        idade = verificador('Idade: ')
        sexo = questao('Sexo: [M/F] ', 'MF')
        if idade > 18:
            ci += 1
        if sexo == 'M':
            cm += 1
        if sexo == 'F' and idade < 20:
            cf += 1
        print('-' * 25)
        continuar = questao('Que continuar? [S/N] ', 'SN')
        if continuar == 'N':
            print('-' * 25)
            print(f'Total de pessoas com mais de 18 anos: {ci}')
            print(f'Ao todo temos {cm} home{"ns" if cm > 1 else "m"} cadastrado{"s" if cm > 1 else ""}.')
            print(f'E temos {cf} mulher{"es" if cf > 1 else ""} com menos de 20 anos.')
            break
