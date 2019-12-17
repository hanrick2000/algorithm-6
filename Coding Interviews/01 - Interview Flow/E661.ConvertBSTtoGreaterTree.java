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
    private int sum;

    /**
     * @param root: the root of binary tree
     * @return: the new root
     */
    public TreeNode convertBST(TreeNode root) {
        // write your code here
        sum = 0;
        helper(root);

        return root;
    }

    private void helper(TreeNode root) {
        if (root == null) return;

        if (root.right != null) helper(root.right);

        root.val = (sum += root.val);

        if (root.left != null) helper(root.left);
    }
}
