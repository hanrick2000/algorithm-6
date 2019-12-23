public class Solution {
    /**
     * @param n: an integer
     * @return: an ineger f(n)
     */
    public int fibonacci(int n) {
        // write your code here
        int first = 0, second = 1;
        for (int i = 1; i < n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }

        return first;
    }
}
