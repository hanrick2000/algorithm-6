class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A or target is None:
            return 0

        size = len(A)
        left, right = 0, size - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] >= target:
                right = mid
            else:
                left = mid

        if A[left] == target:
            first_index = left
        elif A[right] == target:
            first_index = right
        else:
            first_index = -1

        left, right = first_index if first_index else 0, size - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid

        if A[right] == target:
            last_index = right
        elif A[left] == target:
            last_index = left
        else:
            last_index = -1

        if last_index > -1 and first_index > -1:
            return last_index - first_index + 1
        else:
            return 0
