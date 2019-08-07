class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        prefix_hash, sum, count = {0: 1}, 0, 0

        for num in nums:
            sum += num
            if sum - k in prefix_hash:
                count += prefix_hash[sum - k]

            prefix_hash[sum] = prefix_hash.get(sum, 0) + 1

        return count
