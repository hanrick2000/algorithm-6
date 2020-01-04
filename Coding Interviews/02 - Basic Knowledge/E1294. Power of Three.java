public class Solution {
    /**
     * @param n: an integer
     * @return: if n is a power of three
     */
    public boolean isPowerOfThree(int n) {
        // Write your code here
        if (n <= 0) return false;

        int num = 1;
        while (num <= n) {
            if (num == n) return true;

            num *= 3;
        }

        return false;

        //  n = Math.abs(n);
        // int num = power(3, 19);
        // return num % n == 0;

   }

    private int power(int base, int n) {
        int result = 1;
        while (n != 0) {
            if (n % 2 == 1) result *= base;
            base *= base;

            n /= 2;
        }
        return result;
    }
}
