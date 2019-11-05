"""

Manipulando arquivo de texto em um sistema modularizado

Crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções:
    - cadastrar uma nova pessoa;
    - listar todas as pessoas cadastradas.

"""
from ex115.lib.interface import *
from ex115.lib.arquivo import *

cria_cabecalho(4, '=')

destino = 'cadastro.txt'
if arquivo_existe(destino):
    while True:
        mostra_menu()
        opcao = verificador(f'{ansi("amarelo", "bold")}Sua opção:{ansi()} ')
        if opcao == 1:
            le_arquivo(destino)
        elif opcao == 2:
            escreve_arquivo(destino)
        elif opcao == 3:
            cria_cabecalho(3)
            break
        else:
            print(f'{ansi("vermelho", "bold")}ERRO! Digite uma opção válida. Tente novamente!{ansi()}')
            continue
