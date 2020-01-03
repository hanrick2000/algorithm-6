public class Solution {
    /**
     * @param nums: a mountain sequence which increase firstly and then decrease
     * @return: then mountain top
     */
    public int mountainSequence(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return -1;

        int l = 0, r = nums.length - 1;
        // while (l < r) {
        //     int mid = l + (r - l) / 2;
        //     if (nums[mid] >= nums[mid + 1]) {
        //         r = mid;
        //     } else {
        //         l = mid + 1;
        //     }
        // }

        // return nums[l];

        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[mid + 1]) {
                r = mid;
            } else {
                l = mid;
            }
        }

        return Math.max(nums[l], nums[r]);
    }
}
