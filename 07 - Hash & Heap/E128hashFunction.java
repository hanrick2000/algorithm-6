public class Solution {
    /**
     * @param key: A string you should hash
     * @param HASH_SIZE: An integer
     * @return: An integer
     */
    public int hashCode(char[] key, int HASH_SIZE) {
        // write your code here
        int magic_code = 33;
        long result = 0;

        for (char ch: key) {
            result = (result * magic_code + ch) % HASH_SIZE;
            //if (result < 0) result += HASH_SIZE;
        }

        return (int) result;
    }
}
