"""13_ex056_analisador_completo.py em 2018-12-16. Projeto Curso em Video.

Analisador completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- a média de idade do grupo;
- qual é o nome do homem mais velho;
- quantas mulheres têm menos de 20 anos.

"""
from funcoes import cabecalho, verificador, questao

if __name__ == '__main__':
    cabecalho('Analisador completo')

    print('''\tfrom cicero import cabecalho, verificador, questao
    
    nome = sexo = n_velho = ''
    idade = s_idades = s_sexos = i_velho = 0
    for k in range(1, 5):
        print()
        print(f' {k}ª pessoa '.center(30, '-'))
        nome = str(input('Nome: ')).strip().title()
        idade = verificador('Idade: ')
        sexo = questao('Sexo: [M/F] ', 'MF')
        s_idades += idade
        if i_velho == 0 and sexo == 'M':
            i_velho = idade
            n_velho = nome
        elif idade > i_velho and sexo == 'M':
            i_velho = idade
            n_velho = nome
        if sexo == 'F' and idade < 20:
            s_sexos += 1
    print(f'\\nA média de idade do grupo é de {s_idades / 4} anos.')
    if i_velho != 0:
        print(f'O homem mais velho tem {i_velho} anos e se chama {n_velho}.')
    print(f'Ao todo temos {s_sexos if s_sexos != 0 else "nenhuma"} mulher{"es" if s_sexos > 1 else ""} '
          f'com menos de 20 anos.')
    ''')
    nome = sexo = n_velho = ''
    idade = s_idades = s_sexos = i_velho = 0
    for k in range(1, 5):
        print()
        print(f' {k}ª pessoa '.center(30, '-'))
        nome = str(input('Nome: ')).strip().title()
        idade = verificador('Idade: ')
        sexo = questao('Sexo: [M/F] ', 'MF')
        s_idades += idade
        if i_velho == 0 and sexo == 'M':
            i_velho = idade
            n_velho = nome
        elif idade > i_velho and sexo == 'M':
            i_velho = idade
            n_velho = nome
        if sexo == 'F' and idade < 20:
            s_sexos += 1
    print(f'\nA média de idade do grupo é de {s_idades / 4} anos.')
    if i_velho != 0:
        print(f'O homem mais velho tem {i_velho} anos e se chama {n_velho}.')
    print(f'Ao todo temos {s_sexos if s_sexos != 0 else "nenhuma"} mulher{"es" if s_sexos > 1 else ""} '
          f'com menos de 20 anos.')
