class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code her
        result = 0;
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return result

        size = len(matrix)
        lineSize = len(matrix[0])
        for i in range(size):
            lineArray = [0] * lineSize
            for j in range(i, size):
                for k in range(lineSize):
                    lineArray[k] += matrix[j][k]
                result = max(result, self.maxSubarray(lineArray))

        return result

    def maxSubarray(self, array):
        result, sum = 0, 0

        for i in range(len(array)):
            sum += array[i]
            result = max(result, sum)
            sum = max(sum, 0)

        return result
