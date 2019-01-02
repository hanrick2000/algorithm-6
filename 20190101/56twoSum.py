class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        # method two
        ans = [-1, -1]
        if numbers is None or target is None:
            return ans

        hashMap = {}
        left, right = 0, len(numbers) - 1
        while left <= right:
            if (target - numbers[left]) in hashMap:
                ans[0], ans[1] = left, hashMap[target - numbers[left]]
                break
            hashMap[numbers[left]] = left
            left += 1

            if target - numbers[right] in hashMap:
                ans[0], ans[1] = hashMap[target - numbers[right]], right
                break

            hashMap[numbers[right]] = right
            right -= 1

        if ans[0] > ans[1]:
            ans[0], ans[1] = ans[1], ans[0]

        return ans

        # # method one
        # ans = [-1, -1]
        # if numbers is None or target is None:
        #     return ans

        # left, right = 0, len(numbers) - 1
        # array = sorted(numbers)

        # while left < right:
        #     if array[left] + array[right] == target:
        #         ans = [left, right]
        #         break

        #     if array[left] + array[right] > target:
        #         right -= 1
        #         continue

        #     if array[left] + array[right] < target:
        #         left += 1

        # if ans[0] > -1:
        #     left, right = -1, -1
        #     for i in range(len(numbers)):
        #         if numbers[i] == array[ans[0]] and left == -1:
        #             left = i
        #         elif numbers[i] == array[ans[1]]:
        #             right = i

        #         if left > -1 and right > -1:
        #             break

        #     if left < right:
        #         ans = [left, right]
        #     else:
        #         ans = [right, left]

        # return ans
