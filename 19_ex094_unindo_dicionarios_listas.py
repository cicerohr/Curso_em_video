"""19_ex094_unindo_dicionarios_listas.py em 2018-12-22. Projeto Curso em Video.

Unindo dicionários e listas

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média

"""
from funcoes import cabecalho, questao, verificador

if __name__ == '__main__':
    cabecalho('Unindo dicionários e listas')

    print('''\tfrom funcoes import cabecalho, questao, verificador
    
    pessoa = dict(nome='', sexo='', idade=0)
    pessoas = list()
    mulheres = list()
    soma = media = 0
    while True:
        pessoa['nome'] = str(input('Nome: ')).strip().title()
        pessoa['sexo'] = questao('Sexo: [M/F] ', 'MF')
        pessoa['idade'] = verificador('Idade: ')
        soma += pessoa['idade']
        if pessoa['sexo'] == 'F':
            mulheres.append(pessoa['nome'])
        pessoas.append(pessoa.copy())
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            media = soma / len(pessoas)
            print('-=' * 30)
            print(f'A) ao todo temos {len(pessoas)} pessoa{"s" if len(pessoas) > 1 else ""} no cadastro.')
            print(f'B) a média de idade é de {media:5.2f} anos.')
            print(
                f'C) {"as mulheres cadastradas foram" if len(mulheres) > 1 else "a mulher cadastrada foi"} {mulheres}.')
            print(f'D) a lista de pessoas acima da média são:')
            for v in pessoas:
                if v['idade'] >= media:
                    print(f'\\tnome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]}')
            break
    ''')
    pessoa = dict(nome='', sexo='', idade=0)
    pessoas = list()
    mulheres = list()
    soma = media = 0
    while True:
        pessoa['nome'] = str(input('Nome: ')).strip().title()
        pessoa['sexo'] = questao('Sexo: [M/F] ', 'MF')
        pessoa['idade'] = verificador('Idade: ')
        soma += pessoa['idade']
        if pessoa['sexo'] == 'F':
            mulheres.append(pessoa['nome'])
        pessoas.append(pessoa.copy())
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            media = soma / len(pessoas)
            print('-=' * 30)
            print(f'A) ao todo temos {len(pessoas)} pessoa{"s" if len(pessoas) > 1 else ""} no cadastro.')
            print(f'B) a média de idade é de {media:5.2f} anos.')
            print(
                f'C) {"as mulheres cadastradas foram" if len(mulheres) > 1 else "a mulher cadastrada foi"} {mulheres}.')
            print(f'D) a lista de pessoas acima da média são:')
            for v in pessoas:
                if v['idade'] >= media:
                    print(f'\tnome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]}')
            break
