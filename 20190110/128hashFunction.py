class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        magicNumber, result = 33, 0

        for char in key:
            result = (result * magicNumber + ord(char)) % HASH_SIZE

        return result
