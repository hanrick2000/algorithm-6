public class Solution {
    /*
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    public int replaceBlank(char[] string, int length) {
        // write your code here
        if (string == null || length == 0) return length;

        int size = length;
        for (int i = 0; i < length; i++) {
            if (string[i] == ' ') size += 2;
        }

        string[size] = 0;
        int index = size - 1;
        for (int i = length - 1; i >= 0; i--) {
            if (string[i] == ' ') {
                string[index--] = '0';
                string[index--] = '2';
                string[index--] = '%';
            } else {
                string[index--] = string[i];
            }
        }

        return size;
    }
}
