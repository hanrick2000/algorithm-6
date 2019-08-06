"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        # method 2
        return self.dfs(nestedList, 1)

    def dfs(self, nestedList, depth):
        result = 0
        if not nestedList:
            return result

        for item in nestedList:
            if item.isInteger():
                result += depth * item.getInteger()
            else:
                result += self.dfs(item.getList(), depth + 1)

        return result

        # # method 1
        # result = 0

        # if not nestedList:
        #     return result

        # stack = []
        # for item in nestedList:
        #     stack.append((item, 1))

        # while stack:
        #     item, depth = stack.pop()
        #     if item.isInteger():
        #         result += depth * item.getInteger()
        #     else:
        #         for num in item.getList():
        #             stack.append((num, depth + 1))

        # return result
