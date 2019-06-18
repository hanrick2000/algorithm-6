class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        sizeA = len(A)
        lineSizeA = len(A[0])
        lineSizeB = len(B[0])

        result = [[0] * lineSizeB for _ in range(sizeA)]

        for i in range(sizeA):
            for j in range(lineSizeA):
                if A[i][j] != 0:
                    for k in range(lineSizeB):
                        result [i][k] += A[i][j] * B[j][k]

        return result
