matrix = [
          [" "," "," "],
          [" "," "," "],
          [" "," "," "],
         ]

def printTicTacToe(): 
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == 0:
                print(matrix[i][j], end="")
                continue
            print("|" + matrix[i][j], end="")
        if i == len(matrix) - 1:
            print("\n")
            continue
        print("\n-----")
    
selected_plays = []

def playNow(player):
    m = int(input(f"{player}: Em qual linha você quer jogar (1-3)"))
    n = int(input(f"{player}: Em qual coluna você quer jogar (1-3): ")) 
    print("")
    if [m, n] in selected_plays:
        print(f"linha {m} e coluna {n} já foi selecionado. Tente outra jogada")
        playNow(player) 

    selected_plays.append([m, n])
    matrix[m-1][n-1] = player 
    
    printTicTacToe()

def checkMainDiagonally(matrix, player):
    m = 3
    for i in range(0, m):
        if matrix[i][i] != player:
            return False
    return True

def validateVictory(player): 
    if len(selected_plays) >= 3:
        if matriz[0] == player and matriz[1] == player and matriz[2] == player:
            print(f"Venceu {player}")
            return True
        elif matriz[3] == player and matriz[4] == player and matriz[5] == player:
            print(f"Venceu {player}")
            return True
        elif matriz[6] == player and matriz[7] == player and matriz[8] == player:
            print(f"Venceu {player}")
            return True
        elif matriz[0] == player and matriz[4] == player and matriz[8] == player:
            print(f"Venceu {player}")
            return True
        elif matriz[2] == player and matriz[4] == player and matriz[6] == player:
            print(f"Venceu {player}")
            return True
        elif matriz[0] == player and matriz[3] == player and matriz[6] == player:
            print(f"Venceu {player}")
            return True
        elif matriz[1] == player and matriz[4] == player and matriz[7] == player:
            print(f"Venceu {player}")
            return True
        elif matriz[2] == player and matriz[5] == player and matriz[8] == player:
            print(f"Venceu {player}")
            return True
        elif len(selected_plays) == 9:
            print("Empate")
            return True
        return False
while True:
    print("="*30)
    player_one = str(input("Qual você quer ser X/O: ")).upper()
    if player_one in "xX" and player_one != "":
        player_one = "X"
        player_two = "O"
        break
    elif player_one in "oO0" and player_one != "":
        player_one = "O"
        player_two = "X"
        break
    else:
        print("Valor Inválido, Digite X ou O!")

counter = 1
while True: 
    printTicTacToe()
    if counter % 2 != 0:
        playNow(player_one)
        won = validateVictory(player_one)
    else:
        playNow(player_two)
        won = validateVictory(player_two)
    

    if won == True:
        break
    
    counter += 1
  
    

# como ganhar
# linhas
# 1 2 3
# 4 5 6
# 7 8 9
# colunas
# 1 4 7
# 2 5 8
# 3 6 9

# 1 5 9
# 3 5 7

