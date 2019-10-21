def verificador(m, n=int):
    """-> verifica se a entrada do usuário é um número inteiro ou real,
    caso não seja nenhuma das opções retorna uma mensagem de erro.

    :param m: mensagem da entrada
    :param n:(opcional) tipos possíveis => int; float
    :return: entrada do usuário
    """
    from funcoes import ansi

    entrada = 0
    while True:
        try:
            if n == int:
                entrada = int(input(m))
            elif n == float:
                entrada = float(input(m))
        except ValueError:
            print(f'{ansi("vermelho")}'
                  f'Digite um número {"inteiro" if n == int else "real"}. Tente novamente!{ansi()}')
            continue
        else:
            return entrada
