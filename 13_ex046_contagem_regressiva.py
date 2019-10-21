"""13_ex046_contagem_regressiva.py em 2018-12-14. Projeto Curso em Video.

Contagem regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.

"""
from time import sleep
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Contagem regressiva')

    print('''\tfrom time import sleep
    
    for k in range(10, -1, -1):
        print(k, flush=True)
        sleep(1)
    print('Bum! Bum! Pooow!')
    ''')
    for k in range(10, -1, -1):
        print(k, flush=True)
        sleep(1)
    print('Bum! Bum! Pooow!')
