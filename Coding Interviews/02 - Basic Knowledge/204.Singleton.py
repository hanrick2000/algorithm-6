class Solution:
    instance = None

    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        # write your code here
        if not cls.instance:
            cls.instance = Solution()

        return cls.instance
