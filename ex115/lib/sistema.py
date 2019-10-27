from ex115.lib.interface import *

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
