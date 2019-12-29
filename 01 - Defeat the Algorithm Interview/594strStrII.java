public class Solution {
    /*
     * @param source: A source string
     * @param target: A target string
     * @return: An integer as index
     */
    public int strStr2(String source, String target) {
        // write your code here
        if (source == null || target == null) return -1;

        int size_s = source.length(), size_t = target.length();
        if (size_t == 0)
            return size_t;
        else if (size_s == 0)
            return -1;

        int magic_code = 31, base = Integer.MAX_VALUE / magic_code;
        int power = 1;
        for (int i = 0; i < size_t; i++) {
            power = (power * magic_code) % base;
        }

        int hash_t = 0;
        for (int i = 0; i < size_t; i++) {
            hash_t = (hash_t * magic_code + target.charAt(i) - 'a') % base;
        }

        int hash_s = 0;
        for (int i = 0; i < size_s; i++) {
            hash_s = (hash_s * magic_code + source.charAt(i) - 'a') % base;

            if (i < size_t - 1) continue;
            if (i >= size_t) {
                hash_s -= ((source.charAt(i - size_t) - 'a') * power) % base;
                if (hash_s < 0) hash_s += base;
            }
            if (hash_s == hash_t) {
                if (target.equals(source.substring(i - size_t + 1, i + 1))) return i - size_t + 1;
            }
        }

        return -1;
    }
}
