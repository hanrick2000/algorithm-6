public class Solution {
    /**
     * @param s: a string
     * @return: return a string
     */
    public String reverseString(String s) {
        // write your code here
        char[] str = s.toCharArray();
        int right = str.length - 1;

        for (int i = 0; i < (right + 1) / 2; i++) {
            char tmp = str[i];
            str[i] = str[right - i];
            str[right - i] = tmp;
        }

        return new String(str);
    }
}
