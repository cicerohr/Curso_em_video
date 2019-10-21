"""10_ex031_custo_viagem.py em 2018-12-13. Projeto Curso em Video.

Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km
para viagens de até 200km e R$0,45 parta viagens mais longas.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Custo da Viagem')

    print("""\tfrom cicero import cabecalho, verificador
    
    distancia = abs(verificador('Qual é a distância da sua viagem? ', float))
    print(f'Você esta preste a começar a sua viagem de {distancia}km.')
    print(f'E o preço da sua passagem será de R$ ', end='')
    if distancia <= 200:
        print(f'{distancia * 0.5:.2f}.')
    else:
        print(f'{distancia * 0.45:.2f}.')
    """)
    distancia = abs(verificador('Qual é a distância da sua viagem? ', float))
    print(f'Você esta preste a começar a sua viagem de {distancia}km.')
    print(f'E o preço da sua passagem será de R$ ', end='')
    if distancia <= 200:
        print(f'{distancia * 0.5:.2f}.')
    else:
        print(f'{distancia * 0.45:.2f}.')
