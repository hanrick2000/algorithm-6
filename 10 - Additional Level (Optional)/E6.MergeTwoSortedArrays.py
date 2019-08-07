class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        i, j, nums = 0, 0, []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                nums.append(A[i])
                i += 1
            else:
                nums.append(B[j])
                j += 1

        while i < len(A):
            nums.append(A[i])
            i += 1

        while j < len(B):
            nums.append(B[j])
            j += 1

        return nums
