class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here

        # # method 2:
        # num = 0
        # for i in A:
        #     num ^= i

        # return num

        # # method 1:
        return 2 * sum(set(A)) - sum(A)

# leetCode
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         counts = collections.Counter(nums)
#         for key, value in counts.items():
#             if value == 1:
#                 return key
