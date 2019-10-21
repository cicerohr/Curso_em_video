"""14_ex058_jogo_adivinhacao_2.py em 2018-12-16. Projeto Curso em Video.

Jogo da Adivinhação v2.0

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.

"""
from random import randint
from funcoes import cabecalho, verificador, ansi

if __name__ == '__main__':
    cabecalho('Jogo da Adivinhação v2.0')

    print('''\tfrom random import randint
    from cicero import cabecalho, verificador, ansi
    
    computador = randint(0, 10)
    print('Sou seu computador.\\nAcabei de pensar em número entre 0 a 10.\\nSerá que você consegue adivinhar qual foi?')
    palpites = 0
    while True:
        jogador = verificador('Qual é seu palpite? ')
        if 0 <= jogador <= 10:
            palpites += 1
            if jogador < computador:
                print('Mais... Tente novamente!')
            elif jogador > computador:
                print('Menos... Tente novamente!')
            else:
                print(f'\\nAcertou com {palpites} tentativa(s). Parabéns!')
                break
        else:
            print(f'\\n{ansi("vermelho")}Digite um número inteiro entre 0 e 10. Tente novamente!{ansi()}\\n')
    ''')
    computador = randint(0, 10)
    print('Sou seu computador...\nAcabei de pensar em número entre 0 a 10.\nSerá que você consegue adivinhar qual foi?')
    palpites = 0
    while True:
        jogador = verificador('Qual é seu palpite? ')
        if 0 <= jogador <= 10:
            palpites += 1
            if jogador < computador:
                print('Mais... Tente novamente!')
            elif jogador > computador:
                print('Menos... Tente novamente!')
            else:
                print(f'\nAcertou com {palpites} tentativa{"s" if palpites > 1 else ""}. Parabéns!')
                break
        else:
            print(f'\n{ansi("vermelho")}Digite um número inteiro entre 0 e 10. Tente novamente!{ansi()}\n')
