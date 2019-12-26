public class Solution {
    /**
     * @param source:
     * @param target:
     * @return: return the index
     */
    public int strStr(String source, String target) {
        // Write your code here
        if (source == null || target == null) return -1;

        int size_s = source.length(), size_t = target.length();
        for (int i = 0; i < size_s - size_t + 1; i++) {
            int j = 0;
            while (j < size_t) {
                if (source.charAt(i + j) != target.charAt(j)) break;
                j++;
            }

            if (j == size_t) return i;
        }

        return -1;
    }
}
