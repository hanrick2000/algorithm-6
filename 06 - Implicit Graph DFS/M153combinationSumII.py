class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        results = []
        if not num:
            return results

        num.sort()

        self.dfs(num, 0, [], target, results)

        return results

    def dfs(self, num, start, combination, target, results):
        if target == 0:
            results.append(list(combination))
            return

        for i in range(start, len(num)):
            if i != start and num[i] == num[i - 1]:
                continue

            if target < num[i]:
                break

            combination.append(num[i])
            self.dfs(num, i + 1, combination, target - num[i], results)
            combination.pop()
