public class Solution {
    /**
     * @param nums: An integer array sorted in ascending order
     * @param target: An integer
     * @return: An integer
     */
    public int lastPosition(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) return -1;

        int l = 0, r = nums.length - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] <= target) {
                l = mid;
            } else {
                r = mid;
            }
        }

        if (nums[r] == target) return r;
        if (nums[l] == target) return l;

        return -1;
    }
}
