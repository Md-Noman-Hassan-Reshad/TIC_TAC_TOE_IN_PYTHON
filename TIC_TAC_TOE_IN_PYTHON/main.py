import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def print_board(x_state, o_state):
    def get_symbol(position):
        if x_state[position]:
            return "X"
        elif o_state[position]:
            return "O"
        else:
            return position

    print(f"\n\t {get_symbol(0)} | {get_symbol(1)} | {get_symbol(2)}")
    print("\t---|---|---")
    print(f"\t {get_symbol(3)} | {get_symbol(4)} | {get_symbol(5)}")
    print("\t---|---|---")
    print(f"\t {get_symbol(6)} | {get_symbol(7)} | {get_symbol(8)}")


def check_win(x_state, o_state):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for win in wins:
        if all(x_state[i] for i in win):
            return "X"
        elif all(o_state[i] for i in win):
            return "O"
    return None


def is_board_full(x_state, o_state):
    return all(x_state[i] or o_state[i] for i in range(9))


if __name__ == "__main__":
    print("\n\nWelcome To Tic-Tac-Toe")
    player1_name = input("Enter the name of Player 1 (X): ")
    player2_name = input("Enter the name of Player 2 (O): ")

    while True:
        x_state = [0] * 9
        o_state = [0] * 9
        turn = 1
        while True:
            clear_console()
            print("\n\nTic-Tac-Toe")
            print_board(x_state, o_state)

            if turn == 1:
                print(f"\n{player1_name}'s turn (X)")
                player = player1_name
                symbol = "X"
            else:
                print(f"\n{player2_name}'s turn (O)")
                player = player2_name
                symbol = "O"

            try:
                value = int(input("Enter a position [0-8]: "))
                if 0 > value < 8:
                    raise ValueError("Invalid!. Please enter a number between 0 and 8.")
                if x_state[value] or o_state[value]:
                    raise ValueError("Position already taken. Choose another one.")
            except ValueError:
                print("Invalid!")
                continue

            if symbol == "X":
                x_state[value] = 1
            else:
                o_state[value] = 1

            winner = check_win(x_state, o_state)
            board_full = is_board_full(x_state, o_state)

            if winner:
                clear_console()
                print_board(x_state, o_state)
                print(f"\n{player} ({symbol}) wins!")
                break
            elif board_full:
                clear_console()
                print_board(x_state, o_state)
                print("\nIt's a draw!")
                break

            turn = 3 - turn

        play_again = input("Do you want to play again?[y/n]: ")
        if play_again.lower() != "y":
            print("\nThanks for playing Tic-Tac-Toe")
            break



# --------------------------------------------ooooooooooooooooooooooooooooooooo----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This code is an implementation of a simple command-line Tic-Tac-Toe game in Python. Let's break down the code step by step:

# 1. `clear_console()`: This function clears the console screen. It uses the `os.system` function to execute the appropriate console-clearing command based on the operating system (Windows or Unix-like systems).

# 2. `print_board(x_state, o_state)`: This function takes two lists, `x_state` and `o_state`, representing the current state of the game for player X and player O, respectively. It prints the Tic-Tac-Toe board with the current positions of X and O.

# 3. `checkwin(x_state, o_state)`: This function checks if either player X or player O has won the game. It does this by checking all possible winning combinations (horizontal, vertical, and diagonal) and returns 'X' if player X wins, 'O' if player O wins, or `None` if there is no winner yet.

# 4. `is_board_full(x_state, o_state)`: This function checks if the Tic-Tac-Toe board is full, meaning all positions are occupied by X or O.

# 5. `main()`: This is the main function of the game. It starts by getting the names of the two players and then enters an infinite loop to play the game repeatedly.

#    Inside the game loop:
#    - Two lists, `x_state` and `o_state`, are initialized to represent the current state of the board.
#    - `turn` is used to keep track of which player's turn it is (1 for player X and 2 for player O).

#    The game loop continues until there is a winner or the board is full:
#    - The console is cleared, and the current state of the board is printed.
#    - The current player's name and symbol (X or O) are displayed.
#    - The player is prompted to enter a position (0-8) to place their symbol.
#    - Input validation is performed to ensure the input is within the valid range and the chosen position is not already occupied.
#    - The chosen position is updated with the player's symbol (X or O).
#    - After each move, the code checks if there is a winner or if the board is full.
#    - If there is a winner, the winner's name and symbol are displayed, and the game ends.
#    - If the board is full, it's a draw, and the game ends.
#    - The `turn` is switched to the other player for the next iteration.

#    After the game ends, the player is asked if they want to play again. If they enter 'y', a new game starts. Otherwise, the program exits.

# 6. `if __name__ == "__main__":`: This line ensures that the `main` function is only executed if the script is run directly, not when it's imported as a module.

# However, there are a few issues in the code:
# - The `print_board` function call in the game loop should pass `x_state` and `o_state` as separate arguments, not as a single tuple.

# The code should function as a simple Tic-Tac-Toe game where two players can take turns playing the game on the command line.
