"""18_ex085_listas_pares_impares.py em 2018-12-20. Projeto Curso em Video.

Listas com pares e ímpares

Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Listas com pares e ímpares')

    print('''\tfrom funcoes import cabecalho, verificador
    
    numeros = [[], []]
    for k in range(1, 8):
        numero = verificador(f'Digite o {k}° número: ')
        if numero % 2 == 0:
            numeros[0].append(numero)
        else:
            numeros[1].append(numero)
    numeros[0].sort()
    numeros[1].sort()
    print('-=' * 30, '\\n', f'Os valores pares digitados foram: {numeros[0]}', sep='')
    print(f'Os valores ímpares digitados foram: {numeros[1]}')
    ''')
    numeros = [[], []]
    for k in range(1, 8):
        numero = verificador(f'Digite o {k}° número: ')
        if numero % 2 == 0:
            numeros[0].append(numero)
        else:
            numeros[1].append(numero)
    numeros[0].sort()
    numeros[1].sort()
    print('-=' * 30, '\n', f'Os valores pares digitados foram: {numeros[0]}', sep='')
    print(f'Os valores ímpares digitados foram: {numeros[1]}')
