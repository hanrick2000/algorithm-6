class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here

        # method 4
        # nums.sort()
        # return nums[len(nums) // 2]

        # method 3
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # return candidate


        # counts = collections.Counter(nums)

        # method 2
        # return max(counts.keys(), key = counts.get)

        # method 1
        # for key, value in sorted(counts.items(), key = lambda kv:(kv[1], kv[0]), reverse = True):
        #     return key

            
