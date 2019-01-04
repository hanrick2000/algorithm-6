class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return

        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        left, right = start, end

        if left > right:
            return

        pivot = A[(left + right) // 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
