from typing import Any


class Board:
    EMPTY_CELL_VALUE = None
    SIZE_BOARD = 3

    def __init__(self, board_matrix=None):
        if board_matrix == None:
            self._board_matrix = self._create_new_board()
        else:
            self._board_matrix = board_matrix

    def is_empty_cell(self, cell_id: int) -> bool:
        # if not self.is_cell_in_board(): ...
        row = self.get_row(cell_id)
        column = self.get_column(cell_id)
        return self._board_matrix[row][column] == self.EMPTY_CELL_VALUE

    def put_value_in_cell(self, cell_id: int, value: Any):
        row = self.get_row(cell_id)
        column = self.get_column(cell_id)
        self._board_matrix[row][column] = value

    def get_value_from_cell_id(self, cell_id) -> Any:
        row = self.get_row(cell_id)
        column = self.get_column(cell_id)
        return self._board_matrix[row][column]

    def is_cell_in_board(self, cell_id: int) -> bool:
        return 1 <= cell_id <= 9

    def get_row(self, cell_id: int) -> int:  ##input//3
        if cell_id in (1, 2, 3):
            return 0
        elif cell_id in (4, 5, 6):
            return 1
        elif cell_id in (7, 8, 9):
            return 2
        else:
            raise ValueError("Cell not in board")

    # def get_value_rows(self) -> list[list[int]]:
    #     value_rows = []
    #     for idx in range(board.SIZE_BOARD):
    #         row = self._board_matrix[idx]
    #         value_rows.append(row)
    #     return value_rows

    def get_value_row(self, row_idx: int) -> list[int]:
        # return self._board_matrix[row_idx].copy()
        row = self._board_matrix[row_idx]  # [0, 0, 'X']
        value_row = []
        for cell_value in row:
            value_row.append(cell_value)
        return value_row

    # assert board.get_value_row()==["O","",""]
    def get_column(self, cell_id: int) -> int:  # input-1 %3
        if cell_id in (1, 4, 7):
            return 0
        elif cell_id in (2, 5, 8):
            return 1
        elif cell_id in (3, 6, 9):
            return 2
        else:
            raise ValueError("Cell not in board")

    def get_value_column(self, col_idx: int) -> list[int]:  ##input-1 %3
        col = []
        for row in self._board_matrix:
            col.append(row[col_idx])
        return col

    def get_value_diag_asend(self) -> list[int]:  ##input-1 %3
        # return [
        # self._board_matrix[2][0],
        # self._board_matrix[1][1],
        # self._board_matrix[0][2],
        # ]
        diag = []
        for i in range(len(self._board_matrix)):
            j = len(self._board_matrix) - 1
            j -= i
            diag.append(self._board_matrix[j][i])

        return diag

    def get_value_diag_decnd(self) -> list[int]:  ##input-1 %3
        diag = []
        for i in range(len(self._board_matrix)):
            diag.append(self._board_matrix[i][i])
        return diag

    def check_full_board(self):
        size = len(self._board_matrix)
        for rowIdx in range(size):
            for value in self.get_value_row(rowIdx):
                if value == self._board.is_empty_cell:
                    print("You bet and no one won")
                    return True
                else:
                    return False

    def print_board(self):
        for row in self._board_matrix:
            for value in row:
                print(value, end=" ")
            print()  # print(end="/n")

    @staticmethod
    def _create_new_board():
        # Always 3x3 board
        """
        new_list = [i for i in range(3)]

        new_list = list()
        for i in range(3):
            new_list.append(i)

        """
        return [
            [Board.EMPTY_CELL_VALUE for _ in range(3)]
            for _ in range(3)
        ]


board = Board()
