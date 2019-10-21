"""07_ex013_reajuste_salarial.py em 2018-12-10. Projeto Curso em Video.

Reajuste Salarial

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Reajuste Salarial')

    print('''\ts = verificador('Qual é o salário do funcionário? R$ ')
    print(f'Um funcionário que ganhava R$ {s:.2f}, com 15% de aumento, passa a receber R$ {s * 1.15:.2f}')
    ''')
    s = verificador('Qual é o salário do funcionário? R$ ')
    print(f'Um funcionário que ganhava R$ {s:.2f}, com 15% de aumento, passa a receber R$ {s * 1.15:.2f}')
