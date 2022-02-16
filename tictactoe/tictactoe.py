import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("Player 1 is X and Player 2 is 0")
        print("Take turns placing your pieces - the first to 3 in a row win!")
    def print_board(self):
        # TODO: Print the board
        for i in range(len(self.board)):
            print()
            for o in range(len(self.board[0])):
                print(self.board[i][o], end=' ')
        print()
    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if row >= 0 and row <= 2:
            if col >= 0 and col <= 2:
                if self.board[row][col] == "-":
                    return True
    def take_random_turn(self, player):
        randRow = random.randint(0, len(self.board)-1)
        randCol = random.randint(0, len(self.board)-1)
        while not self.is_valid_move(randRow, randCol):
            randRow = random.randint(0, len(self.board) - 1)
            randCol = random.randint(0, len(self.board) - 1)
        self.place_player(player, randRow, randCol)
    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        row = int(input("Enter a row: "))
        col = int(input("Enter a column: "))
        while self.is_valid_move(row, col) != True:
            print("Please enter a valid move.")
            row = input("Enter a row: ")
            col = input("Enter a column: ")
        self.place_player(player, row, col)

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + "'s Turn")
        if player == "X":
            self.take_manual_turn(player)
        else:
            self.take_random_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win
        win = False
        for i in range(len(self.board[0])):
            for o in range(len(self.board)):
                if(self.board[o][i] == player):
                    win = True
                else:
                    win = False
                    break
            if win == True:
                return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        win = False
        for i in range(len(self.board)):
            for o in range(len(self.board[0])):
                if (self.board[i][o] == player):
                    win = True
                else:
                    win = False
                    break
            if win == True:
                return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        win = False
        for i in range(len(self.board)):
            if (self.board[i][i] == player):
                win = True
            else:
                win = False
                break
        if win == True:
            return True
        for p in range(len(self.board)):
            if self.board[p][len(self.board[0]) - 1 - p] == player:
                win = True
            else:
                win = False
                break
        return win

    def check_win(self, player):
        # TODO: Check win
        win = False
        if self.check_col_win(player):
            return True
        if self.check_row_win(player):
            return True
        if self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        for i in range(len(self.board)):
            for o in range(len(self.board[0])):
                if self.board[i][o] == "-":
                    return False

        if self.check_win("X") and self.check_win("O"):
            return True

    def play_game(self):
        player1 = "X"
        player2 = "O"
        winner = None

        moves = 0
        win = False
        tie = False
        while(win != True and tie != True):
            if(moves % 2 == 0):
                self.take_turn(player1)
                self.print_board()
                win = self.check_win(player1)
                if win:
                    winner = player1
            if(moves % 2 == 1):
                self.take_turn(player2)
                self.print_board()
                win = self.check_win(player2)
                if win:
                    winner = player2
            moves+=1
            tie = self.check_tie()

        if win == True:
            print(winner + "wins!")
        else:
            print("It's a tie!")

