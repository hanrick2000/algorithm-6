public class Solution {
    /*
     * @param nums: an array of integers
     * @return: nothing
     */
    public void partitionArray(int[] nums) {
        // write your code here
        int l = 0, r = nums.length - 1;
        while (l < r) {
            while (l < r && nums[l] % 2 == 1) l++;
            while (l < r && nums[r] % 2 == 0) r--;

            if (l < r) {
                int tmp = nums[l];
                nums[l++] = nums[r];
                nums[r--] = tmp;
            }
        }
    }
}
