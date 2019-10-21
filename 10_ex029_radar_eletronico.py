"""10_ex029_radar_eletronico.py em 2018-12-13. Projeto Curso em Video.

Radar eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Radar eletrônico')

    print("""\tfrom cicero import cabecalho, verificador, ansi
    
    velocidade = abs(verificador('Qual é a velocidade atual do carro?  ', float))
    if velocidade > 80:
        print(f'{ansi("bold", "vermelho")}Multado! Você excedeu o limite permitido que é de 80km/h.')
        print(f'Você deve pagar uma multa de R$ {(velocidade - 80) * 7:.2f}!{ansi()}')
    print(f'{ansi("amarelo")}Tenha um bom dia! Dirija com segurança!{ansi()}')
    """)
    velocidade = abs(verificador('Qual é a velocidade atual do carro?  ', float))
    if velocidade > 80:
        print(f'{ansi("bold", "vermelho")}Multado! Você excedeu o limite permitido que é de 80km/h.')
        print(f'Você deve pagar uma multa de R$ {(velocidade - 80) * 7:.2f}!{ansi()}')
    print(f'{ansi("amarelo")}Tenha um bom dia! Dirija com segurança!{ansi()}')
