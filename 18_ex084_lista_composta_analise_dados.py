"""18_ex084_lista_composta_analise_dados.py em 2018-12-20. Projeto Curso em Video.

Lista composta e análise de dados

Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

"""
from funcoes import cabecalho, verificador, questao

if __name__ == '__main__':
    cabecalho('Lista composta e análise de dados')

    print('''\tfrom funcoes import cabecalho, verificador, questao
    
    pessoas = list()
    pessoa = list()
    maior = list()
    menor = list()
    while True:
        pessoa.append(str(input('Nome: ')).strip().title())
        pessoa.append(verificador('Massa: [kg] ', float))
        pessoas.append(pessoa[:])
        pessoa.clear()
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            break
    for p in pessoas:
        if not maior and not menor:
            maior.append(p[:])
            menor.append(p[:])
        else:
            if p[1] >= maior[0][1]:
                if p[1] > maior[0][1]:
                    maior.clear()
                maior.append(p[:])
            if p[1] <= menor[0][1]:
                if p[1] < menor[0][1]:
                    menor.clear()
                menor.append(p[:])
    print('-=' * 30, '\\n', f'Ao todo você cadastrou {len(pessoas)} pessoas.', sep='')
    print(f'O maior peso foi de {maior[0][1]}kg. Peso de {[maior[x][0] for x in range(len(maior))]}')
    print(f'O menor peso foi de {menor[0][1]}kg. Peso de {[menor[x][0] for x in range(len(menor))]}')
    ''')
    pessoas = list()
    pessoa = list()
    maior = list()
    menor = list()
    while True:
        pessoa.append(str(input('Nome: ')).strip().title())
        pessoa.append(verificador('Massa: [kg] ', float))
        pessoas.append(pessoa[:])
        pessoa.clear()
        continuar = questao('Quer continuar? [S/N] ', 'SN')
        if continuar == 'N':
            break
    for p in pessoas:
        if not maior and not menor:
            maior.append(p[:])
            menor.append(p[:])
        else:
            if p[1] >= maior[0][1]:
                if p[1] > maior[0][1]:
                    maior.clear()
                maior.append(p[:])
            if p[1] <= menor[0][1]:
                if p[1] < menor[0][1]:
                    menor.clear()
                menor.append(p[:])
    print('-=' * 30, '\n', f'Ao todo você cadastrou {len(pessoas)} pessoas.', sep='')
    print(f'O maior peso foi de {maior[0][1]}kg. Peso de {[maior[x][0] for x in range(len(maior))]}')
    print(f'O menor peso foi de {menor[0][1]}kg. Peso de {[menor[x][0] for x in range(len(menor))]}')
