"""09______manipulando_texto.py em 2018-12-05. Projeto Curso em Video.

Manipulando Texto

Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são
o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(),
capitalize(), title(), strip(), junção com join().

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Manipulando Texto', 120)

    cabecalho('Fatiamento de string', 120, '-')
    frase = 'Curso em Vídeo Python'
    print(f'frase = {frase}')
    print('        012345678901234567890  (índices)')
    print('                                                            variavel[start, stop, step]\n')
    print(f'Índice 9 da frase:                                          frase[9] => "{frase[9]}"')
    print(f'Somente a palavra "Vídeo":                                  frase[9:14] => "{frase[9:14]}"')
    print(f'Fatiamento da frase do 9 índice ao 21 pulando de 2 em 2:    frase[9:21:2] => "{frase[9:21:2]}"')
    print(f'Quando omitido o início começa do índice 0:                 frase[:5] => "{frase[:5]}"')
    print(f'Quando omitido o fim começa do índice até o final:          frase[15:] => "{frase[15:]}"')
    print(f'Do índice 9 até o final de 3 em 3:                          frase[9::3] => "{frase[9::3]}"')
    print(f'Inverte a frase:                                            frase[::-1] => "{frase[::-1]}"')

    cabecalho('Análise da string', 120, '-')
    print(f'Mostra a quantidade de caracteres da variável:              len(frase) = > {len(frase)}')
    print(f'Conta a ocorrência de um carater dentro da variável:        frase.count("o") => {frase.count("o")} (método)')
    print(f'Conta a ocorrência com fatiamento do 0 ao 13:               frase.count("o", 0, 13) = > {frase.count("o", 0, 13)} (método)')
    print(f'Índice onde começa a sequência de caracteres:               frase.find("deo") => {frase.find("deo")} (método)')
    print(f'Retorna -1 quando não encontra a sequência de caracteres:   frase.find("Deo") => {frase.find("Deo")} (método)')
    print(f'Retorna True ou False:                                      "Curso" in frase => {"Curso" in frase} (operador)')

    cabecalho('Transformação da string', 120, '-')
    print(f'Troca de sequência de caracteres:                           frase.replace("Python", "Android") => {frase.replace("Python", "Android")}')
    print(f'Coloca em caixa alta:                                       frase.upper() => {frase.upper()} (método)')
    print(f'Coloca em caixa baixa:                                      frase.lower() => {frase.lower()} (método)')
    print(f'Coloca a primeira letra em maiúscula:                       frase.capitalize() => {frase.capitalize()} (método)')
    print(f'Coloca o primeiro caracter em maiúscula:                    frase.title() => {frase.title()} (método)')
    frase2 = '   Aprenda Python  '
    print(f'frase2 = {frase2}')
    print('         0123456789012345678  (índices)')
    print(f'Remove os espaços no início e fim:                          frase2.strip() => {frase2.strip()} (método)')
    print(f'Remove os espaços à direta:                                 frase2.rstrip() => {frase2.rstrip()} (método)')
    print(f'Remove os espaços à esquerda:                               frase2.lstrip() => {frase2.lstrip()} (método)')
    print(f'\n    Obs.: a variável é imutável                             frase = {frase}')
    print(f'                                                            frase2 = {frase2}')

    cabecalho('Divisão da string', 120, '-')
    print(f'Divide a string, à cada espaço, e coloca em uma "lista":   frase.split() => {frase.split()} (método)')
    print('                                                                    (índices) 01234    01    01234    012345')
    print('                                                         (índice das palavras)  0       1      2         3')
    print(f'Junta a frase separando por um caracter:                   "-".join(frase) => {"-".join(frase)}')
