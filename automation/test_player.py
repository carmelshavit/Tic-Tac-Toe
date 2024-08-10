from tic_tac_toe.board import Board
from tic_tac_toe.player import Player


def test_opposite_marker():
    board = Board()
    p1 = Player(is_human=True, board=board, marker="X")
    assert p1.marker == "X"
    assert p1.opposite_marker == "O"


