class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return

        temp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, temp)

    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.mergeSort(A, start, mid, temp)
        self.mergeSort(A, mid + 1, end, temp)
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):
        mid = (start + end) // 2
        left, right = start, mid + 1
        index = left

        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right]
                right += 1
            index += 1

        while left <= mid:
            temp[index] = A[left]
            index += 1
            left += 1

        while right <= end:
            temp[index] = A[right]
            index += 1
            right += 1

        for i in range(start, end + 1):
            A[i] = temp[i]
