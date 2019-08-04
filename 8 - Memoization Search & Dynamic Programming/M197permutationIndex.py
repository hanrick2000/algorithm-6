class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here

        permutaion, result = 1, 1
        if A is None:
            return result

        for i in range(len(A) - 2, -1, -1):
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1

            result += smaller * permutaion
            permutaion *= len(A) - i

        return result
