from player import Player
from board import Board


class TicTacGame:
    def __init__(self, board: Board):
        self._board = board
        self._player1 = None
        self._player2 = None

        self._current_player = None

    @property
    def current_player(self):
        return self._current_player

    @current_player.setter
    def current_player(self, player):
        self.current_player = player

    @property
    def player1(self):
        return self._player1

    @player1.setter
    def player1(self, player):
        self._player1 = player

    @property
    def player2(self):
        return self._player2

    @player2.setter
    def player2(self, player):
        self._player2 = player

    def start_game(self):
        player = self.prepare_game()
        self._current_player = player
        self.start_round()

    def start_round(self, input_move=None):
        while True:
            if input_move is None:
                input_move = self._current_player.get_move_input()

            if not self.is_valid_input(input_move):
                continue
            if not self.is_valid_move(input_move):
                continue

                # Player.submit_move(player, input_move)
            self.current_player.submit_move(input_move)
            self._board.print_board()
            if not self._board.check_full_board():
                continue
            self.current_player = self.switch_player()

    def prepare_game(self):
        self._board._create_new_board()
        player = self.determine_starter()
        return player

    def is_valid_input(self, move_input: int) -> bool:
        return self._board.is_cell_in_board(move_input)

    def is_valid_move(self, move_input: int):
        if self._board.is_empty_cell(move_input):
            return True
        else:
            print("This position already taken, Please choose another one")
            return False

    def set_players_for_game(self, p1_is_human, p2_is_human, p1_marker, p2_marker):
        self.player1 = Player(p1_is_human, self._board, p1_marker)
        self.player2 = Player(p2_is_human, self._board, p2_marker)

        self._current_player = None  # p1? p2?

    def determine_starter(self) -> Player:
        # condition for check if both players are computer. if true: return player1 to start
        if self.set_players_for_game(False, False, 'X', 'O'):
            return self.player1
        while True:
            marker = input("Choose 'X' or 'O' ")
            # TODO: Use set_players_for_game
            if marker == 'X':
                self.set_players_for_game(True, False, 'X', 'O')
                return self.player1
            elif marker == 'O':
                self.set_players_for_game(True, False, 'O', 'X')
                return self.player2
            print("Invalid input")

    def switch_player(self):
        if self.current_player is self.player1:
            self.current_player = self.player2
        elif self.current_player is self.player2:
            self.current_player = self.player1
        else:
            raise ValueError


if __name__ == '__main__':
    def main():
        board = Board()
        game = TicTacGame(board)
        game.start_game()


    main()
