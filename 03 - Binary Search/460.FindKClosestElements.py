class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        index = self.find_first_index(A, target)
        left, right, result = index - 1, index, []

        for i in range(k):
            if left < 0:
                result.append(A[right])
                right += 1
            elif right == len(A):
                result.append(A[left])
                left -= 1
            else:
                if target - A[left] <= A[right] - target:
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1

        return result

    def find_first_index(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid

        if A[left] >= target:
            return left

        if A[right] >= target:
            return right

        return len(A)
