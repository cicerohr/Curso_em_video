"""12_ex044_gerenciador_pagamentos.py em 2018-12-14. Projeto Curso em Video.

Gerenciador de Pagamentos

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Gerenciador de Pagamentos')

    print('''\tfrom funcoes import cabecalho, ansi, verificador
    
    menu = {1: 'à vista dinheiro/cheque', 2: 'à vista no cartão', 3: '2x no cartão', 4: '3x ou mais no cartão'}
    preco = verificador('Preço das compras: [R$] ', float)
    print('\\nForma de pagamento'.upper())
    for k, v in menu.items():
        print(f'[{k}] {v}')
    opcao = verificador('\\nQual a opção? ')
    if opcao == 1:
        print(f'Sua compra de R$ {preco:.2f} vai custar R$ {preco * 0.9:.2f} no final.')
    elif opcao == 2:
        print(f'Sua compra de R$ {preco:.2f} vai custar R$ {preco * 0.95:.2f} no final.')
    elif opcao == 3:
        print(f'Sua compra de R$ {preco:.2f} será parcelada em 2x de R$ {preco / 2:.2f} sem juros.')
    elif opcao == 4:
        while True:
            parcelas = verificador('Quantas parcelas? ')
            if parcelas >= 3:
                print(f'Sua compra será parcelada em {parcelas}x de R$ {(preco * 1.2) / parcelas:.2f} com juros.')
                print(f'Sua compra de R$ {preco:.2f} vai custar {preco * 1.2:.2f} no final.')
                break
            else:
                print(f'{ansi("vermelho")}Digite pelo menos 3 parcelas. Tente novamente!{ansi()}')
    else:
        preco = 0
        print(f'{ansi("vermelho")}Opção inválida de pagamento. Tente novamente!{ansi()}')
    ''')
    menu = {1: 'à vista dinheiro/cheque', 2: 'à vista no cartão', 3: '2x no cartão', 4: '3x ou mais no cartão'}
    preco = verificador('Preço das compras: [R$] ', float)
    print('\nForma de pagamento'.upper())
    for k, v in menu.items():
        print(f'[{k}] {v}')
    opcao = verificador('\nQual a opção? ')
    if opcao == 1:
        print(f'Sua compra de R$ {preco:.2f} vai custar R$ {preco * 0.9:.2f} no final.')
    elif opcao == 2:
        print(f'Sua compra de R$ {preco:.2f} vai custar R$ {preco * 0.95:.2f} no final.')
    elif opcao == 3:
        print(f'Sua compra de R$ {preco:.2f} será parcelada em 2x de R$ {preco / 2:.2f} sem juros.')
    elif opcao == 4:
        while True:
            parcelas = verificador('Quantas parcelas? ')
            if parcelas >= 3:
                print(f'Sua compra será parcelada em {parcelas}x de R$ {(preco * 1.2) / parcelas:.2f} com juros.')
                print(f'Sua compra de R$ {preco:.2f} vai custar {preco * 1.2:.2f} no final.')
                break
            else:
                print(f'{ansi("vermelho")}Digite pelo menos 3 parcelas. Tente novamente!{ansi()}')
    else:
        preco = 0
        print(f'{ansi("vermelho")}Opção inválida de pagamento. Tente novamente!{ansi()}')
