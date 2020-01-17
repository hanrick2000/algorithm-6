/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param nums: an array
     * @return: the maximum tree
     */
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        // Write your code here
        if (nums == null || nums.length == 0) return null;

        return helper(nums, 0, nums.length - 1);
    }

    private TreeNode helper(int[] nums, int l, int r) {
        if (l > r) return null;

        int index = l;
        for (int i = l + 1; i <= r; i++) {
            if (nums[i] > nums[index]) index = i;
        }

        TreeNode root = new TreeNode(nums[index]);
        root.left = helper(nums, l, index - 1);
        root.right = helper(nums, index + 1, r);

        return root;
    }
}
