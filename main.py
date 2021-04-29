
TURN = 0

raster_dict = {"A1":" ", "A2":" ", "A3":" ",
               "B1":" ", "B2":" ", "B3":" ",
               "C1":" ", "C2":" ", "C3":" "
               }



def print_raster():
    print("   1   2   3\n"
      "-|---|---|---|\n" 
      "A|" + " " + raster_dict["A1"] + " " + "|" + " " + raster_dict["A2"] + " " +"|" + " " + raster_dict["A3"] + " \n"
      "-|---|---|---|\n"                                                                                                         
      "B|"+ " " + raster_dict["B1"] + " " + "|" + " " + raster_dict["B2"] + " " +"|" + " " + raster_dict["B3"] + " \n"
      "-|---|---|---|\n"                                                                                                      
      "C|"+ " " + raster_dict["C1"] + " " + "|" + " " + raster_dict["C2"] + " " +"|" + " " + raster_dict["C3"] + " ")


print_raster()


player_1 = input("Please enter your name player 1: ")
print(f"Thanks {player_1} you'll play with X")
player_2 = input("Please enter your name player 2: ")
print(f"Thanks {player_2} you'll play with O")


def game_end():
    winner = " "
    if raster_dict["A1"] == raster_dict["A2"] and raster_dict["A1"] != " ":
        if raster_dict["A1"] == raster_dict["A3"]:
            winner = raster_dict["A1"]
    elif raster_dict["B1"] == raster_dict["B2"] and raster_dict["B1"] != " ":
        if raster_dict["B1"] == raster_dict["B3"]:
            winner = raster_dict["B1"]
    elif raster_dict["C1"] == raster_dict["C2"] and raster_dict["C1"] != " ":
        if raster_dict["C1"] == raster_dict["C3"]:
            winner = raster_dict["C1"]
    elif raster_dict["A1"] == raster_dict["B1"] and raster_dict["A1"] != " ":
        if raster_dict["A1"] == raster_dict["C1"]:
            winner = raster_dict["A1"]
    elif raster_dict["A2"] == raster_dict["B2"] and raster_dict["A2"] != " ":
        if raster_dict["A2"] == raster_dict["C2"]:
            winner = raster_dict["A2"]
    elif raster_dict["A3"] == raster_dict["B3"] and raster_dict["A3"] != " ":
        if raster_dict["A3"] == raster_dict["C3"]:
            winner = raster_dict["A3"]
    elif raster_dict["A1"] == raster_dict["B2"] and raster_dict["A1"] != " ":
        if raster_dict["A1"] == raster_dict["C3"]:
            winner = raster_dict["A1"]
    elif raster_dict["A3"] == raster_dict["B2"] and raster_dict["A1"] != " ":
        if raster_dict["A3"] == raster_dict["C1"]:
            winner = raster_dict["A3"]
    return winner

def place_item():
    correct = True
    global TURN
    TURN += 1

    while correct:
        if TURN % 2 == 0:
            player = player_2
            sign = "O"
        else:
            player = player_1
            sign = "X"
        placing = input(f"{player}, please enter the placement coordinates like 'A1'\n")
        if placing in raster_dict:
            if raster_dict[placing] == " ":
                correct = False
                raster_dict[placing] = sign
                print_raster()
            else:
                print("Can't place it there.")
                correct = True
        else:
            print("Wrong coordinates")
            correct = True

game_on = True

while game_on:
    place_item()
    winner = game_end()
    if winner == "X":
        game_on = False
        print(f"{player_1} wins! Congratulations!")
    elif winner == "O":
        game_on = False
        print(f"{player_2} wins! Congratulations!")
    else:
        if TURN == 9:
            game_on = False
            print("It's a draw")
        else:
            game_on = True