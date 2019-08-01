class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if not A or target is None:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                right = mid
            else:
                left = mid

        if target - A[left] < A[right] - target:
            return left
        else:
            return right
