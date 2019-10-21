"""12_ex040_aquele_classico_media.py em 2018-12-14. Projeto Curso em Video.

Aquele clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Aquele clássico da Média')

    print('''\tfrom cicero import cabecalho, ansi, verificador
    
    n1 = verificador('Primeira nota: ', float)
    n2 = verificador('Segunda nota: ', float)
    media = n1 + n2 / 2
    print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}.')
    print(f'O aluno está', end=' ')
    if 5.0 <= media < 7.0:
        print(f'em {ansi("bold", "amarelo")}RECUPERAÇÃO{ansi()}.')
    elif media >= 7.0:
        print(f'{ansi("bold", "cyan")}APROVADO{ansi()}.')
    else:
        print(f'{ansi("bold", "vermelho")}REPROVADO{ansi()}.')
    ''')
    n1 = verificador('Primeira nota: ', float)
    n2 = verificador('Segunda nota: ', float)
    media = n1 + n2 / 2
    print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}.')
    print(f'O aluno está', end=' ')
    if 5.0 <= media < 7.0:
        print(f'em {ansi("bold", "amarelo")}RECUPERAÇÃO{ansi()}.')
    elif media >= 7.0:
        print(f'{ansi("bold", "cyan")}APROVADO{ansi()}.')
    else:
        print(f'{ansi("bold", "vermelho")}REPROVADO{ansi()}.')
