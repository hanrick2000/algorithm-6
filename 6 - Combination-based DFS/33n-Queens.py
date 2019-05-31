class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        results = []

        self.placeQueens([0] * n, 0, ['.' * n] * n, results)

        return results

    def placeQueens(self, cols, row, subset, results):
        size = len(cols)

        if row == size:
            results.append(list(subset))
            return

        for i in range(size):
            if self.is_valid(cols, row, i):
                cols[row] = i

                prefix, suffix = subset[row][:i], subset[row][i + 1:]
                subset[row] = prefix + 'Q' + suffix
                self.placeQueens(cols, row + 1, subset, results)
                subset[row] = prefix + '.' + suffix

    def is_valid(self, cols, row, col):
        for i in range(row):
            if cols[i] == col:
                return False

            if row - i == abs(cols[i] - col):
                return False

        return True
