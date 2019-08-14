class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here

        # method 1:
        # counts, result = collections.Counter(S), 0

        # for char in J:
        #     result += counts.get(char, 0)

        # return result

        # method 2:
        # return sum(each in J for each in S)

        # method 3:
        return len([x for x in S if x in J])
