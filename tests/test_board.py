from tic_tac_toe.board import Board


def test_is_empty_cell_on_new_board(cell_id):
    # Test all cells on a new board to ensure they are empty
    board = Board()
    for cell_id in range(1, 10):
        assert board.is_empty_cell(cell_id) is True


def test_put_value_in_cell(cell_id):
    board = Board()
    assert test_is_empty_cell_on_new_board(cell_id) is True
    board.put_value_in_cell(5, 'X')
    assert board.is_empty_cell(5) is False

    for cell_id in range(1, 10):
        if cell_id != 5:
            assert board.is_empty_cell(cell_id) is True


def test_is_cell_in_board(cell_id):
    if not 0 <= cell_id <= 9:
        assert ValueError


def test_get_row():
    board = Board()
    board.put_value_in_cell(5, 'X')
    assert board.get_row(5) is 1


def get_column():
    board = Board()
    board.put_value_in_cell(5, 'X')
    assert board.get_row(5) is 1
