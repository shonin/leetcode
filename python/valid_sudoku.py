class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.row_is_valid(row):
                return False

        for i in range(9):
            column = [row[i] for row in board]
            if not self.row_is_valid(column):
                return False

        for i in range(3):
            board_slice = board[i * 3:i * 3 + 3]
            for j in range(3):
                dummy_row = []
                for k in range(3):
                    dummy_row += board_slice[k][j * 3:j * 3 + 3]
                if not self.row_is_valid(dummy_row):
                    return False

        return True

    def row_is_valid(self, row):
        s_row = row.copy()
        s_row.sort()
        for i in range(8): # 8 prevents out of bounds
            if s_row[i] == '.':
                continue
            if s_row[i] == s_row[i+1]:
                return False
        return True
