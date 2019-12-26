public class Solution {
    /**
     * @param s: a string which consists of lowercase or uppercase letters
     * @return: the length of the longest palindromes that can be built
     */
    public int longestPalindrome(String s) {
        // write your code here
        // // method 1:
        // Set<Character> hashset = new HashSet<>();

        // for (char ch: s.toCharArray()) {
        //     if (hashset.contains(ch)) {
        //         hashset.remove(ch);
        //     } else {
        //         hashset.add(ch);
        //     }
        // }

        // int size = s.length();
        // if (hashset.size() > 0) size -= hashset.size() - 1;

        // return size;

        // method 2:
        int[] set = new int[128];

        for (char ch: s.toCharArray()) {
            set[ch]++;
        }

        int count = 0;
        for (int c: set) {
            count += c / 2 * 2;
            if (count % 2 == 0 && c % 2 == 1) {
                count++;
            }
        }

        return count;
    }
}
