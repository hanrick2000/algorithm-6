public class Solution {
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        // write your code here
        if (s == null || s.length() == 0) return true;

        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (!isAlNum(s.charAt(l))) {
                l++;
                continue;
            }

            if (!isAlNum(s.charAt(r))) {
                r--;
                continue;
            }

            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;
            l++;
            r--;
        }

        return true;
    }

    private boolean isAlNum(char ch) {
        return Character.isLetter(ch) || Character.isDigit(ch);
    }
}
