"""12_ex036_aprovando_emprestimo.py em 2018-12-14. Projeto Curso em Video.

Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Aprovando Empréstimo')

    print('''\tfrom funcoes import cabecalho, ansi, verificador
    
    casa = verificador('Valor da casa: R$ ', float)
    salario = verificador('Salário do comprador: R$ ', float)
    anos = verificador('Quantos anos de financiamento: ')
    prestacao = casa / (anos * 12)
    print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}')
    if prestacao > salario * 0.3:
        print(f'{ansi("bold", "vermelho")}Empréstimo Negado!{ansi()}')
    else:
        print(f'{ansi("bold", "verde")}Empréstimo pode ser concedido!{ansi()}')
    ''')
    casa = verificador('Valor da casa: R$ ', float)
    salario = verificador('Salário do comprador: R$ ', float)
    anos = verificador('Quantos anos de financiamento: ')
    prestacao = casa / (anos * 12)
    print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}')
    if prestacao > salario * 0.3:
        print(f'{ansi("bold", "vermelho")}Empréstimo Negado!{ansi()}')
    else:
        print(f'{ansi("bold", "verde")}Empréstimo pode ser concedido!{ansi()}')
