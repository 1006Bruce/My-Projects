from cs50 import get_string
import shutil


def main():
    cell_list = list(range(9))
    printboard(cell_list)

    terminal_size = shutil.get_terminal_size()
    console_width = terminal_size.columns
    rules1 = "This is a Tic-tac-toe game, there are two players, Player1 for X, Player2 for O."
    rules2 = "If three X aligns in a line, Player1 wins. Instead, Player2 wins."
    print(rules1.center(console_width))
    print(rules2.center(console_width))

    while True:

        position1 = get_string("Player1 position: ")
        if not position1.isdigit() or int(position1) not in range(9):
            print("Please key in the right number.")
            continue
        if cell_list[int(position1)] in ["X", "O"]:
            print("Please choose another position.")
            continue

        cell_list[int(position1)] = "X"
        printboard(cell_list)
        if not notwin(cell_list):
            break


        position2 = get_string("Player2 position: ")
        if not position2.isdigit() or int(position2) not in range(9):
            print("Please key in the right number.")
            continue
        if cell_list[int(position2)] in ["X", "O"]:
            print("Please choose another position.")
            continue

        cell_list[int(position2)] = "O"
        printboard(cell_list)
        if not notwin(cell_list):
            break


def notwin(cell_list):

    for i in range(3):
        if cell_list[i * 3] == cell_list[i * 3 + 1] == cell_list[i * 3 + 2] ==  "X":
            print("Player1 win!")
            return False
        elif cell_list[i] == cell_list[i + 3] == cell_list[i +6] ==  "X":
            print("Player1 win!")
            return False
        elif cell_list[i * 3] == cell_list[i * 3 + 1] == cell_list[i * 3 + 2] ==  "O":
            print("Player2 win!")
            return False
        elif cell_list[i] == cell_list[i + 3] == cell_list[i +6] ==  "O":
            print("Player2 win!")
            return False

    if cell_list[0] == cell_list[4] == cell_list[8]:
        if cell_list[0] == "X":
            print("Player1 win!")
            return False
        else:
            print("Player2 win!")
            return False
    elif cell_list[2] == cell_list[4] == cell_list[6]:
        if cell_list[2] == "X":
            print("Player1 win!")
            return False
        else:
            print("Player2 win!")
            return False
    else:
        num_x = 0
        num_o = 0
        for i in range(9):
            if cell_list[i] == "X":
                num_x += 1
            elif cell_list[i] == "O":
                num_o += 1

        if num_x + num_o == 9:
            print("Tie!")
            return False
        else:
            return True

def printboard(cell_list):

    terminal_size = shutil.get_terminal_size()
    console_width = terminal_size.columns

    #print title
    title = "Tic-tac-toe"
    print(title.center(console_width))

    for j in range(3):

        #print cells
        output = " "

        for i in range(j * 3, (j + 1) * 3):
            output += " " + str(cell_list[i])
        output_len = len(output)
        space_output = (console_width - output_len) // 2

        print(" " * (space_output - 1) + output)

        #print divide line
        divide = "+ " + "- " * 3 + "+"
        divide_len = len(divide)
        space_divide = (console_width - divide_len) // 2

        print (" " * space_divide + divide)

main()
