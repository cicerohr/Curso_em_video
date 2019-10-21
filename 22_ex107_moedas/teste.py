"""teste.py em 2019-04-29. Projeto Curso em Video.



"""
from funcoes.strings import cabecalho
import moeda

if __name__ == '__main__':
    cabecalho('Aumentar, diminuir, dobro e metade')

    p = float(input('Digite o preço: R$ '))
    print(f'A medade de R$ {p} é R$ {moeda.metade(p)}.')
    print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}.')
    print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}.')
    print(f'Reduzindo 13%, temos R$ {moeda.diminuir(p, 13)}.')
