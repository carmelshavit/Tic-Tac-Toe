from player import Player
from board import Board


class TicTacGame:
    def __init__(
            self,
            board: Board,
    ):
        self._board = board
        self._player1 = None
        self._player2 = None

    def start_game(self):
        self._board._create_new_board()
        player = self.determine_starter()
        while True:
            input_move = player.get_move_input(player)

            if not self.is_valid_input(input_move):
                continue
            if not self.is_valid_move(input_move):
                continue

                #Player.submit_move(player, input_move)
            player.submit_move(input_move)
            self._board.print_board()
            if not self.check_full_board(self._board):
                continue
            player = self.switch_player(player)

    def is_valid_input(self, move_input: int) -> bool:
        return self._board.is_cell_in_board(move_input)

    def is_valid_move(self, move_input: int):
        if self._board.is_empty_cell(move_input):
            return True
        else:
            print("This position already taken, Please choose another one")
            return False

    def determine_starter(self) -> Player:
        while True:
            marker = input("Choose 'X' or 'O' ")
            if marker == 'X':
                self._player1 = Player(True, self._board, marker)
                self._player2 = Player(False, self._board, marker='O')
                return self._player1
            elif marker == 'O':
                self._player1 = Player(True, self._board, marker)
                self._player2 = Player(False, self._board, marker='X')
                return self._player2
            print("Invalid input")

    def switch_player(self, player: Player) -> Player:
        if player is self._player1:
            return self._player2
        elif player is self._player2:
            return self._player1
        else:
            raise ValueError



if __name__ == '__main__':
    def main():
        board = Board()
        game = TicTacGame(board)
        game.start_game()
    main()
