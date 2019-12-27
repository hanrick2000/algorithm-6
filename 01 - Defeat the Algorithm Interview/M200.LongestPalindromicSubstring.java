public class Solution {
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */
    public String longestPalindrome(String s) {
        // write your code here
        if (s == null || s.length() == 0) return "";

        int start = 0, len = 0, longest = 0;
        for (int i = 0; i < s.length(); i++) {
            len = findPalindromeLength(s, i, i);
            if (len > longest) {
                longest = len;
                start = i - len / 2;
            }
            len = findPalindromeLength(s, i, i + 1);
            if (len > longest) {
                longest = len;
                start = i - len / 2 + 1;
            }
        }

        return s.substring(start, start + longest);
    }

    private int findPalindromeLength(String s, int l, int r) {
        int len = 0;

        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            len += l == r ? 1 : 2;
            l--;
            r++;
        }

        return len;
    }
}
