# method 3
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        self.quick_sort(nums, 0, len(nums) - 1, k)

        results = []
        for i in range(k):
            results.append(nums[i])
        return results

    def quick_sort(self, nums, start, end, k):
        if start >= k or start >= end:
            return

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1

            if left > right:
                continue

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        self.quick_sort(nums, start, right, k)
        self.quick_sort(nums, left, end, k)

# # method 2
# class Solution:
#     """
#     @param nums: an integer array
#     @param k: An integer
#     @return: the top k largest numbers in array
#     """
#     def topk(self, nums, k):
#         # write your code here
#         heapq.heapify(nums)

#         results = heapq.nlargest(k, nums)
#         results.sort(reverse = True)

#         return results

# # method 1, fastest
# import heapq

# class Solution:
#     """
#     @param nums: an integer array
#     @param k: An integer
#     @return: the top k largest numbers in array
#     """
#     def topk(self, nums, k):
#         # write your code here
#         results, heap = [], []
#         for num in nums:
#             heapq.heappush(heap, (-num))

#         for i in range(k):
#             results.append(-heapq.heappop(heap))
#         return results
