"""10_ex034_aumentos_multiplos.py em 2018-12-14. Projeto Curso em Video.

Aumentos múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento:

- para salários superiores a R$1250,00, calcule um aumento de 10%;
- para os inferiores ou iguais, o aumento é de 15%.

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Aumentos múltiplos')

    print('''\tsalario = verificador('Qual o salário do funcionário? R$ ')
    print(f'Quem ganhava {ansi("underline")}R$ {salario:.2f}{ansi()} passa a ganhar{ansi("bold", "verde")}', end=' ')
    if salario > 1250:
        print(f'R$ {salario * 1.10:.2f}{ansi()} agora.')
    else:
        print(f'R$ {salario * 1.15:.2f}{ansi()} agora.')
    ''')
    salario = verificador('Qual o salário do funcionário? R$ ')
    print(f'Quem ganhava {ansi("underline")}R$ {salario:.2f}{ansi()} passa a ganhar{ansi("bold", "verde")}', end=' ')
    if salario > 1250:
        print(f'R$ {salario * 1.10:.2f}{ansi()} agora.')
    else:
        print(f'R$ {salario * 1.15:.2f}{ansi()} agora.')
