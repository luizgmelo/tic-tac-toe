matriz = [
          0,0,0,
          0,0,0,
          0,0,0
         ]

def printTicTacToe(): 
    count = 1
    for x in matriz:
        print(x, end='')
        if count % 3 == 0:
            print("")
        count+=1

print("="*30)
player_one = str(input("Qual você quer ser X/O: "))
if player_one in "xX":
    player_two = "O"
else:
    player_two = "X"

selected_play_one = []

while True:
    play = int(input("Onde você quer jogar (1-9): "))
    if play in selected_play_one:
        print(f"{play} já foi selecionado. Tente outra jogada")
        continue
    
    selected_play_one.append(play)
    matriz[play-1] = player_one 

    # Validar vitória
    if len(selected_play_one) >= 3:
        if matriz[0] == "X" and matriz[1] == "X" and matriz[2] == "X":
            print("Venceu")
            break

    print(selected_play_one)
    printTicTacToe()
    

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

