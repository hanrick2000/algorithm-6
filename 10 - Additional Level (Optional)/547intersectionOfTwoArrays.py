class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here

        # method 1: sorted and merged
        results, i, j = [], 0, 0

        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not results or results[-1] != nums1[i]:
                    results.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return results
