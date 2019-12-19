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
     * @param root: the root of binary tree
     * @return: the length of the longest consecutive sequence path
     */
    public int longestConsecutive(TreeNode root) {
        // write your code here
        return helper(root, null, 0);
    }

    private int helper(TreeNode root, TreeNode parent, int length) {
        if (root == null) return length;

        if (parent != null && root.val == parent.val + 1) {
            length += 1;
        } else {
            length = 1;
        }

        return Math.max(length, Math.max(helper(root.left, root, length), helper(root.right, root, length)));
    }
}
