class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here

        # method 2:
        return self.placeQueen([0] * n, 0, 0)

    def placeQueen(self, cols, row, count):
        size = len(cols)
        if row == size:
            return count + 1

        for i in range(size):
            if self.is_valid(cols, row, i):
                cols[row] = i
                count = self.placeQueen(cols, row + 1, count)

        return count

    def is_valid(self, cols, row, col):
        for i in range(row):
            if cols[i] == col:
                return False

            if row - i == abs(col - cols[i]):
                return False

        return True


    #     # method 1:
    #     usedColumns = [0] * (n + 1)

    #     self.placeQueen(usedColumns, 1)

    #     return usedColumns[0]

    # def placeQueen(self, cols, row):
    #     size = len(cols)
    #     if row == size:
    #         cols[0] += 1
    #         return

    #     for i in range(1, size):
    #         if self.is_valid(cols, row, i):
    #             cols[row] = i
    #             self.placeQueen(cols, row + 1)

    # def is_valid(self, cols, row, col):
    #     for i in range(1, row):
    #         if cols[i] == col:
    #             return False

    #         if row - i == abs(col - cols[i]):
    #             return False

    #     return True
