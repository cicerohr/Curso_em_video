"""23______tratamento_erros.py em 2019-07-13. Projeto Curso em Video.

Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
Aprenda como usar a estrutura try except no Python de uma forma simples.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Tratamento de erros')

    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
    except Exception as erro:
        print(f'Problema encontrado foi {erro.__class__}')  # mostra o tipo de erro
    else:
        print(f'O resultado é {r}')
    finally:
        print('Volte sempre!')

    try:
        print('=' * 20)
        c = int(input('Numerador: '))
        d = int(input('Denominador: '))
        r2 = c / d
    except (ValueError, TypeError):
        print('Problema com tipo de dado que você digitou.')
    except ZeroDivisionError:
        print('Não é possível dividir um número por zero.')
    except KeyboardInterrupt:
        print('O usuário preferiu nã0 informar os dados.')
    except Exception as erro:
        print(f'Problema encontrado foi {erro.__cause__}')  # mostra a causa de erro
    else:
        print(f'O resultado é {r2}')
    finally:
        print('Volte sempre!')
