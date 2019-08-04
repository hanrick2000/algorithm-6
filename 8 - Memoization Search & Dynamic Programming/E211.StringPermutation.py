class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here

        # method 2
        counts = collections.Counter(A)
        left, right = 0, len(B) - 1
        while left <= right:
            if B[left] in counts:
                counts[B[left]] -= 1
            else:
                return False

            if right != left:
                if B[right] in counts:
                    counts[B[right]] -= 1
                else:
                    return False

            left += 1
            right -= 1

        for key, value in counts.items():
            if value:
                return False

        return True

        # # method 1
        # A = sorted(A)
        # B = sorted(B)

        # return A == B
