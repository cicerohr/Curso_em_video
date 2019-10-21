"""17_ex080_lista_ordenada_sem_repeticoes.py em 2018-12-20. Projeto Curso em Video.

Lista ordenada sem repetições

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Lista ordenada sem repetições')

    print('''\tfrom funcoes import cabecalho, verificador
    
    numeros = []
    for i in range(0, 5):
        valor = verificador('Digite um valor: ')
        if not numeros:
            numeros.insert(-1, valor)
            print('O 1° número foi adicionado à lista.')
        elif valor > max(numeros):
            numeros.insert(len(numeros), valor)
            print('Adicionado ao final da lista...')
        elif valor < min(numeros):
            numeros.insert(0, valor)
            print('Adicionado na posição 0 da lista...')
        else:
            for v in numeros:
                if valor <= v:
                    indice = numeros.index(v)
                    numeros.insert(indice, valor)
                    print(f'Adicionado na posição {indice} da lista...')
                    break
    print('-=' * 25, '\\n', f'Os valores digitados em ordem foram {numeros}', sep='')
    ''')
    numeros = []
    for i in range(0, 5):
        valor = verificador('Digite um valor: ')
        if not numeros:
            numeros.insert(-1, valor)
            print('O 1° número foi adicionado à lista.')
        elif valor > max(numeros):
            numeros.insert(len(numeros), valor)
            print('Adicionado ao final da lista...')
        elif valor < min(numeros):
            numeros.insert(0, valor)
            print('Adicionado na posição 0 da lista...')
        else:
            for v in numeros:
                if valor <= v:
                    indice = numeros.index(v)
                    numeros.insert(indice, valor)
                    print(f'Adicionado na posição {indice} da lista...')
                    break
    print('-=' * 25, '\n', f'Os valores digitados em ordem foram {numeros}', sep='')
