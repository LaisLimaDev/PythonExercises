def computador_escolhe_jogada(n, m):
    # Computador tenta deixar múltiplo de (m+1) para o usuário
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    # Se não for possível, retira o máximo de peças possíveis
    return min(n, m)

def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        print(f"Oops! Jogada inválida! Tente de novo. (Você pode tirar entre 1 e {min(n, m)} peças.)")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_computador = False
    else:
        print("Computador começa!")
        vez_do_computador = True

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print(f"O computador tirou {jogada} peça(s).")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            print(f"Você tirou {jogada} peça(s).")
        
        print(f"Agora restam {n} peça(s) no tabuleiro.\n")
        vez_do_computador = not vez_do_computador

    if vez_do_computador:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for _ in range(3):
        print("\n**** Rodada ****\n")
        partida()
      #  if vez_do_computador:
            placar_usuario += 1
        else:
            placar_computador += 1

    print("\n**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

opcao = int(input())

if opcao == 1:
    print("\nVocê escolheu uma partida isolada!")
    partida()
elif opcao == 2:
    print("\nVocê escolheu um campeonato!")
    campeonato()
else:
    print("Opção inválida!")
