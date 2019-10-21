from funcoes import ansi

for li in range(0, 11):
    print(f'{ansi("negative", "bold")}{li:3} {ansi()}', end='')
    for co in range(1, 11):
        if li == 0 and co < 10:
            print(f'{ansi("negative", "bold")}{co:3} {ansi()}', end='')
        elif li == 0 and co == 10:
            print(f'{ansi("negative", "bold")}{co:3} {ansi()}')
        else:
            if co == 10 and li != 10:
                print(f'{co * li:3} ')
            else:
                if li == co:
                    print(f'{ansi("negative", "bold", "vermelho")}{co * li:3} {ansi()}', end='')
                else:
                    print(f'{co * li:3} ', end='')
