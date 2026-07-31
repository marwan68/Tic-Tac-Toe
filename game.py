from player import Player
from board import Board
from menu import Menu
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

        self.board = Board()
        self.menu = Menu()

        # 0 -> Player 1
        # 1 -> Player 2
        self.current_player = 0

    def start(self):
        choice = self.menu.display_main_menu()

        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        print("Setting up Player 1:")
        self.player1.choose_name()
        self.player1.choose_symbol()

        print("\nSetting up Player 2:")
        self.player2.choose_name()

        while True:
            self.player2.choose_symbol()

            if self.player2.symbol != self.player1.symbol:
                break

            print(f"Symbol already taken by {self.player1.name}. Please choose another symbol.")

        clear_screen()

    def play_game(self):
        while True:

            self.play_turn()

            if self.check_winner():

                clear_screen()
                self.board.display_board()

                if self.current_player == 0:
                    print(f"\n{self.player1.name} wins!")
                else:
                    print(f"\n{self.player2.name} wins!")

                choice = self.menu.display_end_game_menu()

                if choice == "1":
                    self.restart_game()
                    continue
                else:
                    self.quit_game()

            elif self.check_draw():

                clear_screen()
                self.board.display_board()

                print("\nIt's a draw!")

                choice = self.menu.display_end_game_menu()

                if choice == "1":
                    self.restart_game()
                    continue
                else:
                    self.quit_game()

            self.switch_player()

    def play_turn(self):

        clear_screen()

        if self.current_player == 0:
            player = self.player1
        else:
            player = self.player2

        self.board.display_board()

        print(f"\n{player.name}'s turn ({player.symbol})")

        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))

                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break

                print("Invalid move! Try again.")

            except ValueError:
                print("Please enter a number between 1 and 9.")

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_winner(self):

        win_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],

            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],

            [0, 4, 8],
            [2, 4, 6]
        ]

        for combo in win_combinations:

            if (
                self.board.board[combo[0]] ==
                self.board.board[combo[1]] ==
                self.board.board[combo[2]]
                and
                not self.board.board[combo[0]].isdigit()
            ):
                return True

        return False

    def check_draw(self):

        for cell in self.board.board:
            if cell.isdigit():
                return False

        return True

    def restart_game(self):
        self.board.reset_board()
        self.current_player = 0
        clear_screen()

    def quit_game(self):
        print("Thank you for playing!")
        exit()