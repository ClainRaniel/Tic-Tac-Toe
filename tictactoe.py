cells = '         '
cell_list = list(cells)


def fields():
    print("---------")
    print("|", cell_list[0], cell_list[1], cell_list[2], "|")
    print("|", cell_list[3], cell_list[4], cell_list[5], "|")
    print("|", cell_list[6], cell_list[7], cell_list[8], "|")
    print("---------")


fields()


def game():
    turn = 'X'
    counter = 0

    while True:
        x_coordinates = input("Enter coordinates: ").split()

        if x_coordinates[0].isalpha() or x_coordinates[1].isalpha():
            print("You should enter numbers!")
            continue

        # to convert 1-based (Bottom-left) to 0-based (Top-left)
        cell_list_col, cell_list_row = x_coordinates
        cell_list_x = int(cell_list_col) - 1
        cell_list_y = 3 - int(cell_list_row)
        move = (cell_list_y * 3) + cell_list_x

        if int(cell_list_col) > 3 or int(cell_list_row) > 3 or int(cell_list_col) <= 0 or int(cell_list_row) <= 0:
            print("Coordinates should be from 1 to 3!")
            continue

        if cell_list[move] == ' ':
            cell_list[move] = turn
            counter += 1
            fields()
        else:
            print("This cell is occupied! Choose another one!")

        # This will check if there's a winner after 5th moves.
        if counter >= 5:
            if cell_list[0] == cell_list[1] == cell_list[2] != ' ':
                print(turn + " wins")
                break
            elif cell_list[3] == cell_list[4] == cell_list[5] != ' ':
                print(turn + " wins")
                break
            elif cell_list[6] == cell_list[7] == cell_list[8] != ' ':
                print(turn + " wins")
                break
            elif cell_list[6] == cell_list[3] == cell_list[0] != ' ':
                print(turn + " wins")
                break
            elif cell_list[7] == cell_list[4] == cell_list[1] != ' ':
                print(turn + " wins")
                break
            elif cell_list[8] == cell_list[5] == cell_list[2] != ' ':
                print(turn + " wins")
                break
            elif cell_list[0] == cell_list[4] == cell_list[8] != ' ':
                print(turn + " wins")
                break
            elif cell_list[8] == cell_list[4] == cell_list[0] != '_':
                print(turn + " wins")
                break

        if counter == 9:
            print("Draw!!")
            break
        # changes the player every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


game()
