class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        result = 0

        if matrix is None or target is None:
            return result

        # From the left bottom corner to check each one
        x, y = len(matrix) - 1, 0
        while x > -1 and y < len(matrix[x]):
            if matrix[x][y] == target:
                result += 1
                x -= 1
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1

        return result
