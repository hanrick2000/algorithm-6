class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix), len(matrix[0])
        start, end = 0, row * col - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            x, y = mid // col, mid % col
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid

        if self.is_match(matrix, start, col, target):
            return True

        if self.is_match(matrix, end, col, target):
            return True

        return False

    def is_match(self, matrix, index, col, target):
        x, y = index // col, index % col
        if matrix[x][y] == target:
            return True

        return False
