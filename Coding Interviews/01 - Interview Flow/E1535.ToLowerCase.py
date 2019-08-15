class Solution:
    """
    @param str: the input string
    @return: The lower case string
    """
    def toLowerCase(self, str):
        # Write your code here
        # result = []
        # for c in str:
        #     if 65 <= ord(c) <= 90:
        #         c = chr(ord(c) + 32)
        #     result.append(c)

        # return ''.join(result)

        # return ''.join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)

        # return "".join(chr(ord(c) | 32) for c in str)
