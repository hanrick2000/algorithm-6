public class Solution {
    /**
     * @param n: a integer
     * @return: return a integer
     */
    public int countPrimes(int n) {
        // write your code here
        if (n < 2) return 0;

        int count = 0;
        boolean[] notPrime = new boolean[n];

        for (int i = 2; i < n; i++) {
            if (notPrime[i]) continue;

            count++;
            for (int j = 2; i * j < n; j++)
                notPrime[i * j] = true;
        }

        return count;
    }
}
