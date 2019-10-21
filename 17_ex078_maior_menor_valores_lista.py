"""17_ex078_maior_menor_valores_lista.py em 2018-12-20. Projeto Curso em Video.

Maior e Menor valores na Lista

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Maior e Menor valores na Lista')

    print('''\tfrom funcoes import cabecalho, verificador
    
    numeros = list()
    maior = menor = ''
    conta_M = conta_m = 0
    for i in range(0, 5):
        numeros.append(verificador(f'Digite um valor para o índice {i}: '))
    for k, v in enumerate(numeros):
        if v == max(numeros):
            maior += f'{str(k)}...'
            conta_M += 1
        if v == min(numeros):
            menor += f'{str(k)}...'
            conta_m += 1
    print('=-' * 25, '\\n', f'Você digitou os valores {numeros}', sep='')
    print(f'O maior valor digitado foi {max(numeros)} {"nas posições" if conta_M > 1 else "na posição"} {maior}')
    print(f'O menor valor digitado foi {min(numeros)} {"nas posições" if conta_m > 1 else "na posição"} {menor}',
          '\\n', '=-' * 25, sep='')
    ''')
    numeros = list()
    maior = menor = ''
    conta_M = conta_m = 0
    for i in range(0, 5):
        numeros.append(verificador(f'Digite um valor para o índice {i}: '))
    for k, v in enumerate(numeros):
        if v == max(numeros):
            maior += f'{str(k)}...'
            conta_M += 1
        if v == min(numeros):
            menor += f'{str(k)}...'
            conta_m += 1
    print('=-' * 25, '\n', f'Você digitou os valores {numeros}', sep='')
    print(f'O maior valor digitado foi {max(numeros)} {"nas posições" if conta_M > 1 else "na posição"} {maior}')
    print(f'O menor valor digitado foi {min(numeros)} {"nas posições" if conta_m > 1 else "na posição"} {menor}',
          '\n', '=-' * 25, sep='')
