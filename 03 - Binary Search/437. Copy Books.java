public class Solution {
    /**
     * @param pages: an array of integers
     * @param k: An integer
     * @return: an integer
     */
    public int copyBooks(int[] pages, int k) {
        // write your code here
        int l = 0, r = Integer.MAX_VALUE;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (check(pages, mid, k)) {
                r = mid;
            } else {
                l = mid;
            }
        }

        return check(pages, l, k) ? l : r;
    }

    private boolean check(int[] pages, int limit, int k) {
        int num = 0, left = 0;
        for (int page: pages) {
            if (page > limit) return false;
            if (page > left) {
                num++;
                left = limit;
            }
            left -= page;
        }
        return num <= k;
    }
}
