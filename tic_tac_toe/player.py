import random
from typing import Literal

from tic_tac_toe.board import Board
from random import random


class Player:

    def __init__(self, is_human: bool, board: Board, marker: Literal['X', 'O']):
        self._marker = marker
        self._is_human = is_human
        self._board = board

    # Works if move is public

    def __eq__(self, other):
        if self.marker == other.marker:
            return True
        else:
            return False

    def change_value(self, new_value: int):
        self.move.value(new_value)  # GOOD
        self.move._value = new_value  # BAD

    # Works if _move is protected
    def change_value2(self, new_value: int):
        self._move._value = new_value  # BAD, twice
        self.move._value = new_value  # GOOD, then BAD
        self.move.value(new_value)  # GOOD, calls the setter

    # self.move(Move(new_value))  # GOOD, calls the setter with a new instance object. destroy instance exist.
    # self.move is protected, use classic getter/setter
    def change_value3(self, new_value: int):
        self._move._value = new_value  # BAD, twice
        self.get_move()._value = new_value  # GOOD, then BAD
        self.get_move().value(new_value)  # GOOD, calls the setter
        #self.set_move(Move(new_value))  # GOOD, calls the setter with a new instance object. destroy instance exist.

    @property
    def marker(self) -> Literal['X', 'O']:
        return self._marker

    @property
    def opposite_marker(self) -> Literal['X', 'O']:
        if self.marker == 'X':
            return 'O'
        elif self.marker == 'O':
            return 'X'
        else:
            raise ValueError

    @marker.setter
    def marker(self, val: Literal['X', 'O']):
        self._marker = val

    @property
    def board(self):
        return self._board

    def get_human_input(self) -> int:
        return int(input("Please enter your move (1-9)"))

    def get_move_input(self, player) -> int:
        if player.is_human:
            user_input = self.get_human_input()
            return user_input
        else:
            computer_input = self.get_computer_move(self.marker)
            return computer_input

    def submit_move(self, cell_id: int):
        if self.marker is None:
            raise ValueError
        self._board.put_value_in_cell(cell_id, self.marker)

    def get_computer_move(self, marker) -> int:
        pass

    def get_computer_move2(self, marker) -> int:

        cell_value = self.check_complete_row(marker)
        if cell_value is not None:
            return cell_value
        cell_value = self.check_complete_row(self.opposite_marker)
        if cell_value is not None:
            return cell_value
        cell_value = self.check_complete_column(marker)
        if cell_value is not None:
            return cell_value
        cell_value = self.check_complete_column(self.opposite_marker)
        if cell_value is not None:
            return cell_value

    def check_complete_row(self, marker) -> int | None:  # X
        for idx in range(self.board.SIZE_BOARD):
            row = self.board.get_value_row(idx)
            found_empty_cell = False
            cell_id = None
            for value, row_idx in row:
                if value not in (marker, self.board.EMPTY_CELL_VALUE):
                    found_empty_cell = False
                    break
                # value is marker or empty
                elif value == self.board.EMPTY_CELL_VALUE:
                    if found_empty_cell is True:
                        found_empty_cell = False
                        break
                found_empty_cell = True
                cell_id = row_idx  #["X", "X", ""]

                # value is marker or empty, and all values are marker, or up to 1 empty
            if found_empty_cell is True:
                return cell_id

    def check_complete_column(self, marker) -> bool | None:  # 'X'
        for idx_column in range(self.board.SIZE_BOARD):
            col = self.board.get_column(idx_column)
            found_empty_cell = False
            cell_id = None
            for value, col_idx in col:
                if value not in (marker, self.board.EMPTY_CELL_VALUE):  #'O'
                    found_empty_cell = False
                    continue
                elif value is self.board.EMPTY_CELL_VALUE:  #' '
                    if found_empty_cell is True:
                        found_empty_cell = False
                        break
                found_empty_cell = True
                cell_id = col_idx

                # value is marker or empty, and all values are marker, or up to 1 empty
            if found_empty_cell is True:
                return cell_id

    def check_win_diagnose(self) -> bool:
        pass

    def check_defeat(self) -> bool:
        pass
