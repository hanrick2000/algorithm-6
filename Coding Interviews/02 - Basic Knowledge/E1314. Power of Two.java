public class Solution {
    /**
     * @param n: an integer
     * @return: if n is a power of two
     */
    public boolean isPowerOfTwo(int n) {
        // Write your code here
        if (n <= 0) return false;

        return (n & (n - 1)) == 0;
    }
}
