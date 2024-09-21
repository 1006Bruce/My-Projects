# Tic-tac-toe
#### Video Demo:  <URL https://youtu.be/5dreEOTPdTs>
#### Description:
This project is a command-line implementation of the classic Tic-Tac-Toe game, designed for two players. Player 1 uses "X" and Player 2 uses "O". The game is played on a 3x3 grid, and the objective is for a player to align three of their symbols in a row, column, or diagonal. This project serves as an educational tool to practice concepts of user input handling, loops, and basic game logic in Python.

The game is interactive and prompts each player to enter their desired position on the grid. It checks for win conditions after each move and displays the current state of the board. The game also handles invalid inputs and occupied positions gracefully, ensuring a smooth user experience.

Highlights of the project:

1.User-Friendly Interface:
The game's title and instructions are centered in the terminal, enhancing readability. This small but impactful detail improves the user experience by making the interface clear and organized.

2.Input Validation and Error Handling:
The game employs input validation to check whether the entered positions are within the accepted range (0-8) and whether the positions are already taken. This helps prevent crashes due to invalid inputs and keeps the game running smoothly for the users.

3.Win Condition Verification:
The notwin() function rigorously checks possible winning conditions after each move. It scans all rows, columns, and diagonals to determine if a player has won. This function ensures the game can promptly declare the winner and end the game loop correctly.

4.End Game Conditions:
Apart from detecting winners, the game also checks for a "tie" condition. This occurs when the board is full, and no player manages to align three symbols in a row. This feature is particularly important to ensure the game handles all possible outcomes.

5.Grid Display:
The printboard() function dynamically aligns the grid display to the console's width, making use of shutil.get_terminal_size(). This keeps the grid well-formatted and visually appealing on different terminal sizes.

Now I am gong to show the function details of my code:

1. main()
This is the main function of my code, it will ensure to realize the function of Tic-tac-toe game. First, it will print the title of the game and the rules of the game, also it will print the board of the game with numbers on it. I put the words and the board in the middle of the terminal, because it will be more easier for users to play. Then their is a while loop, which will ensure the two players can choose the position they decided. The players can key in the number of the cell to put X or O on it If they key in other information besides the number from 0 to 9, terminal will warn them to key in the right number. Also, if they key in the cell that is already placed, there will be a warning for them to choose another place. After they choose the number of the position, the cell will change to X or O. Finally I call a judge function to see if the situation meets the win conditions, if it does, it will print the winner in the terminal. If not, it will continue the loop.

2.notwin(cell_list)
This function is to check if some player has won the game. Basically it checks the rows, lines and diagnols of the board, to make sure there are no three X or O aligns together. If it does find such a situation, it will break the function and print who wins, also it will return false back to the main function to finish the game. In the last part, the function will check if the cells are filled full of X and O, the way to check is to count how many X in the cells, because Player1 is the first to move. If there are no winners and cells are full, it will print tie and end the game either.

3.printboard(cell_list)
This function is for printing game board. First, it will print the title of the game, I change the position of the title to middle of the terminal. Then print the cells row one by one, after printing one row, it will print a divide line to make the board more beautiful. I aslo change the cells and the divide lines position to the middle of the terminal.
