def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        quantia = n % (m + 1)
        if quantia > 0:
            return quantia
        return m

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada = int(input('Quantas peças irá tirar? '))
        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0
    return  jogada

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    vezDoPc = True
    if n % (m + 1) == 0:
        vezDoPc = False
        print('Você começa!')
    else:
        print('Computador começa!\n')
    while n > 0:
        if vezDoPc:
            jogada = computador_escolhe_jogada(n, m)
            vezDoPc = False
            if jogada == 1:
                print('O computador tirou uma peça.')
            else:
                print('O computador tirou {} peça(s)'.format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vezDoPc = True
            print('Você tirou {} peças'.format(jogada))
        n = n - jogada
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print('Agora restam {} peças no tabuleiro.\n'.format(n))
    if vezDoPc:
        print('Você ganhou!')
        return 1
    else:
        print('O computador ganhou')
        return 0

def campeonato():
    usuario = 0
    pc = 0
    x = 1
    for _ in range(3):
        print('\n**** Rodada {} ****\n'.format(x))
        x += 1
        vencedor = partida()
        if vencedor == 1:
            usuario += 1
        else:
            pc += 1
    print('Placar: Você {} X {} Computador'.format(usuario, pc))

modo = 0
while modo == 0:
    print('Bem-vindo ao jogo do NIM! Escolha:\n')
    modo = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
    print()
    if modo == 1:
        print('Você escolheu uma partida isolada')
        partida()
        break
    elif modo == 2:
        print('Você escolheu um campeonato!')
        campeonato()
        break
    else:
        print('Opção inválida!')
        modo = 0
