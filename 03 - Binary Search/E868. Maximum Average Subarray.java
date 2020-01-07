public class Solution {
    /**
     * @param nums: an array
     * @param k: an integer
     * @return: the maximum average value
     */
    public double findMaxAverage(int[] nums, int k) {
        // Write your code here

        // method 2：Cumulative sum
        int[] sum = new int[nums.length];
        sum[0] = nums[0];
        for (int i = 1; i < sum.length; i++) {
            sum[i] = sum[i - 1] + nums[i];
        }

        int max = sum[k - 1];
        for (int i = k; i < sum.length; i++) {
            max = Math.max(max, sum[i] - sum[i - k]);
        }

        return max * 1.0 / k;

        // method 1: Sliding Window
        // int sum = 0;
        // for (int i = 0; i < k; i++) {
        //     sum += nums[i];
        // }

        // int max = sum;
        // for (int i = k; i < nums.length; i++) {
        //     sum += nums[i] - nums[i - k];
        //     max = Math.max(sum, max);
        // }

        // return max * 1.0 / k;
    }
}
