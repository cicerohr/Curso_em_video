"""ex_115_cadastrar_listar_pessoas em 2019-07-16. Projeto Curso em Video.

Manipulando arquivo de texto

Crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções:
    - cadastrar uma nova pessoa;
    - listar todas as pessoas cadastradas.

"""
from ex_115_modularizado.lib.interface import *
from ex_115_modularizado.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    reposta = menu(['Listar Pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if reposta == 1:
        ler_arquivo(arq)
    elif reposta == 2:
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = verificador('Idade: ')
        cadastrar(arq, nome, idade)
    elif reposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'{ansi("vermelho")}ERRO! Digite uma opção válida!{ansi()}')
    sleep(2)
