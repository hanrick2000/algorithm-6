class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        if not string:
            return length

        size = length
        for c in string:
            if c == ' ':
                size += 2

        index = size - 1
        for i in range(length - 1, -1, -1):
            if string[i] == ' ':
                string[index], string[index - 1], string[index - 2] = '0', '2', '%'
                index -= 3
            else:
                string[index] = string[i]
                index -= 1

        return size
