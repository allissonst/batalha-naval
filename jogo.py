import random


def montar_tabuleiro(c, l):
    tab = [['.'] * (c) for i in range(l)]
    return tab


def alocando(quantnavios, tab):
    cont_frota = 0
    while cont_frota < quantnavios:
        lin = random.randint(0, 9)
        col = random.randint(0, 9)
        if col < 9 and col > 0 and lin < 9 and lin > 0:
            if tab[lin - 1][col - 1] != "N" and tab[lin - 1][col] != "N" and tab[lin - 1][col + 1] != "N" and tab[lin][
                col - 1] != "N" and tab[lin][col + 1] != "N" and tab[lin + 1][col - 1] != "N" and tab[lin + 1][
                col] != "N" and tab[lin + 1][col + 1] != "N" and tab[lin][col] != "N":
                tab[lin][col] = "N"
                cont_frota += 1
        elif col == 9 and lin == 0:
            if tab[lin][col - 1] != "N" and tab[lin + 1][col - 1] != "N" and tab[lin + 1][col] != "N" and tab[lin][
                col] != "N":
                tab[lin][col] = "N"
                cont_frota += 1
        elif col == 0 and lin == 0:
            if tab[lin][col + 1] != "N" and tab[lin + 1][col] != "N" and tab[lin + 1][col + 1] != "N" and tab[lin][
                col] != "N":
                tab[lin][col] = "N"
                cont_frota += 1
        elif col == 9 and lin == 9:
            if tab[lin - 1][col - 1] != "N" and tab[lin - 1][col] != "N" and tab[lin][col - 1] != "N" and tab[lin][
                col] != "N":
                tab[lin][col] = "N"
                cont_frota += 1
        elif col == 0 and lin == 9:
            if tab[lin][col + 1] != "N" and tab[lin - 1][col] != "N" and tab[lin - 1][col + 1] != "N" and tab[lin][
                col] != "N":
                tab[lin][col] = "N"
                cont_frota += 1
        elif col == 0 and tab[lin][col] != "N":
            if tab[lin - 1][col] != "N" and tab[lin - 1][col + 1] != "N" and tab[lin][col + 1] != "N" and tab[lin + 1][
                col] != "N" and tab[lin + 1][col + 1] != "N":
                tab[lin][col] = "N"
                cont_frota += 1
        elif lin == 0 and tab[lin][col] != "N":
            if tab[lin][col - 1] != "N" and tab[lin][col + 1] != "N" and tab[lin + 1][col - 1] != "N" and tab[lin + 1][
                col] != "N" and tab[lin + 1][col + 1] != "N":
                tab[lin][col] = "N"
                cont_frota += 1
    return tab


def mostrar_tabuleiro_completo(tab):
    print('\n  1   2   3   4   5   6   7   8   9   10')
    for l in range(lin):
        print(f'{linhas[l]}|', end='')
        for c in range(col):
            print(f'{tab[l][c]:4}', end='')
        print()


def mostrar_tabuleiro_parcial(tab):
    print('\n  1   2   3   4   5   6   7   8   9   10')
    for l in range(lin):
        print(f'{linhas[l]}|', end='')
        for c in range(col):
            if tab[l][c] == "F":
                print(f'{tab[l][c]:4}', end='')
            elif tab[l][c] == "A":
                print(f'{tab[l][c]:4}', end='')
            else:
                print('.   ', end='')
        print()


def jogar(jog, tab, jog2, tab2):
    print(f'\nTabuleiro do oponente ({jog2}): ')
    mostrar_tabuleiro_parcial(tab)
    print(f'\nMeu tabuleiro ({jog}):')
    mostrar_tabuleiro_parcial(tab2)
    jogcol = int(input(f'\n Agora é a vez do(a) jogador(a) {jog}. Escolha uma coluna (1-10).')) - 1
    joglin = input(f'Escolha uma linha (A-J).')
    joglin = ord(str(joglin.upper())) - 65

    if tab[joglin][jogcol] == "N":
        print(f'FOGO, você acertou um navio!!')
        tab[joglin][jogcol] = "F"
        print(f'Continue jogando a partir do tabuleiro do oponente')
        return "FOGO"
    elif tab[joglin][jogcol] == ".":
        tab[joglin][jogcol] = "A"
        print(f'ÁGUA. Não foi dessa vez :(')
    else:
        print(f'Você digitou uma coordenada que não corresponde ao jogo. Passou a vez.')


#############################################
#     PROGRAMA PRINCIPAL
#############################################

linhas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
col = 10
lin = 10
pontosjog1 = 0;
pontosjog2 = 0;
vez = 1

tab1 = montar_tabuleiro(col, lin)
tab2 = montar_tabuleiro(col, lin)

jogador1_nome = input("Digite o nome do jogador 1: ")
jogador2_nome = input("Digite o nome do jogador 2: ")

quantnavios = int(input("Digite a quantidade de navios. Deve ser no mínimo de 1 e no máximo de 10."))

tab1 = alocando(quantnavios, tab1)
tab2 = alocando(quantnavios, tab2)

print(f'\nO tabuleiro do jogador 1 - {jogador1_nome} - é: ')
mostrar_tabuleiro_completo(tab1)

print(f'\nO tabuleiro do jogador 2 - {jogador2_nome} - é: ')
mostrar_tabuleiro_completo(tab2)

print(f'\n VAMOS COMEÇAR! PREPARADOS?!!!!')

while pontosjog1 < quantnavios and pontosjog2 < quantnavios:
    if vez == 1:
        resultado = jogar(jogador1_nome, tab2, jogador2_nome, tab1)
        if resultado == "FOGO":
            pontosjog1 += 1
        else:
            vez = 2

    if vez == 2:
        resultado = jogar(jogador2_nome, tab1, jogador1_nome, tab2)
        if resultado == "FOGO":
            pontosjog2 += 1
        else:
            vez = 1

print()
if pontosjog1 > pontosjog2:
    print(f'Jogador(a) {jogador1_nome} venceu com {pontosjog1} pontos. Parabéns!')
    print(f'\nTabuleiro do oponente ({jogador2_nome}): ');
    mostrar_tabuleiro_parcial(tab2)
    print(f'\nMeu tabuleiro ({jogador1_nome}):');
    mostrar_tabuleiro_parcial(tab1)
else:
    print(f'Jogador(a) {jogador2_nome} venceu com {pontosjog2} pontos. Parabéns!')
    print(f'\nTabuleiro do oponente ({jogador1_nome}): ');
    mostrar_tabuleiro_parcial(tab1)
    print(f'\nMeu tabuleiro ({jogador2_nome}):');
    mostrar_tabuleiro_parcial(tab2)
