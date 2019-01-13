class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        if not A:
            return

        # method two: shiftdown O(n)
        for i in range((len(A) - 1) // 2, -1, -1):
            self.shiftdown(A, i)

    def shiftdown(self, A, i):
        while i * 2 + 1 < len(A):
            # get the index of the left son
            sonIndex = i * 2 + 1
            if sonIndex + 1 < len(A) and A[sonIndex] > A[sonIndex + 1]:
                # get the index of the right son
                sonIndex += 1
            if A[sonIndex] > A[i]:
                break

            A[sonIndex], A[i] = A[i], A[sonIndex]

            i = sonIndex

    #     # method one: shiftup O(nlog(n))
    #     for i in range(len(A)):
    #         self.shiftup(A, i)

    # def shiftup(self, A, i):
    #     while i > 0:
    #         fatherIndex = (i - 1) // 2
    #         if A[fatherIndex] < A[i]:
    #             break

    #         A[fatherIndex], A[i] = A[i], A[fatherIndex]

    #         i = fatherIndex
