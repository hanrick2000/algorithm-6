public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return -1;

        // method 1: think what is the worst condition.
        // int min = nums[0];
        // for (int num: nums) {
        //     min = Math.min(min, num);
        // }
        // return min;

        // method 2:binary search
        int l = 0, r = nums.length - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == nums[r]) {
                // [1,1,-1,1]
                r--;
            } else if (nums[mid] > nums[r]) {
                l = mid;
            } else {
                r = mid;
            }
        }

        return nums[l] <= nums[r] ? nums[l] : nums[r];
    }
}
