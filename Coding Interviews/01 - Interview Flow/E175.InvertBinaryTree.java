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
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        // method 1:
        // if (root == null) return;

        // TreeNode node = root.left;
        // root.left = root.right;
        // root.right = node;

        // invertBinaryTree(root.left);
        // invertBinaryTree(root.right);

        helper(root);
    }

    private TreeNode helper(TreeNode root) {
        if (root == null) return root;

        TreeNode leftNode = helper(root.left);
        TreeNode rightNode = helper(root.right);

        root.left = rightNode;
        root.right = leftNode;

        return root;
    }
}
