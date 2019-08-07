class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here

        # method 2:
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1

        while n > 0:
            A[m + n - 1] = B[n - 1]
            n -= 1

        # method 1:
        # i, j = m - 1, n - 1
        # index = m + n - 1

        # while i >= 0 or j >= 0:
        #     if i < 0 or (j >= 0 and B[j] > A[i]):
        #         A[index] = B[j]
        #         j -= 1
        #     else:
        #         A[index] = A[i]
        #         i -= 1
        #     index -= 1
