import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(x_state, o_state):
    def get_symbol(position):
        if x_state[position]:
            return 'X'
        elif o_state[position]:
            return 'O'
        else:
            return position
        
    print(f"\n\t {get_symbol(0)} | {get_symbol(1)} | {get_symbol(2)}")
    print("\t---|---|---")
    print(f"\t {get_symbol(3)} | {get_symbol(4)} | {get_symbol(5)}")
    print("\t---|---|---")
    print(f"\t {get_symbol(6)} | {get_symbol(7)} | {get_symbol(8)}")

def checkwin(x_state, o_state):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if all(x_state[i] for i in win):
            return 'X'
        elif all(o_state[i] for i in win):
            return 'O'
    return None

def is_board_full(x_state, o_state):
    return all(x_state[i] or o_state[i] for i in range (9))

def main():
    print("\n\nWelcome To Tic-Tac-Toe")
    player1_name = input("Enter the name of Player 1 (X): ")
    player2_name = input("Enter the name of Player 2 (O): ")

    while True:
        x_state = [0] * 9
        o_state = [0] * 9
        turn = 1

        while True:
            clear_console()
            print("\n\nTic-Tac-Toe\n")
            print_board(x_state, o_state)

            if turn == 1:
                print(f"\n{player1_name}'s turn (X)")
                player = player1_name
                symbol = 'X'
            else:
                print(f"\n{player2_name}'s turn (O)")
                player = player2_name
                symbol = 'O'

            try:
                value = int(input("Enter a position (0-8): "))
                if value < 0 or value > 8:
                    raise ValueError("Invalid input. Please enter a number between 0 and 8.")
                if x_state[value] or o_state[value]:
                    raise ValueError("Position already taken. Choose another one.")
            except ValueError as e:
                print(e)
                continue

            if symbol == 'X':
                x_state[value] = 1
            else:
                o_state[value] = 1

            winner = checkwin(x_state, o_state)
            board_full = is_board_full(x_state, o_state)
            if winner:
                clear_console()
                print_board(f"\n{x_state, o_state}")
                print(f"\n{player} ({symbol}) wins!")
                break
            elif board_full:
                clear_console()
                print_board(f"\n{x_state, o_state}")
                print("\nIt's a draw!")
                break

            turn = 3 - turn

        play_again = input("\nDo you want to play again? (yes/no)[y/n]: ")
        if play_again.lower() != 'yes' or play_again.lower() != 'y':
            print("\nThanks for Playing Tic-Tac-Toe")
            break

if __name__ == "__main__":
    main()
