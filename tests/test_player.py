from tic_tac_toe.board import Board
from tic_tac_toe.player import Player


def test_opposite_marker():
    board = Board()
    p1 = Player(is_human=True, board=board, marker="X")
    assert p1.marker == "X"
    assert p1.opposite_marker == "O"


def test_submit_move():  # call submit_move and check if the marker in cell_id changed
    board = Board()
    p1 = Player(is_human=True, board=board, marker="X")
    p1.submit_move(3)
    assert board.get_value_from_cell_id(3) == "X"


def test_check_complete_row():
    board = Board()
    p1 = Player(is_human=True, board=board, marker="X")
    p1.submit_move(4)
    p1.submit_move(5)
    assert p1.check_complete_row(p1.marker) == 6  # return True
    assert p1.check_complete_row(p1.marker) == 7  #return None

    # create current stage with markers on the row and check if return cell_id
    # create current stage without markers and check if return None

    # @pytest.fixture
    # def board_with_top_row_x():
    #     return Board([['X', 'X', 'X'], ["", "", ""], ["", "", ""]])

    p1 = Player(is_human=True, board=board, marker="X")
