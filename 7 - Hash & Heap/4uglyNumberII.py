# method 2
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        numbs, steps = [1], [0, 0, 0]

        for _ in range(n - 1):
            value2, value3, value5 = numbs[steps[0]] * 2, numbs[steps[1]] * 3, numbs[steps[2]] * 5

            minValue = min(value2, value3, value5)
            if value2 == minValue:
                steps[0] += 1
            if value3 == minValue:
                steps[1] += 1
            if value5 == minValue:
                steps[2] += 1

            numbs.append(minValue)

        return numbs[-1]

# # methon 1
# import heapq

# class Solution:
#     """
#     @param n: An integer
#     @return: return a  integer as description.
#     """
#     def nthUglyNumber(self, n):
#         # write your code here
#         heap, visited = [1], set([1])

#         result = None

#         for i in range(n):
#             result = heapq.heappop(heap)
#             for allowed in [2, 3, 5]:
#                 if result * allowed not in visited:
#                     visited.add(result * allowed)
#                     heapq.heappush(heap, result * allowed)

#         return result
