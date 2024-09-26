# 14
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "X"

def exibir_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
    print()

def verificar_vitoria():
    for linha in tabuleiro:
        if linha.count(jogador_atual) == 3:
            return True
    for coluna in range(3):
        if [tabuleiro[linha][coluna] for linha in range(3)].count(jogador_atual) == 3:
            return True
    if [tabuleiro[i][i] for i in range(3)].count(jogador_atual) == 3 or [tabuleiro[i][2-i] for i in range(3)].count(jogador_atual) == 3:
        return True
    return False

for _ in range(9):
    exibir_tabuleiro()
    linha, coluna = map(int, input(f"Jogador {jogador_atual}, escolha a linha e a coluna (0-2): ").split())
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador_atual
        if verificar_vitoria():
            exibir_tabuleiro()
            print(f"Jogador {jogador_atual} venceu!")
            break
        jogador_atual = "O" if jogador_atual == "X" else "X"
    else:
        print("Posição ocupada, tente novamente.")
else:
    exibir_tabuleiro()
    print("Empate!")
