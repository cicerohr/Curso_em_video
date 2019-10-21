"""12_ex043_indice_massa_corporal.py em 2018-12-14. Projeto Curso em Video.

Índice de Massa Corporal

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida


O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que
a massa está em quilogramas e a altura em metros.

IMC = massa / altura²

Classificação
O resultado é comparado com uma tabela que indica o grau de obesidade do indivíduo:

IMC	        Classificação do IMC
< 16	        Magreza grave
16 a < 17	    Magreza moderada
17 a < 18,5	    Magreza leve
18,5 a < 25	    Saudável
25 a < 30	    Sobrepeso
30 a < 35	    Obesidade Grau I
35 a < 40	    Obesidade Grau II (severa)
> 40	        Obesidade Grau III (mórbida)

Fonte: https://pt.wikipedia.org/wiki/Índice_de_massa_corporal#Cálculo

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Índice de Massa Corporal')

    print('''\tm = verificador('Qual é sua massa? [kg] ', float)
    h = verificador('Qual é sua altura? [m] ', float)
    imc = m / pow(h, 2)
    print(f'O IMC é de {imc:.1f}.')
    print('Sua classificação: ', end='')
    if imc < 16:
        print('Magreza grave'.upper())
    elif 16 <= imc < 17:
        print('Magreza moderada'.upper())
    elif 17 <= imc < 18.5:
        print('Magreza leve'.upper())
    elif 18.5 <= imc < 25:
        print('Saudável'.upper())
    elif 25 <= imc < 30:
        print('Sobrepeso'.upper())
    elif 30 <= imc < 35:
        print('Obesidade Grau I'.upper())
    elif 35 <= imc < 40:
        print('Obesidade Grau II (severa)'.upper())
    else:
        print('Obesidade Grau III (mórbida)'.upper())
    ''')
    m = verificador('Qual é sua massa? [kg] ', float)
    h = verificador('Qual é sua altura? [m] ', float)
    imc = m / pow(h, 2)
    print(f'O IMC é de {imc:.1f}.')
    print('Sua classificação: ', end='')
    if imc < 16:
        print('Magreza grave'.upper())
    elif 16 <= imc < 17:
        print('Magreza moderada'.upper())
    elif 17 <= imc < 18.5:
        print('Magreza leve'.upper())
    elif 18.5 <= imc < 25:
        print('Saudável'.upper())
    elif 25 <= imc < 30:
        print('Sobrepeso'.upper())
    elif 30 <= imc < 35:
        print('Obesidade Grau I'.upper())
    elif 35 <= imc < 40:
        print('Obesidade Grau II (severa)'.upper())
    else:
        print('Obesidade Grau III (mórbida)'.upper())
