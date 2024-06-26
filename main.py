matriz = [
          " "," "," ",
          " "," "," ",
          " "," "," "
         ]

def printTicTacToe(): 
    count = 1
    for x in matriz:
        print(x, end=' ')
        if count == 9:
            print("\n")
        elif count % 3 == 0:
            print("\n----------")
        else:
            print("|", end=' ')
        count+=1
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
    
selected_plays = []

def playNow(player):
    position = int(input(f"{player}: Onde você quer jogar (1-9): ")) 
    print("")
    if position in selected_plays:
        print(f"{position} já foi selecionado. Tente outra jogada")
        playNow(player) 

    selected_plays.append(position)
    matriz[position-1] = player 
    
    printTicTacToe()


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

counter = 1
while True: 
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

