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
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    public boolean isValidBST(TreeNode root) {
        // write your code here
        return helper(root, null, null);
    }

    private boolean helper(TreeNode root, Integer lower, Integer upper) {
        if (root == null) return true;

        int value = root.val;
        if (lower != null && lower >= value) return false;
        if (upper != null && upper <= value) return false;

        if (!helper(root.right, value, upper)) return false;
        if (!helper(root.left, lower, value)) return false;

        return true;
    }
}
