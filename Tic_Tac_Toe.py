from time import sleep
from sys import exit
# Create class for the board
class Board:
    cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    winning_combinations = [
    [0, 1, 2],  # rows
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],  # columns
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],  # diagonals
    [2, 4, 6]
]
    def __init__(self):
        self.__visual = f"| {Board.cells[0]} | {Board.cells[1]} | {Board.cells[2]} |\n \
=============\n \
| {Board.cells[3]} | {Board.cells[4]} | {Board.cells[5]} |\n \
=============\n \
| {Board.cells[6]} | {Board.cells[7]} | {Board.cells[8]} |"

    def get_board(self):
        return self.__visual
    
    def set_board_Player_1(self, cell_player_1):
        Board.cells[cell_player_1-1] = "X"

    def set_board_Player_2(self, cell_player_2):
        Board.cells[cell_player_2-1] = "O"

    def win_or_draw(self):
        game_over = None
        if any(all(Board.cells[i] == "X" for i in combo) for combo in Board.winning_combinations):
            game_over = "Player 1"
            return game_over

        elif any(all(Board.cells[i] == "O" for i in combo) for combo in Board.winning_combinations):
            game_over = "Player 2"
            return game_over
        
        elif not set(["1", "2", "3","4", "5","6","7","8","9"]) & set(Board.cells):
            game_over = "Draw"
            return game_over
        else: 
            return game_over
# Create class for each of the two players
class Player_1:
    def __init__(self, user_name, X_or_O = "X"):
        self.__name = user_name
        self.X_or_O = X_or_O

    def get_name(self):
        return self.__name
    
    def get_X(self):
        return self.X_or_O

# Create class for each of the two players    
class Player_2:
    def __init__(self, user_name, X_or_O = "O"):
        self.__name = user_name
        self.__X_or_O = X_or_O

    def get_name(self):
        return self.__name
    
    def get_X(self):
        return self.__X_or_O

######################################################
# Program Logic
while True:
    print("-"*30)
    print("Welcome to Tic Tac Toe")
    print("-"*30)
    sleep(2)

    # Player 1
    player_1_name = input("Player 1, Choose your name. ").title().strip()
    print("-"*30)
    player_1 = Player_1(player_1_name)
    print(f"Hello {player_1.get_name()} You will play with {player_1.get_X()}")
    print("-"*30)
    sleep(2)

    # Player 2
    player_2_name = input("Player 2, Choose your name. ").title().strip()
    print("-"*30)
    player_2 = Player_2(player_2_name)
    print(f"Hello {player_2.get_name()} You will play with {player_2.get_X()}")
    print("-"*30)
    sleep(2)
    
    # Show Board while it's not full
    board = Board()
    print(board.get_board())

    # Turns
    while True:
    # Player 1 turn
        while True:
            try:
                print("-"*30)
                player_1_choice = int(input(f"{player_1.get_name()}, Choose cell no from the empty ones ").strip())
                print("-"*30)
                if player_1_choice >= len(Board.cells):
                    player_1_choice = 9
                    if Board.cells[player_1_choice-1] in ["X", "O"]:
                        print("Can't play here")
                        print("-"*30)
                        print(board.get_board())
                    else:
                        board.set_board_Player_1(player_1_choice)
                        board = Board()
                        print(board.get_board())
                elif 0 > player_1_choice:
                    player_1_choice = 1
                    if Board.cells[player_1_choice-1] in ["X", "O"]:
                        print("Can't play here")
                        print("-"*30)
                        print(board.get_board())
                    else:
                        board.set_board_Player_1(player_1_choice)
                        board = Board()
                        print(board.get_board())
                elif Board.cells[player_1_choice-1] in ["X", "O"]:
                    print("Can't play here")
                    print("-"*30)
                    print(board.get_board())
                else:
                    board.set_board_Player_1(player_1_choice)
                    board = Board()
                    print(board.get_board())

                board.win_or_draw()
                break
            except ValueError:
                print("-"*30)
                print("Choose from 1-9")
                print("-"*30)
                board = Board()
                print(board.get_board())

        if board.win_or_draw() == "Player 1":
            print("-"*30)
            print(f"{player_1.get_name()} wins !!!")
            break
        elif board.win_or_draw() == "Player 2":
            print("-"*30)
            print(f"{player_2.get_name()} wins !!!")
            break
        elif board.win_or_draw() == "Draw":
            print("-"*30)
            print(f"That was a fine draw")
            break
        else:
            pass

        # Player 2 turn
        while True:
            try:
                print("-"*30)
                player_2_choice = int(input(f"{player_2.get_name()}, Choose cell no from the empty ones ").strip())
                print("-"*30)
                if player_2_choice >= len(Board.cells):
                    player_2_choice = 9
                    if Board.cells[player_2_choice-1] in ["X", "O"]:
                        print("Can't play here")
                        print("-"*30)
                        print(board.get_board())
                    else:
                        board.set_board_Player_2(player_2_choice)
                        board = Board()
                        print(board.get_board())
                elif 0 > player_2_choice:
                    player_2_choice = 1
                    if Board.cells[player_2_choice-1] in ["X", "O"]:
                        print("Can't play here")
                        print("-"*30)
                        print(board.get_board())
                    else:
                        board.set_board_Player_2(player_2_choice)
                        board = Board()
                        print(board.get_board())
                elif Board.cells[player_2_choice-1] in ["X", "O"]:
                    print("Can't play here")
                    print("-"*30)
                    print(board.get_board())
                else:
                    board.set_board_Player_2(player_2_choice)
                    board = Board()
                    print(board.get_board())

                board.win_or_draw()
                break
            except ValueError:
                print("-"*30)
                print("Choose from 1-9")
                print("-"*30)
                board = Board()
                print(board.get_board())

        if board.win_or_draw() == "Player 1":
            print("-"*30)
            print(f"{player_1.get_name()} wins !!!")
            break
        elif board.win_or_draw() == "Player 2":
            print("-"*30)
            print(f"{player_2.get_name()} wins !!!")
            break
        elif board.win_or_draw() == "Draw":
            print("-"*30)
            print(f"That was a fine draw")
            break
        else:
            pass

    # Play again
    while True:
        print("-"*30)
        choice = input("Do you want to play again?[y/n] ").lower().strip()
        if choice in ['y', 'yes']:
            Board.cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            break
        elif choice in ['n', 'no']:
            print("-"*30)
            print("Hope you had fun playing together 😊")
            exit()
        else:
            print("-"*30)
            print("Try using yes or no")