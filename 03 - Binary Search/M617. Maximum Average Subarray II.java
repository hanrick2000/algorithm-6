public class Solution {
    /**
     * @param nums: an array with positive and negative numbers
     * @param k: an integer
     * @return: the maximum average
     */
    public double maxAverage(int[] nums, int k) {
        // write your code here
        double l, r;
        l = r = nums[0];
        for (int i = 0; i < nums.length; i++) {
            l = Math.min(nums[i], l);
            r = Math.max(nums[i], r);
        }

        while (r - l > 1e-5) {
            double mid = l + (r - l) / 2;

            if (canFind(nums, k, mid)) {
                l = mid;
            } else {
                r = mid;
            }
        }

        return l;
    }

    private boolean canFind(int[] nums, int k, double avg) {
        double sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i] - avg;
        }

        double pre_min = 0, pre_sum = 0;
        for (int i = k; i < nums.length; i++) {
            if (sum - pre_min >= 0) return true;

            sum += nums[i] - avg;
            pre_sum += nums[i - k] - avg;
            pre_min = Math.min(pre_sum, pre_min);
        }

        return (sum - pre_min >= 0);
    }
}
