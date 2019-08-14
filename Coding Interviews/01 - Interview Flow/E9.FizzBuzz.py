class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here

        hash, result = {3: "fizz", 5: "buzz"}, []

        for i in range(1, n + 1):
            word = []

            for key, value in hash.items():
                if i % key == 0 and i >= key:
                    word.append(value)

            while not word:
                word.append(str(i))

            result.append(" ".join(word))

        return result

# leetcode
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         word_hash, result = {3: "Fizz", 5: "Buzz"}, []
#
#         for i in range(1, n + 1):
#             word = ""
#             for key, value in word_hash.items():
#                 if i >= key and i % key == 0:
#                     word += value
#
#             if not word:
#                 word = str(i)
#
#             result.append(word)
#
#         return result
