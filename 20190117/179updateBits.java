public class Solution {
    /**
     * @param n: An integer
     * @param m: An integer
     * @param i: A bit position
     * @param j: A bit position
     * @return: An integer
     */
    public int updateBits(int n, int m, int i, int j) {
        // write your code here
        return ~((-1) << (31 - j) >>> (31 - j + i) << i) & n | (m << i);
    }
}
