"""17_ex079_valores_unicos_lista.py em 2018-12-20. Projeto Curso em Video.

Valores únicos em uma Lista

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

"""
from funcoes import cabecalho, verificador, ansi, questao

if __name__ == '__main__':
    cabecalho('Valores únicos em uma Lista')

    print('''\tfrom funcoes import cabecalho, verificador, ansi, questao
    
    numeros = []
    while True:
        numero = verificador('Digite um valor: ')
        if numero not in numeros:
            numeros.append(numero)
            print(f'{ansi("bold", "verde")}Valor adicionado com sucesso!{ansi()}')
        else:
            print(f'{ansi("bold", "vermelho")}Valor duplicado! Não vou adicionar!{ansi()}')
        pergunta = questao('Quer continuar? [S/N] ', 'SN')
        if pergunta == 'N':
            print('-=' * 20, '\\n', f'Você digitou {"os valores" if len(numeros) > 1 else "o valor"} {sorted(numeros)}',
                  sep='')
            break
    ''')
    numeros = []
    while True:
        numero = verificador('Digite um valor: ')
        if numero not in numeros:
            numeros.append(numero)
            print(f'{ansi("bold", "verde")}Valor adicionado com sucesso!{ansi()}')
        else:
            print(f'{ansi("bold", "vermelho")}Valor duplicado! Não vou adicionar!{ansi()}')
        pergunta = questao('Quer continuar? [S/N] ', 'SN')
        if pergunta == 'N':
            print('-=' * 20, '\n', f'Você digitou {"os valores" if len(numeros) > 1 else "o valor"} {sorted(numeros)}',
                  sep='')
            break
