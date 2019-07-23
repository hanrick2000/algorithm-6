class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                return mid

            if A[mid] > A[left]:
                if A[mid] >= target >= A[left]:
                    right = mid
                else:
                    left = mid
            else:
                if A[mid] <= target <= A[right]:
                    left = mid
                else:
                    right = mid

        if A[left] == target:
            return left

        if A[right] == target:
            return right

        return -1
