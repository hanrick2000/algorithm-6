class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return

        # method 3: mergeSort
    #     self.mergeSort(A, 0, len(A) - 1)

    # def mergeSort(self, A, start, end):
    #     if start >= end:
    #         return

    #     mid = (start + end) // 2
    #     self.mergeSort(A, start, mid)
    #     self.mergeSort(A, mid + 1, end)

    #     self.merge(A, start, end)

    # def merge(self, A, start, end):
    #     mid = (start + end) // 2
    #     left, right, tmp = start, mid + 1, []

    #     while left <= mid and right <= end:
    #         if A[left] < A[right]:
    #             tmp.append(A[left])
    #             left += 1
    #         else:
    #             tmp.append(A[right])
    #             right += 1

    #     while left <= mid:
    #         tmp.append(A[left])
    #         left += 1

    #     while right <= end:
    #         tmp.append(A[right])
    #         right += 1

    #     for i in range(len(tmp)):
    #         A[start + i] = tmp[i]

        # method 2: quickSort
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        if start >= end:
            return

        pivot = self.partition(A, start, end)

        self.quickSort(A, start, pivot - 1)
        self.quickSort(A, pivot + 1, end)

    def partition(self, A, start, end):
        pivot = A[end]

        i = start - 1
        for j in range(start, end):
            if A[j] <= pivot:
                i += 1
                if j != i:
                    A[i], A[j] = A[j], A[i]

        A[i + 1], A[end] = pivot, A[i + 1]

        return i + 1

        # method 1: mergeSort
    #     temp = [0] * len(A)
    #     self.mergeSort(A, 0, len(A) - 1, temp)

    # def mergeSort(self, A, start, end, temp):
    #     if start >= end:
    #         return

    #     mid = (start + end) // 2
    #     self.mergeSort(A, start, mid, temp)
    #     self.mergeSort(A, mid + 1, end, temp)
    #     self.merge(A, start, end, temp)

    # def merge(self, A, start, end, temp):
    #     mid = (start + end) // 2
    #     left, right = start, mid + 1
    #     index = left

    #     while left <= mid and right <= end:
    #         if A[left] < A[right]:
    #             temp[index] = A[left]
    #             left += 1
    #         else:
    #             temp[index] = A[right]
    #             right += 1
    #         index += 1

    #     while left <= mid:
    #         temp[index] = A[left]
    #         index += 1
    #         left += 1

    #     while right <= end:
    #         temp[index] = A[right]
    #         index += 1
    #         right += 1

    #     for i in range(start, end + 1):
    #         A[i] = temp[i]
