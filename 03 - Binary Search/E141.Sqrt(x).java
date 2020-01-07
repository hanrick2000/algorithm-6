public class Solution {
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    public int sqrt(int x) {
        // write your code here
        // method 2
        if (x <= 0) return 0;

        int l = 1, r = x < 2 ? x : x / 2;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            int quotient = x / mid;
            if (quotient == mid) return mid;

            if (quotient > mid) {
                l = mid;
            } else {
                r = mid;
            }
        }

        return x / r >= r ? r : l;

        // method 1
        // if (x <= 0) return 0;
        // if (x < 2) return x;

        // long l = 1, r = x / 2;
        // while (l + 1 < r) {
        //     long mid = l + (r - l) / 2;
        //     long square = mid * mid;
        //     if (square == x) return (int) mid;

        //     if (square < x) {
        //         l = mid;
        //     } else {
        //         r = mid;
        //     }
        // }

        // return (int) (r * r <= x ? r : l);
    }
}
