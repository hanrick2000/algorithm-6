public class Solution {
    /**
     * @param nums: An integer array sorted in ascending order
     * @param target: An integer
     * @return: An integer
     */
    public int findPosition(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) return -1;

        int l = 0, r = nums.length - 1;
        // method 2
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;

            if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        // [1,2] 2
        if (nums[l] == target) return l;
        return -1;

        // method 1
        // while (l + 1 < r) {
        //     int mid = l + (r - l) / 2;
        //     if (nums[mid] == target) return mid;

        //     if (nums[mid] < target) {
        //         l = mid;
        //     } else {
        //         r = mid;
        //     }
        // }

        // if (nums[l] == target) return l;
        // if (nums[r] == target) return r;

        // return -1;
    }
}
