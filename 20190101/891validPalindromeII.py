class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        # Write your code here
        left, right = 0, len(s) - 1
        isDeleteOne = False

        while left < right:
            if s[left] != s[right]:
                if s[left + 1] == s[right] and isDeleteOne == False:
                    isDeleteOne = True
                    left += 1
                elif s[left] == s[right - 1] and isDeleteOne == False:
                    isDeleteOne = True
                    right -= 1
                else:
                    return False
            else:
                left += 1
                right -= 1

        return True
