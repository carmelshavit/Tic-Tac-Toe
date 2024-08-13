from tic_tac_toe.tic_tac_toe_game import TicTacGame
from tic_tac_toe.board import Board


def test_is_valid_move():
    board = Board()
    #Board([["","","X"],["","",""],["","",""]])
    game = TicTacGame(board)
    player = game.prepare_game()
    player.submit_move(3)
    assert game.is_valid_move(3) is False
    assert game.is_valid_move(4) is True
    # current stage, use method, check the outcome


def test_is_valid_input():
    board = Board()
    game = TicTacGame(board)
    player = game.prepare_game()
    player.submit_move(3)
    assert board.is_cell_in_board(3) is True
    player.submit_move(10)
    assert board.is_cell_in_board(10) is False


def test_switch_player():
    board = Board()
    game = TicTacGame(board)
    game.set_players_for_game(False, False, 'X', 'O')
    player1 = game.prepare_game()
    game.switch_player()
    assert player1 is game.player2
