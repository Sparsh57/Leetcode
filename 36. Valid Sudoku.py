import numpy as np
class Solution:
    def rows(self, board):
        for i in board:
            k = i.copy()
            k = [x for x in k if x != '.']
            if len(k)!=len(set(k)):
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.rows(board):
            print('r')
            return False
        if not self.rows(np.transpose(board)):
            print("t")
            return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                k = []
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        k.append(board[m][n])
                if not self.rows([k]):
                    print(m, n)
                    return False
        return True
