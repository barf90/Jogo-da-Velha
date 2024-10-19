import time

# Metodo com uma lista de string como argumento para mostrar tabuleiro
def tabuleiro (elemento: list) -> None:
    
    print()
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")

    print("JOGO DA VELHA")
    print("pressione ENTER para startar...")

    input()

    print("Carregando.....")

    time.sleep(1)

def nomear_player(simbolo: str, numero: int) -> str:
    # Checa se o nome do jogador é válido
    while True:
        print(f"\nJogador {numero}({simbolo}), digite seu nome:")
        nome_jogador = input().title()

        if nome_jogador != "":
            return nome_jogador
    
        print("Nome Inválido, digite novamente:")

jogador1 = nomear_player("Círculo", 1)
jogador2 = nomear_player("X", 2)

tabuleiro([numbers for numbers in range(1,10)])

print("\nPara ganhar, é preciso 3 símbolos consecutivos")

time.sleep(3)

print(f"{jogador1} VS {jogador2}")


# Método que checa se há vitória a partir de uma lista
def checar_vitoria(elemento: list) -> bool:
    # Verifica linhas, colunas e diagonais para vitória
    vitorias = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Linhas
                (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colunas
                (0, 4, 8), (2, 4, 6)]           # Diagonais
    
    for a, b, c in vitorias:
        if elemento[a] == elemento[b] == elemento[c] and elemento[a] != " ":
            return True
        
    return False

# Se existe um elemento em branco no tabuleiro, há um empate
def checar_empate(elemento: list) -> bool:
    return " " not in elemento

def rodada(elemento: list, num_jogador: int, jogador: str) -> None:
    simbolo = "O" if num_jogador == 1 else "X"

    while True:
        tabuleiro(elemento)
        jogada = input(f"{jogador} ({simbolo}), escolha uma posição (1-9): ")

        if jogada.isdigit() and int(jogada) in range(1, 10):
            jogada = int(jogada) - 1

            if elemento[jogada] == " ":
                elemento[jogada] = simbolo
                break

            else:
                print("Casa ocupada, escolha outra.")

        else:
            print("Jogada inválida, escolha outra posição.")

elemento_do_jogo = [" "] * 9

# Contador para saber qual é o jogador da vez
for num_rodada_atual in range(1, 10):
    num_jogador_atual = 1 if num_rodada_atual % 2 != 0 else 2
    jogador_atual = jogador1 if num_jogador_atual == 1 else jogador2

    rodada(elemento_do_jogo, num_jogador_atual, jogador_atual)

    if checar_vitoria(elemento_do_jogo):
        tabuleiro(elemento_do_jogo)
        print(f"{jogador_atual} Venceu! Parabéns, você venceu na {num_rodada_atual}ª rodada!")
        break

    if checar_empate(elemento_do_jogo):
        tabuleiro(elemento_do_jogo)
        print("Empate!")
        break

    time.sleep(0.5)

else:
    tabuleiro(elemento_do_jogo)
    print("Empate!")